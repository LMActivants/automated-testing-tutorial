Feature: Test Edit Profile form

  Scenario: Update name
    When I click on my username
    When I click on Edit Profile
    Then I should see Edit Profile
    When I update my username
    When I click on Update
    When I click on Back
    When I click on my username
    When I click on View Profile
    Then I should see my updated username
