# Tic Tac Toe Minimax

A python3 bot that plays tic-tac-toe perfectly using minimax!

You'll need python3 to run it.

- Check out minimax on [Wikipedia](https://en.wikipedia.org/wiki/Minimax).
- We full brute force the entire decision tree (it's pretty small with a maximum of 3^9 == 19k).
- Interesting next steps include:
  - Suppose you're evaluating two nodes on a max step. From node1 you there are n subtrees that maximize the score and from node2, there are m subtrees that maximize the score. If n > m, then we should always prefer node1 over node2 because it provides the highest chance of the min player to make a mistake.
  - Generify to any game beyond tic-tac-toe.
  - Train an neural network to play perfectly! Given that there's only 19k total board states, it'll be an ineteresting balance between playing perfectly and overfitting (i.e. memorizing how this bot plays for every single possible position).
