@regression
@tid:9003
Feature: Use a local step definition
    In order to extend the existing step library with additional steps
    I need to be able to add my own step definition inside the test project
    to test unsupported items

    Scenario: Use local step definition
        Given nothing
        Then I run my own acre-test step
