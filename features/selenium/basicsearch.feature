@tid:9002
@regression
@search
Feature: Search for data
    Search for data

    Scenario: search for huhu
        Given I start the chromium browser
        When I navigate to 'http://www.duckduckgo.com'
        When I search for 'python.org'
        Then I see the link 'Welcome to Python.org'
        Then I close the browser
