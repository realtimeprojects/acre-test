@tid:9009
@regression
@search
Feature: Login to my account
    login then logout to my account

    Scenario: login/logout with my private account
        Given I start the chromium browser
        When I navigate to 'https://hunting.zeiss.com/'
        Then I see 'ZEISS Hunting' in the page title

        When I login to Hazem profile
        Then I agree to the privacy Agreement
        Then I see my Dashboard page

        Then I close the browser
