Feature: Validate the Save Data API feature

  @duplicate_video_content
  Scenario Outline: Verify Save API is storing data successfully
    Given User posts a request
    When request "<url>" is successfull
    Then User should be able to verify the response "<status>"
  Examples:
    |url|status|
    |https://api.elucidat.com/v4/usage/store?bms=1|success|
    