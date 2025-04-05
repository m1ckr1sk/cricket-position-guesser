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
       | incorrect  | 8      |
       | incorrect  | 7      |
       | incorrect  | 3      |