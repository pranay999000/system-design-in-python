
class Move:
	def move(self, start_cell, end_cell):
		end_cell.piece = start_cell.piece
		start_cell.piece = None
	
	def color_check(self, x, y, start_cell):
		if board.get_cell(x, y).piece is not None and board.get_cell(x, y).piece.color == start_cell.color:
			return False
		return True

	def action(self, start_cell, end_cell):
		if start_cell is None:
			print("Invalid move!")
			return
		
		if end_cell.piece is not None and end_cell.piece.color == start_cell.piece.color:
			print("Invalid move!")
			return

		x1 = start_cell.x
		y1 = start_cell.y

		x2 = end_cell.x
		y2 = end_cell.y

		if start_cell.piece.name == "pawn":
			d = 0
			if start_cell.piece.color == 'black':
				d += 1
			else:
				d -= 1

		
			if x1 + d == x2 and self.color_check(x2, y2, start_cell):
				self.move(start_cell, end_cell)
				return
			if x1 + d + d == x2 and self.color_check(x2, y2, start_cell):
				self.move(start_cell, end_cell)
				return
			if x1 + d == x2 and (y1 + 1 == y2 or y1 - 1 == y2) and not self.color_check(x2, y2, start_cell):
				self.move(start_cell, end_cell)
				return
			
			print('Invalid move!')
			return

		
		if start_cell.piece.name == 'rook':
			if x1 == x2:
				c = 0
				if y1 < y2:
					c += 1
				else:
					c -= 1
				
				for i in range(y1 + c, y2 + c, c):
					if i == y2:
						if not self.color_check(x1, i, start_cell):
							print('Invalid move!')
							return
						self.move(start_cell, end_cell)
						return
					if board.get_cell(x1, i).piece is not None:
						print('Invalid move!')
						return
			
			if y1 == y2:
				c = 0
				if x1 < x2:
					c += 1
				else:
					c -= 1

				for i in range(x1 + c, x2 + c, c):
					if i == x2:
						if not self.color_check(i, y1, start_cell):
							print('Invalid move!')
							return
						self.move(start_cell, end_cell)
						return
					if board.get_cell(i, y1).piece is not None:
						print('Invalid move!')
						return

		if start_cell.piece.name == 'knight':
			if x1 < x2 and y1 < y2:
				if x1 + 2 == x2 and y1 + 1 == y2 and self.color_check(x2, y2, start_cell):
					self.move(start_cell, end_cell)
					return
				if x1 + 1 == x2 and y1 + 2 == y2 and self.color_check(x2, y2, start_cell):
					self.move(start_cell, end_cell)
					return
			if x2 < x1 and y1 < y2:
				if x1 - 2 == x2 and y1 + 1 == y2 and self.color_check(x2, y2, start_cell):
					self.move(start_cell, end_cell)
					return
				if x1 - 1 == x2 and y1 + 2 == y2 and self.color_check(x2, y2, start_cell):
					self.move(start_cell, end_cell)
					return
			if x2 < x1 and y2 < y1:
				if x1 - 2 == x2 and y1 - 1 == y2 and self.color_check(x2, y2, start_cell):
					self.move(start_cell, end_cell)
					return
				if x1 - 1 == x2 and y1 - 2 == y2 and self.color_check(x2, y2, start_cell):
					self.move(start_cell, end_cell)
					return
			if x1 < x2 and y2 < y1:
				if x1 + 2 == x2 and y1 - 1 == y2 and self.color_check(x2, y2, start_cell):
					self.move(start_cell, end_cell)
					return
				if x1 + 1 == x2 and y1 - 2 == y2 and self.color_check(x2, y2, start_cell):
					self.move(start_cell, end_cell)
					return
			
			print('Invalid move!')
			return

		if start_cell.piece.name == 'bishop':
			m = 0
			n = 0

			if x1 < x2 and y1 < y2:
				m += 1
				n += 1
			if x2 < x1 and y1 < y2:
				m -= 1
				n += 1
			if x2 < x1 and y2 < y1:
				m -= 1
				n -= 1
			if x1 < x2 and y2 < y1:
				m += 1
				n -= 1
			
			i = x1
			j = y1

			while i < 8 and i > -1 and j < 8 and j > -1:
				i += m
				j += n

				if i == x2 and j == y2:
					if self.color_check(i, j, start_cell):
						self.move(start_cell, end_cell)
						return
					print('Invalid move!')
					return
				if board.get_cell(i, j).piece is not None:
					print('Invalid move!')
					return
			
			print('Invalid move!')
			return
		
		if start_cell.piece.name == 'queen':
			m = 0
			n = 0

			if x1 < x2:
				m += 1
			if y1 < y2:
				n += 1
			if x2 < x1:
				m -= 1
			if y1 < y2:
				n += 1
			if x2 < x1:
				m -= 1
			if y2 < y1:
				n -= 1
			if x1 < x2:
				m += 1
			if y2 < y1:
				n -= 1
			
			i = x1
			j = x2

			while i < 8 and i < -1 and j < 8 and j > -1:
				i += m
				j += n

				if i == x2 and j == y2:
					if self.color_check(i, j, start_cell):
						self.move(start_cell, end_cell)
						return
					print('Invalid move!')
					return
				if board.get_cell(i, j).piece is not None:
					print('Invalid move!')
					return
			
			print('Invalid move!')
			return

		if start_cell.piece.name == 'king':
			m = 0
			n = 0

			if x1 < x2:
				m += 1
			if y1 < y2:
				n += 1
			if x2 < x1:
				m -= 1
			if y1 < y2:
				n += 1
			if x2 < x1:
				m -= 1
			if y2 < y1:
				n -= 1
			if x1 < x2:
				m += 1
			if y2 < y1:
				n -= 1
			
			if x1 + m == x2 and y1 + n == y2:
				if self.color_check(x2, y2, start_cell):
					self.move(start_cell, end_cell)
					return
				print('Invalid move!')
				return
			print('Invalid move!')
			return
		
		print('Invalid move!')
		return
					


class Piece:
	def __init__(self, color, name):
		self.color = color
		self.name = name

class Cell:
	def __init__(self, piece, x, y):
		self.piece = piece
		self.x = x
		self.y = y

class Board(Move):
	def __init__(self):
		self.board = [ [ Cell(None, -1, -1) for _ in range(8) ] for _ in range(8) ]
		for i in range(8):
			for j in range(8):
				self.board[i][j].x = i
				self.board[i][j].y = j
		
		self.board[7][0].piece = self.board[7][5].piece = Piece('white', 'rook')
		self.board[7][1].piece = self.board[7][6].piece = Piece('white', 'knight')
		self.board[7][2].piece = self.board[7][7].piece = Piece('white', 'bishop')
		self.board[7][3].piece = Piece('white', 'queen')
		self.board[7][4].piece = Piece('white', 'king')

		self.board[0][0].piece = self.board[0][5].piece = Piece('black', 'rook')
		self.board[0][1].piece = self.board[0][6].piece = Piece('black', 'knight')
		self.board[0][2].piece = self.board[0][7].piece = Piece('black', 'bishop')
		self.board[0][3].piece = Piece('black', 'queen')
		self.board[0][4].piece = Piece('black', 'king')

		for i in range(8):
			self.board[6][i].piece = Piece('white', 'pawn')
			self.board[1][i].piece = Piece('black', 'pawn')

	def print_board(self):
		for i in range(8):
			for j in range(8):
				cell = self.board[i][j]
				print('|', end='')
				if cell.piece is not None:
					if cell.piece.color == 'white':
						print('{}-{}'.format('w', cell.piece.name[:2]).center(10, ' '), end='')
					if cell.piece.color == 'black':
						print('{}-{}'.format('b', cell.piece.name[:2]).center(10, ' '), end='')
				else:
					print('x'.center(10, ' '), end='')
			print('|\n')
		print("\n")
		
	def positon(self, x, y):
		print(self.board[x][y].piece.color + ' ' + self.board[x][y].piece.name)
	
	def get_cell(self, x, y):
		return self.board[x][y]

board = Board()
board.print_board()

# Commands

