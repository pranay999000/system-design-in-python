class ConnectFour:

	def __init__(self):
		self.board = [["x" for _ in range(7)] for _ in range(6)]
	
	def check_sequence(self, row, col, color):
		
		i, count = 0, 0

		while row + i < len(self.board):
			
			if self.board[row + i][col] != color:
				break

			i, count = i + 1, count + 1

			if count == 4:
				return True
		
		i, count = 0, 0

		while row + i < len(self.board) and col - 1 > 0:

			if self.board[row + i][col - i] != color:
				break

			i, count = i + 1, count + 1

			if count == 4:
				return True
		
		i, count = 0, 0

		while row + i < len(self.board) and col + i < len(self.board[0]):

			if self.board[row + i][col + i] != color:
				break

			i, count = i + 1, count + 1

			if count == 4:
				return True
		
		i, count = 0, 0

		while col + i < len(self.board[0]):

			if self.board[row][col + i] != color:
				break

			i, count = i + 1, count + 1

			if count == 4:
				return True
		
		i, count = 0, 0

		while col - i > -1:

			if self.board[row][col - i] != color:
				break

			i, count = i + 1, count + 1

			if count == 4:
				return True
		
		return False

	def move(self, color, column):

		if column > len(self.board[0]) or column < 0:
			print("Invalid Move!")
			return
		
		if self.board[0][column] != "x":
			print("Invalid Move!")
			return

		for i in range(len(self.board) - 1, -1, -1):
			
			if self.board[i][column] == "x":
				self.board[i][column] = color
				
				if self.check_sequence(i, column, color):
					self.print_board()
					print(color, "Wins!")
					return
				break
		
		self.print_board()

	def print_board(self):

		for row in self.board:
			for val in row:
				print("|", end = "")
				print("{}".format(val).center(10, ' '), end="")
				print("|", end = "")
			
			print("\n")
		print("\n")

board = ConnectFour()

board.move("RED", 2)
board.move("YELLOW", 1)
board.move("RED", 3)
board.move("YELLOW", 1)
board.move("RED", 4)
board.move("YELLOW", 1)
board.move("RED", 5)