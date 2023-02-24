Feature: Test login form

  Scenario: Login successful
    When I go to login page
    When I key in my email address 'stx6@outlook.com'
    And I key in my password 'stx123321'
    And I click on Log in
    Then I should see my landing page title 'GOAT OCR'