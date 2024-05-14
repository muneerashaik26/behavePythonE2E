from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from datetime import *
from datetime import datetime
import requests


class CaseJudgementPage(BasePage):
    #Locators
    TXT_USERNAME = (By.XPATH, "//input[@name='username']")
    TXT_PASSWORD = (By.XPATH, "//input[@name='password']")
    BTN_START = (By.XPATH, "//a/span[text()='START']")
    MSG_INVALIDCREDS = (By.ID,"spanMessage")
    SPINNER_ELE = (By.XPATH, "//div[@class='spinner_wrapper']/img")
    TXT_PAGELOAD = (By.XPATH, "//div[@class='template_wrapper']/h1/strong")
    CASE_SELECTION_PAGE_TITLE_ELE = (By.XPATH, "//*[contains(text(),'Press on a case')]")
    SCORE_SELECTION_ELE = (By.XPATH, "(//div[@class='htmlText']/p)[2]")
    FIRST_CASE_SELECT_ELE = (By.XPATH, "//div/span[@class='text caption__text' and contains(text(),'Making a case against Kevin')]") 
    SECOND_CASE_SELECT_ELE = (By.XPATH, "//div/span[@class='text caption__text' and contains(text(),'Who is to blame?')]")
    CASE1_PAGE_MESSAGE = (By.XPATH, "//div[@id='pa_5c9126fe434ba_p154ce332d27-text']")
    CASE1_VIDEO_ATTRIBUTES = (By.XPATH, "//div[contains(@class, 'Title_module_headers__')]/a[1]")
    JUDGE_MSG =  (By.XPATH, "//div[@id='pa_5c9126fe434ba_p1550efedbe9-text']")
    JUDGE_BTN_LINK = (By.XPATH, "//a[@id='pa_5c9126fe434ba_p15564daa856-textButton']")
    JUDGE_VOTE_PAGE_MSG = (By.XPATH, "(//div[@class='htmlText'])[1]")
    VOTE_BTN = (By.XPATH, "//a[@id='pa_5c9126fe47260_p15515116385-save_button']")
    POPUP_MODAL_OVERLAY =  (By.XPATH, "(//div[@class='mod__header modal__header'])[2]")
    POPUP_HEADER = (By.XPATH, "(//div[@class='col__inner']/h2[contains(@id,'modalTitle')]/strong)[2]")
    POPUP_BODY_MSG1 = (By.XPATH, "//div[@id='pa_5c9126fe47260_p1554e607e46-modal__text']/p[1]")
    POPUP_BODY_MSG2 = (By.XPATH, "//div[@id='pa_5c9126fe47260_p1554e607e46-modal__text']/p/em")
    CONTINUE_BTN = (By.XPATH, "(//span[@class='button__text' and contains(text(),'CONTINUE')])[2]")
    CONTINUE_BTN_NXT = (By.XPATH, "//a[@id='pa_5c9126fe4b742_p15550a254a1-textButton']")
    CONTINUE_BTN_NXT1 = (By.XPATH, "//a[@id='pa_5c9126fe4f952_p15578944323-textButton']")
    RELIABLE_RADIO_BTN = (By.XPATH, "//label[contains(text(),'Can be')]/../..//span[@class='icon icon--secondary']")
    VOTE_BTN1 = (By.XPATH, "//a[@id='pa_5c9126fe5331b_p155cc4e94a5-save_button']")
    DISMISS_BTN = (By.XPATH, "//a[@id='pa_5c9126fe5331b_p155cc4e96eb-dismiss_button']")
    VOTE_BTN2 = (By.XPATH, "//a[@id='pa_5c9126fe57197_p155cc4e94a5-button__text']")



    # Variables
    case1_video_link_actual=""
    case1_video_title_actual=""
    case2_video_link_actual=""
    case2_video_title_actual=""


    def __init__(self, driver):
        super().__init__(driver)



    def startCaseJudgement(self):
        self.click_element(self.BTN_START)

    def validateTitle(self):
        assert self.get_element_text(self.TXT_PAGELOAD) == "FINDING THE TRUTH"

    def validateCaseSelectionPageLoad(self):
        self.verify_element_displayed(self.TXT_PAGELOAD)
        self.verify_element_displayed(self.CASE_SELECTION_PAGE_TITLE_ELE)
        assert self.get_element_text(self.CASE_SELECTION_PAGE_TITLE_ELE) == "Press on a case to get started."

    def waitForSpinnerToDisappear(self):
        self.verify_spinner_disappear(self.SPINNER_ELE)


    def verifyScoreOnPage(self):
        self.verify_element_displayed(self.SCORE_SELECTION_ELE)
        score_val = self.get_element_text(self.SCORE_SELECTION_ELE)
        A = score_val.split(":")
        actual_score = A[1]
        today = datetime.today()
        formatted_date = today.strftime("%#m/%#d/%y")
        # assert actual_score == formatted_date
        assert bool(actual_score.isdigit()) == True, " \"Your Final Score\" on landing page must have numeric score but it wrongly shows current date  => %s" % actual_score

    def selectCaseToJudge(self,case):
        if case == "case1":
            self.verify_element_displayed(self.FIRST_CASE_SELECT_ELE)
            self.click_Ele(self.FIRST_CASE_SELECT_ELE)
            self.verify_element_displayed(self.CASE1_PAGE_MESSAGE)
            selected_case_details_actual = self.get_element_attribute(self.CASE1_PAGE_MESSAGE,"innerText")
            selected_case_details_expected = "A murder has been committed in an alleyway outside a pub.\n\n\nWatch the video to find out exactly what happened."
            assert selected_case_details_expected in selected_case_details_actual, "Text not found %s" % selected_case_details_expected
        elif case == "case2":
            self.verify_element_displayed(self.SECOND_CASE_SELECT_ELE)
            self.click_element(self.SECOND_CASE_SELECT_ELE)
            self.verify_element_displayed(self.CASE1_PAGE_MESSAGE)
            selected_case_details_actual = self.get_element_attribute(self.CASE1_PAGE_MESSAGE,"innerText")
            selected_case_details_expected = "A murder has been committed in an alleyway outside a pub.\n\n\nWatch the video to find out exactly what happened."
            assert selected_case_details_expected in selected_case_details_actual, "Text not found %s" % selected_case_details_expected
        else:
            print("Pass correct case to proceed Further")        

    def verifyCaseVideoData(self,title):
        self.verify_element_displayed(self.CASE1_PAGE_MESSAGE)
        ele = self.get_Inner_Text(self.JUDGE_MSG)
        assert ele == "Press 'Judge This' once you have watched it."
        self.switch_to_frame();
        global case1_video_title_actual
        case1_video_title_actual = self.get_element_attribute(self.CASE1_VIDEO_ATTRIBUTES,"innerText") 
        global case1_video_link_actual
        case1_video_link_actual = self.get_element_attribute(self.CASE1_VIDEO_ATTRIBUTES,"href")
        r = requests.head(case1_video_link_actual)
        print(case1_video_link_actual, r.status_code)
        assert r.status_code == 200, " Video link => %s"+ case1_video_link_actual+ " must return status " + r.status_code
        # assert case1_video_title_actual == title


    def verifyCase2VideoData(self):
        self.verify_element_displayed(self.CASE1_PAGE_MESSAGE)
        self.switch_to_frame();
        global case2_video_title_actual
        case2_video_title_actual = self.get_element_attribute(self.CASE1_VIDEO_ATTRIBUTES,"innerText") 
        global case2_video_link_actual
        case2_video_link_actual = self.get_element_attribute(self.CASE1_VIDEO_ATTRIBUTES,"href")
        # case2_video_link_expected="Crime Myths - Case 1, Part 1"
        # assert case2_video_title_actual == case2_video_link_expected

    def validateVideoTitle(self):
        assert case1_video_title_actual != case2_video_title_actual, "Case 1 Video Title is -> "+ case1_video_title_actual +" should not match with case 2 video title  => %s" % case1_video_title_actual


    def validateVideoLink(self):
        assert case1_video_link_actual != case2_video_link_actual, "Case 1 Video Link is -> "+ case1_video_title_actual +" should not match with case 2 video Link  => %s" % case1_video_title_actual



    def clickJudgeThisBtn(self):
        self.click_element(self.JUDGE_BTN_LINK)

    def judgeCasePageLoad(self):
        self.verify_element_displayed(self.JUDGE_VOTE_PAGE_MSG)
        self.verify_element_displayed(self.VOTE_BTN)

    def verifyJudgeQuestion(self):
        JudgementPageMessage = self.get_element_attribute(self.JUDGE_VOTE_PAGE_MSG,"innerText") 
        JudgementDetails = "Based on what you know about the case against Kevin so far..."
        JudgementQuestion = "Is Kevin guilty?"
        assert JudgementDetails in JudgementPageMessage
        assert JudgementQuestion in JudgementPageMessage

    def clickVoteBtn(self):
        self.click_Ele(self.VOTE_BTN)
    
    def clickContinueBtn(self):
        self.click_element(self.CONTINUE_BTN)

    def clickContinueBtnNxt(self):
        # self.scroll_to_view(self.CONTINUE_BTN_NXT)
        self.click_element(self.CONTINUE_BTN_NXT)


    def clickContinueBtnNxt1(self):
        # self.scroll_to_view(self.CONTINUE_BTN_NXT)
        self.click_element(self.CONTINUE_BTN_NXT1)



    def clickReliableBtn(self):
        self.click_element(self.RELIABLE_RADIO_BTN)


    def clickVoteBtn1(self):
        self.click_element(self.VOTE_BTN1)

    def clickVoteBtn2(self):
        self.click_element(self.VOTE_BTN2)

    def clickContinueDismissBtn(self):
        self.click_element(self.DISMISS_BTN)



    def selectJudgementInput(self,judgementInput):
        JUDGEMENT_INPUT_XPATH_STR ="//label/strong[contains(text(),'"+"DEFAULTVAL"+"')]/../..//span[@class='icon icon--secondary']"
        FINAL_XPATH = JUDGEMENT_INPUT_XPATH_STR.replace("DEFAULTVAL",judgementInput)
        JUDGEMENT_INPUT_ELE = (By.XPATH, FINAL_XPATH)
        self.verify_element_displayed(JUDGEMENT_INPUT_ELE)
        self.click_Ele(JUDGEMENT_INPUT_ELE)


    def checkPopupIsDisplayed(self):
        self.verify_element_displayed(self.POPUP_MODAL_OVERLAY)

    def verifyPopupHeader(self,InputSelected):
        FinalInputSelected = InputSelected.upper()+"!"
        self.verify_element_displayed(self.POPUP_MODAL_OVERLAY)
        self.verify_element_displayed(self.POPUP_HEADER)
        popup_header_actual = self.get_element_text(self.POPUP_HEADER)
        assert FinalInputSelected == popup_header_actual, "Form input selected is -> "+ InputSelected +" But popup has wrong popup Header => %s" % popup_header_actual


    def verifyPopupBody(self,InputSelected,text_not_to_present):
        self.verify_element_displayed(self.POPUP_MODAL_OVERLAY)
        self.verify_element_displayed(self.POPUP_BODY_MSG1)
        popup_body_actual_msg = self.get_element_text(self.POPUP_BODY_MSG1)
        print(popup_body_actual_msg)
        assert text_not_to_present not in popup_body_actual_msg, "Form input selected is -> "+ InputSelected +"  showing wrong popup message => %s" % popup_body_actual_msg