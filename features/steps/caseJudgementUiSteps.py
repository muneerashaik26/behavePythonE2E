from behave import *
from selenium import webdriver
from configuration.config import TestData
from pages.CaseJudgementPage import CaseJudgementPage
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

@given(u'User has launched the browser')
def launch_browser(context):
    if TestData.BROWSER == 'chrome':
        chromedriver_autoinstaller.install()
        chrome_options = Options()
        # chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")
        context.driver = webdriver.Chrome(options=chrome_options)
        # context.driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH,options=chrome_options)
    elif TestData.BROWSER == 'firefox':
        context.driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    else:
        raise ValueError('Browser is not supported')


@when(u'User opens the Case Judgement Portal')
def open_caseJudgement_page(context):
    try:
        context.driver.get(TestData.URL)
        context.CaseJudgementPage = CaseJudgementPage(context.driver)
    except:
        context.driver.close()
        assert False,"Test is failed in open login page section"

@then(u'The portal must be launched succesfully')
def validate_case_judgement_landing_page(context):
    try:
        context.CaseJudgementPage.waitForSpinnerToDisappear()
        context.CaseJudgementPage.validateTitle()
    except:
        context.driver.close()
        assert False, "Test is failed in validate login page title"


@when(u'User Clicks the Start button on the case judgement landing page')
def start_case_judgement(context):
    try:
        context.CaseJudgementPage.startCaseJudgement()
    except:
        context.driver.close()
        assert False, "Test is failed in start case button click page"

@then(u'User must navigate to the case selection page to select a case')
def navigate_to_case_selection_page(context):
    try:
        context.CaseJudgementPage.validateCaseSelectionPageLoad()
    except:
        # context.driver.close()
        assert False, "Test is failed case detail selection title validation"

@then(u'User must verify that case selection page must display valid score value')
def verify_Score_on_page(context):
    context.CaseJudgementPage.verifyScoreOnPage()



@when(u'User selects case "{item}"')
def select_case(context,item):
    context.CaseJudgementPage.selectCaseToJudge(item)

@when(u'User verifies case 1 video for title "{title}" and link')
def verify_case1_video_data(context,title):
    context.CaseJudgementPage.verifyCaseVideoData(title)

@when(u'User verifies case 2 video for title and link')
def verify_case2_video_data(context):
    context.CaseJudgementPage.verifyCase2VideoData()

@then(u'User must verify that case 1 video attributes should not match case 2 video attaributes title and link')
def validate_video_attributes(context):
    context.CaseJudgementPage.validateVideoTitle()
    context.CaseJudgementPage.validateVideoLink()

@when(u'User clicks on JUDGE THIS button')
def click_judge_this_btn(context):
    context.CaseJudgementPage.clickJudgeThisBtn()

@then(u'User must succesfully navigate to vote page to judge the case selected')
def judge_case_page_load(context):
    context.CaseJudgementPage.judgeCasePageLoad()
    context.CaseJudgementPage.verifyJudgeQuestion()

@then(u'Users selects the judgement input "{judgementInput}" from the form')
def select_judgement(context,judgementInput):
    context.CaseJudgementPage.selectJudgementInput(judgementInput)

    

@then(u'User clicks on VOTE button')
def click_vote_btn(context):
    context.CaseJudgementPage.clickVoteBtn()


@then(u'User clicks on Continue button')
def click_continue_btn(context):
    context.CaseJudgementPage.clickContinueBtn()


@then(u'User is redirected to a popup')
def popup_dispalyed(context):
    context.CaseJudgementPage.checkPopupIsDisplayed()


@then(u'the input selected "{InputSelected}" must match the popup Header displayed')
def click_vote_btn(context,InputSelected):
    context.CaseJudgementPage.verifyPopupHeader(InputSelected)



@then(u'the input selected "{InputSelected}" must match the popup Body message "{text_not_to_present}"')
def click_vote_btn(context,InputSelected,text_not_to_present):
    context.CaseJudgementPage.verifyPopupBody(InputSelected,text_not_to_present)


@then(u'Close the browser')
def step_impl(context):
    context.driver.close()