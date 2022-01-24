@tid:9002
@regression
@search
Feature: Search for data
    Search for data

    Scenario: search for huhu
        Given I start the chromium browser
        When I navigate to 'http://www.github.com'
        Then I search for 'huhu'
        Then I close the browser
