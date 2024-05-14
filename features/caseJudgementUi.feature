Feature: Validate the case judgement feature

  Background:
    Given User has launched the browser
    When User opens the Case Judgement Portal
    Then The portal must be launched succesfully
    When User Clicks the Start button on the case judgement landing page
    Then User must navigate to the case selection page to select a case

  @valid_score
  Scenario: Verify Functional Bug 1 >> The Case selection page shows score as current date where as it should be a valid numeric score value
    Then User must verify that case selection page must display valid score value
    Then Close the browser


  @duplicate_video_content
  Scenario: Verify Functional Bug 2 >> The Case selection page shows two different titled cases to chose a case and upon selection both have same video being played
    When User selects case "case1"
    And User verifies case 1 video for title "Crime Myths - Case 1, Part 1" and link
    When User opens the Case Judgement Portal
    When User selects case "case2"
    And User verifies case 2 video for title and Link
    Then User must verify that case 1 video attributes should not match case 2 video attaributes title and link
    Then Close the browser


  @WrongJudgementPopupMsgs
  Scenario Outline: Verify Functional Bug 3 >> When User selects judgement input as GUILTY/NOT GUILTY the popup after clicking Vote button shows wrong header and message
    When User selects case "case1"
    And User clicks on JUDGE THIS button
    Then User must succesfully navigate to vote page to judge the case selected
    Then Users selects the judgement input "<judgementInput>" from the form
    And User clicks on VOTE button
    Then User is redirected to a popup
    And the input selected "<judgementInput>" must match the popup Header displayed
    And the input selected "<judgementInput>" must match the popup Body message "<text_not_to_present>"
    Then Close the browser
    Examples:
      | judgementInput | text_not_to_present|
      | Guilty| innocent|
      | Not guilty    | guilty|

