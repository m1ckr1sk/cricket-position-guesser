Feature: Making multiple guesses

  Scenario: Making incorrect guesses
    Given we have identified a position
     When we make the following guesses
       | guess      |
       | mid off    |
       | long on    |
       | third man  |
     Then we should return the results
       | status     | rating |
       | incorrect  | 2      |
       | incorrect  | 3      |
       | incorrect  | 7      |

  Scenario: Making correct guesses
    Given we have identified a position of "third man"
     When we make the following guesses
       | guess      |
       | mid off    |
       | long on    |
       | third man  |
     Then we should return the results
       | status     | rating |
       | incorrect  | 7      |
       | incorrect  | 10      |
       | correct    | 0      |