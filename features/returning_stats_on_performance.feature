
Feature: Returning stats on performance
  
  Scenario: Returning stats on performance
    Given we have identified a position of "third man"
     When we make the following guesses
       | guess      |
       | mid off    |
       | long on    |
       | third man  |
     Then we should return the results
       | status     | rating |
       | incorrect  | 7      |
       | incorrect  | 10     |
       | correct    | 0      |
     And we should return the stats
       | stat           | value |
       | total_guesses  | 3     |
       | average_rating | 5.67   |

  Scenario: Returning stats on performance
    Given we have identified a position of "long on"
     When we make the following guesses
       | guess      |
       | mid off    |
       | long off   |
       | third man  |
       | long on    |
     Then we should return the results
       | status     | rating |
       | incorrect  | 4      |
       | incorrect  | 3      |
       | incorrect  | 10      |
       | correct    | 0      |
     And we should return the stats
       | stat           | value |
       | total_guesses  | 4     |
       | average_rating | 4.25   |