**To solve this problem, we need to determine the winner of each round of the game where Maria and Ben alternately choose prime numbers from a set of integers starting from 1 up to 
𝑛. The player who cannot make a move loses the game. Maria always starts first.**

### Here's the approach we'll take to solve the problem:

1- Prime Number Calculation: Use the Sieve of Eratosthenes to compute all prime numbers up to the maximum efficiency 𝑛 in the list nums. This will help us quickly determine if a number is prime during gameplay.

2. Game Simulation (Dynamic Programming): For each game round:

**.** Compute which player wins using dynamic programming. We'll create a dp array where dp[i] indicates whether the player whose turn it is to play optimally can win starting from number 𝑖.

. Base cases:
  - `dp[0] = False` (if there are no numbers left, the player loses)
  - `dp[1] = False` (if there's only 1 left, the player loses)

. for other numbers, compute whether the current player can force a win by checking if they can leave the opponent in a position where they cannot move.

3. Winner Determination: After computing the results for each game round, count the wins for Maria and Ben and determine the player who won the most rounds. If there's a tie or no winner can be determined (unlikely per problem constraints), return None.
