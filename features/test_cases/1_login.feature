Feature: Test login form

  Scenario: Login successful
    Given I go to login page
    When I key in my email address
    When I key in my password
    When I click on Log in
    Then I should see my landing page