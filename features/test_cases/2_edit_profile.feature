Feature: Test Edit Profile form

  Scenario Outline: Update name
    Given I am in landing page
    When I click on my username
    And I click on Edit Profile
    Then I should see Edit Profile
    When I update my username '<username>'
    And I click on Update
    And I click on Back
    When I click on my username
    And I click on View Profile
    Then I should see my updated username '<outcome>'

    Examples: Sample user name
      | username | outcome |
      | tinxiao  | tinxiao |
      | lmheng   | lmheng  |