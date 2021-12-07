from functools import reduce

class BingoBoard:
  board = []
  def __init__(self, board):
    self.board = board

  def mark(self, number):
    for r,row in enumerate(self.board):
      for c,column in enumerate(row):
        cell, marked = column
        if cell == number:
          self.board[r][c] = (cell, True)
          return self.wins_row(r) or self.wins_column(c)

  def is_winning_row(self, row):
    return reduce(lambda lhs, rhs: lhs and rhs, map(lambda tup: tup[1], row))

  def wins_row(self, r):
    return self.is_winning_row(self.board[r])

  def wins_column(self, c):
    return self.is_winning_row([row[c] for row in self.board]) 

  def calculate_score(self):
    score = 0
    for row in self.board:
      for number, marked in row:
        if not marked:
          score += number

    return score

boards = []
f = open('day4.txt', 'r')
outcomes = map(int, f.readline().split(','))

while f.readline():
  board = []
  for i in range(5):
    row = list(zip(map(int, f.readline().split()), [False for f in range(5)]))
    board.append(row)

  boards.append(BingoBoard(board))

first_win = 0
winning_score = 0

for outcome in outcomes:
  for board in boards:
    if board.mark(outcome):
      winning_score = board.calculate_score() * outcome
      boards.remove(board)
      if first_win == 0:
        first_win = winning_score

print("Part 1: %d" % first_win)
print("Part 2: %d" % winning_score)
