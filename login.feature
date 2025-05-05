Feature: Teacher login
  Scenario: User goes to login page
    Given the user is on the /login page
    then the user sees a login form
    and the form has a username field
    and the form has a password field
    and the form has a role selection field
    and the form has a submit button

  Scenario: User selects the role
    Given the user is on the /login page
    When the user open the role dropdown
    Then the user sees all available roles

  Scenario: User selects the role
    Given the user is on the /login page
    When the user types a username
    And the user types a password
    Then both are checked against the database
    And the user is then an authenticated user

  Scenario: Teacher tries to login
    Given an authenticated user of type Teacher
    When the user tries to login
    Then the password is checked
    And the user to a page with a "Hello Teacher" message

  Scenario: Student tries to login
    Given and authenticated user of type Student
    When the user tries to login
    The login is rejected
    And the user sees an "Wouldn't you like to manage your own grades eh, would you?" message

Feature: User Login

  Scenario: Successful login
    Given I am on the login page
    When I enter valid credentials
    And I click the login button
    Then I should be redirected to the dashboard

  Scenario: Unsuccessful login
    Given I am on the login page
    When I enter invalid credentials
    And I click the login button
    Then I should see an error message
