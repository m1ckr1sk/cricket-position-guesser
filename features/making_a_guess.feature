Feature: Making a guess

  Scenario: Making an incorrect guess
    Given we have idnentified a position
     When we make an incorrect guess
     Then we should return the incorrect position
     And its rating based on distance to correct position