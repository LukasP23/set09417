import copy
import random
import time

def main():
    input("\n Welcome to Sudoku! (Hit any key to continue)")
    menu = Menu()
    menu.display_option()
 
class Board:
    def __init__(self, difficulty):
        self.clear_board()
        self.sudoku_board, self.sudoku_board_solution = self.generate_game_board(self.generate_complete_board(), difficulty)
        self.format_board(self.sudoku_board)
        self.format_board(self.sudoku_board_solution) 
                      
    def find_spaces(self): 
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if self.board[row][column] == 0:
                    return (row, column)
        return False

    def check_space(self, value, space): 
        if not self.board[space[0]][space[1]] == 0: 
            return False
        for column in self.board[space[0]]: 
            if column == value:
                return False
        for row in range(len(self.board)): 
            if self.board[row][space[1]] == value:
                return False
        internal_box_row = space[0] // 3
        internal_box_column = space[1] // 3
        for i in range(3): 
            for j in range(3):
                if self.board[i + (internal_box_row * 3)][j + (internal_box_column * 3)] == value:
                    return False
        return True

    def solve_board(self): 
        spaces = self.find_spaces()
        if not spaces:
            return True
        else:
            row, column = spaces
        for n in range(1, 10):
            if self.check_space(n, (row, column)):
                self.board[row][column] = n	
                if self.solve_board():
                    return self.board
                self.board[row][column] = 0
        return False

    def generate_game_board(self, full_board, difficulty): 
            self.board = copy.deepcopy(full_board)
            if difficulty == 0:
                squares_to_remove = 24
            elif difficulty == 1:
                squares_to_remove = 36
            elif difficulty == 2:
                squares_to_remove = 48
            else:
                return
            counter = 0
            while counter < 4:
                r_row = random.randint(0, 2)
                r_column = random.randint(0, 2)
                if self.board[r_row][r_column] != 0:
                    self.board[r_row][r_column] = 0
                    counter += 1
            counter = 0
            while counter < 4:
                r_row = random.randint(3, 5)
                r_column = random.randint(3, 5)
                if self.board[r_row][r_column] != 0:
                    self.board[r_row][r_column] = 0
                    counter += 1
            counter = 0
            while counter < 4:
                r_row = random.randint(6, 8)
                r_column = random.randint(6, 8)
                if self.board[r_row][r_column] != 0:
                    self.board[r_row][r_column] = 0
                    counter += 1
            squares_to_remove -= 12
            counter = 0
            while counter < squares_to_remove:
                row = random.randint(0, 8)
                column = random.randint(0, 8)
                if self.board[row][column] != 0:
                    n = self.board[row][column]
                    self.board[row][column] = 0
                    if len(self.find_solutions()) != 1:
                        self.board[row][column] = n
                        continue
                    counter += 1
            return self.board, full_board

    def generate_complete_board(self): 
            self.clear_board()
            l = list(range(1, 10))
            for row in range(3):
                for column in range(3):
                    value = random.choice(l)
                    self.board[row][column] = value
                    l.remove(value)
            l = list(range(1, 10))
            for row in range(3, 6):
                for column in range(3, 6):
                    value = random.choice(l)
                    self.board[row][column] = value
                    l.remove(value)
            l = list(range(1, 10))
            for row in range(6, 9):
                for column in range(6, 9):
                    value = random.choice(l)
                    self.board[row][column] = value
                    l.remove(value)
            return self.generate_random_board()

    def generate_random_board(self): 
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.board[row][column] == 0:
                    value = random.randint(1, 9)
                    if self.check_space(value, (row, column)):
                        self.board[row][column] = value
                        if self.solve_board():
                            self.generate_random_board()
                            return self.board
                        self.board[row][column] = 0
        return False

    def find_solutions(self): 
            z = 0
            list_of_solutions = []
            for row in range(len(self.board)):
                for column in range(len(self.board[row])):
                    if self.board[row][column] == 0:
                        z += 1
            for i in range(1, z+1):
                board_copy = copy.deepcopy(self)
                row, column = self.find_spaces_for_solutions(board_copy.board, i)
                board_copy_solution = "".join([str(i) for j in (board_copy.solve_for_solutions(row, column)) for i in j])
                list_of_solutions.append(board_copy_solution)
            return list(set(list_of_solutions))

    def find_spaces_for_solutions(self, board, h): 
        k = 1
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == 0:
                    if k == h:
                        return (row, column)
                    k += 1
        return False

    def solve_for_solutions(self, row, column): 
        for n in range(1, 10):
            if self.check_space(n, (row, column)):
                self.board[row][column] = n
                if self.solve_board():
                    return self.board
                self.board[row][column] = 0
        return False

    def clear_board(self): 
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        return self.board

    def format_board(self, board):
        board.insert(0,[" ", "A","B","C","D","E","F","G","H","I"])
        board[1].insert(0, "A")
        board[2].insert(0, "B")
        board[3].insert(0, "C")
        board[4].insert(0, "D")
        board[5].insert(0, "E")
        board[6].insert(0, "F")
        board[7].insert(0, "G")
        board[8].insert(0, "H")
        board[9].insert(0, "I")         
        
class Menu:
    def __init__(self):
        self.previous_games = {}
        self.previous_boards = {}
        self.previous_solutions = {}
        self.time_leaderboard = {}
        self.main_menu_options = {
            1: "Play Sudoku",
            2: "Instructions",
            3: "Replay",
            4: "Time leaderboard",
            5: "Exit",
        }
        self.game_menu_options = {
            1: "Enter value",
            2: "Undo move",
            3: "Redo move",
            4: "Reveal a value",
            5: "Submit board",
            6: "Give up and reveal solution"
        }
        self.difficulty_menu_options = {
            1: "Easy",
            2: "Medium",
            3: "Hard"
        }
        self.game_mode_menu_options = {
            1: "Traditional",
            2: "Five Lives",
            3: "Timed"
        }
         
    def get_input(self, menu):
        while(True):
            self.print_menu(menu)
            option = ""
            try:
                option = int(input("\n Please choose an option: "))
                return option
            except:
                input("\n Invalid input - Please enter a number that corresponds to a displayed option!")
   
    def display_option(self):
        while(True):
            option = self.get_input(self.main_menu_options)
            if option == 1:
                self.option1()
                break
            elif option == 2:
                self.option2()
                break
            elif option == 3:
                self.option3()
                break
            elif option == 4:
                self.option4()
                break
            elif option == 5:
                input("\n Thanks for playing!")
                exit()
            else:
                input("\n Invalid input - Please enter a number that corresponds to a displayed option!")
   
    def print_menu(self, menu):
        if (menu == self.main_menu_options):
            print("\n Home Menu:")
        elif (menu == self.game_menu_options):
            print("\n Game Menu:")
        elif (menu == self.difficulty_menu_options):
            print("\n Choose a difficulty:")
        elif (menu == self.game_mode_menu_options):
            print("\n Choose a game mode:")
        for key in menu.keys():
            print ("", key, "-", menu[key] )

    def print_replay_menu(self):
        print("\n Previous Games:")
        for key in self.previous_games.keys():
            print (" -", key)
     
    def get_replay_input(self):
        self.print_replay_menu()
        while True:
            game_key = input("\n Enter the name of the game you would like to replay or 'menu' to return to the main menu: ")
            if(game_key == "menu" or game_key in self.previous_games):
                return game_key
            else:
                input("\n Invalid input - Please enter the name of the game you would like to replay or 'menu' to return to the main menu!")
        
    def get_difficulty(self):
        while True:
            difficulty = self.get_input(self.difficulty_menu_options)
            if difficulty >= 1 and difficulty <= len(self.difficulty_menu_options):
                return difficulty
            else:
                input("\n Invalid input - Please enter a number that corresponds to a displayed option!")
    
    def get_game_mode(self):
        while True:
            mode = self.get_input(self.game_mode_menu_options)
            if mode == 1:
                return "traditional"
            if mode == 2:
                return "lives"
            if mode == 3:
                return "timer"
            else:
                input("\n Invalid input - Please enter a number that corresponds to a displayed option!")
          
    def option1(self):
        game_mode = self.get_game_mode()
        difficulty = (self.get_difficulty()) - 1
        current_game = Game()
        game_moves = current_game.new_game(difficulty, game_mode)
        self.previous_games[game_moves[0]] = game_moves[1]
        self.previous_boards[game_moves[0]] = game_moves[2]
        self.previous_solutions[game_moves[0]] = game_moves[3]
        if(game_mode == "timer"):
            self.time_leaderboard[game_moves[0]] = game_moves[4]
        self.display_option()
         
    def option2(self):
        input(" Intructions:\n 1. Normal Sudoku Rules apply - these can be found online.\n 2. The Sudoku board will be displayed with a letter corresponding to each row and column. To enter a value in the board you will be asked to enter the letter that corresponds to the row and then the column of the square you wish to select. You will then be asked for the value you wish to enter in that square.\n 3. You cannot enter a value in a square that is populated at the beginning of the game.\n 4. Once you think you have finished you can use the game menu to submit your board to be checked.")
        self.display_option()
         
    def option3(self):
        if (len(self.previous_games) == 0):
            input("\n You do not have any completed games to replay!")
        else:
            while(True):
                game_key = self.get_replay_input()
                if (game_key == "menu"):
                    break
                else:
                    replay_game = Game()
                    self.initial_board = copy.deepcopy(self.previous_boards[game_key])
                    replay_game.replay(self.previous_games[game_key], self.previous_boards[game_key], self.previous_solutions[game_key])
                    self.previous_boards[game_key] = copy.deepcopy(self.initial_board)
        self.display_option()  
        
    def option4(self):
        if(len(self.time_leaderboard) == 0):
            input("\n Leaderboard is empty!")
        else:
            print("\n Leaderboard:")
            sort_list = sorted(self.time_leaderboard.items(), key=lambda x:x[1])
            leaderboard = dict(sort_list)
            self.print_menu(leaderboard)
            input("\n Hit any key to return to the main menu")
        self.display_option() 
    
class Game:
    def new_game(self, difficulty, game_mode):
        boards = Board(difficulty)
        self.game_board = boards.sudoku_board
        self.start_board = copy.deepcopy(self.game_board)
        self.solution_board = boards.sudoku_board_solution
        self.menu = Menu()
        self.undo_stack = []
        self.redo_stack = []
        self.moves = []
        self.game_name = ""
        self.value = 0
        self.old_value = 0
        self.input_row = ""
        self.input_column = ""
        self.row = 0
        self.column = 0
        lives = 5
        if (game_mode == "timer"):
            t0 = time.time()
            print ("\n The time is on!")
        while True:
            self.print_board(self.game_board)
            if (game_mode == "lives"):
                print("\n Lives: "+str(lives))
            choice = self.menu.get_input(self.menu.game_menu_options)
            if(choice == 1):
                self.game_input()
                if(game_mode == "lives"):
                    if self.check_move() is True:
                        self.insert_value()
                        print("\n Correct!")
                    else:
                        print("\n Incorrect! you lost a life!")
                        lives -= 1
                        if(lives == 0):
                            self.print_board(self.solution_board)
                            self.game_name = input("\n You ran out of lives! Enter a name to save with this game so you can play it back later: ")
                            while (self.game_name == ""):
                                self.game_name = input("\n Game name cannot be empty, please try again: ")
                            return [self.game_name, self.moves, self.start_board, self.solution_board]
                elif(game_mode == "traditional"):    
                    self.insert_value()
            elif(choice == 2):
                self.undo()
            elif(choice == 3):
                self.redo()
            elif(choice == 4):
                self.hint()
            elif(choice == 5):
                if(self.submit_board()):
                    if (game_mode == "timer"):
                        t1 = time.time()
                        final_time = t1-t0
                    self.game_name = input("\n Correct - Well Done! Enter a name to save with this game so you can play it back later: ")
                    while (self.game_name == ""):
                        self.game_name = input("\n Game name cannot be empty, please try again: ")
                    if (game_mode == "timer"): 
                        input("\n Final time: "+str(round(final_time, 2))+"seconds")
                        return [self.game_name, self.moves, self.start_board, self.solution_board, final_time]
                    else:
                        return [self.game_name, self.moves, self.start_board, self.solution_board]
                else:
                    input("\n Not quite - keep trying!")
            elif(choice == 6):
                if (game_mode == "timer"):
                    t1 = time.time()
                    final_time = t1-t0
                self.print_board(self.solution_board)
                self.game_name = input("\n Solution revealed, you'll get it next time! Enter a name to save with this game so you can play it back later: ")
                while (self.game_name == ""):
                    self.game_name = input("\n Game name cannot be empty, please try again: ")
                if (game_mode == "timer"): 
                    input("\n Final time: "+str(round(final_time, 2))+"seconds")
                    return [self.game_name, self.moves, self.start_board, self.solution_board, final_time]
                else:
                    return [self.game_name, self.moves, self.start_board, self.solution_board]
         
    def print_board(self, board):
        count = -1
        print("\n -----------------------------")
        for i in board:
            string = " | %s | %s %s %s | %s %s %s | %s %s %s | " % (str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]), str(i[5]), str(i[6]), str(i[7]), str(i[8]), str(i[9]))
            print(string)
            count += 1
            if (count == 0 or count % 3 == 0):
                print(" -----------------------------")
                count = 0
                
    def game_input(self):
        while True:
            self.input_row = input("\n Enter row: ").upper()
            self.row = self.convert_value(self.input_row)
            if(self.row != 0):
                break
            input("\n Invalid input - Please enter a letter than corresponds to a row on the board!")
        while True:
            self.input_column = input("\n Enter column: ").upper()
            self.column = self.convert_value(self.input_column)      
            if(self.column != 0):
                break            
            input("\n Invalid input - Please enter a letter than corresponds to a column on the board!")
        while True:
            try:
                self.value = int(input("\n Enter value: "))
                if(self.value < 10 and self.value > 0):
                    break
                else: 
                    input("\n Invalid input - Please enter a number from 1 to 9!")
            except:
                input("\n Invalid input - Please enter a number from 1 to 9!")
        
    def convert_value(self, value):
        output = 0
        if (value == "A"):
            output = 1
        elif (value == "B"):
            output = 2   
        elif (value == "C"):
            output = 3 
        elif (value == "D"):
            output = 4 
        elif (value == "E"):
            output = 5 
        elif (value == "F"):
            output = 6 
        elif (value == "G"):
            output = 7 
        elif (value == "H"):
            output = 8 
        elif (value == "I"):
            output = 9        
        return output
            
    def insert_value(self):
        if (self.start_board[self.row][self.column] == 0):
            self.old_value = self.game_board[self.row][self.column]
            self.game_board[self.row][self.column] = self.value
            self.undo_stack.append([self.row, self.column, self.value, self.old_value])
            self.redo_stack = []
            self.moves.append([self.row, self.column, self.value])
        else:
            input("\n This is a set value - try again!")   
            
    def check_move(self):
        if(self.value == self.solution_board[self.row][self.column]):
            return True
        else:
            return False
    
    def submit_board(self):
        if(self.game_board == self.solution_board):
            return True
        else:
            return False
   
    def undo(self):
        if (len(self.undo_stack) == 0 ):
            input("\n There are no moves to undo!")
        else:
            last_move = self.undo_stack.pop()
            undo_row = int(last_move[0])
            undo_column = int(last_move[1])
            undo_value = int(last_move[3])
            self.game_board[undo_row][undo_column] = undo_value
            self.moves.append([undo_row, undo_column, undo_value])
            self.redo_stack.append(last_move)
            print("\n Move undone!")
            
    def redo(self):
        if (len(self.redo_stack) == 0 ):
            input("\n There are no moves to redo!")
        else:
            last_undo = self.redo_stack.pop()
            redo_row = int(last_undo[0])
            redo_column = int(last_undo[1])
            redo_value = int(last_undo[2])
            self.game_board[redo_row][redo_column] = redo_value
            self.undo_stack.append(last_undo)
            self.moves.append([redo_row, redo_column, redo_value])
            print("\n Move redone!")
                   
    def replay(self, moves, board, solution_board):
        print("\n Press any key to cycle through each move of the replay!")
        print(" Start board:")
        self.print_board(board)
        i = 1
        for move in moves:
            board[move[0]][move[1]] = move[2]
            input("")
            print(" Move "+str(i)+":")
            self.print_board(board)
            i += 1   
        print("\n Final board:")
        self.print_board(solution_board)
     
    def hint(self):
        if self.get_first_zero() is False:
            print("\n There are no 0 values left on the board!")
        else:    
            row, column = self.get_first_zero()
            value = self.solution_board[row][column]
            self.undo_stack.append([row, column, value, self.game_board[row][column]])
            self.game_board[row][column] = value
            self.moves.append([row, column, value])
            print("\n Value revealed!")
        
    def get_first_zero(self):
        for row in self.game_board:
            for value in row:
                if value == 0:
                    return self.game_board.index(row), row.index(value)
        return False
        
if __name__ == "__main__":
    main()