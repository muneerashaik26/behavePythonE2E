from selenium.webdriver import ActionChains
from  selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, TimeoutException, NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, InvalidSelectorException as EX
from selenium.webdriver.common.by import By

"""This class is the parent of all the page classes"""
"""It contains all the common action methods and utilities for all the pages"""

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].click();", element)
        except EX as e:
            print("Exception! Can't click on the element")

    def input_element(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except EX as e:
            print("Exception! Can't click on the element")

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return element.text
        

    def get_title(self):
        return self.driver.title

    def get_element_attribute(self, by_locator, attribute_name):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute_name)

    def verify_element_displayed(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()
        except:
            return False
        

    def verify_spinner_disappear(self, by_locator):
        try:
            WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(by_locator))
        except EX as e:
            print("Exception! Element is still present")


    def click_Ele(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        except EX as e:
            print("Exception! Can't click on the element")

    def get_Inner_Text(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute('innerText')

    def switch_to_frame(self):
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='video1']")))

    def scroll_to_view(self,by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

