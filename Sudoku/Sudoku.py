def main():
    menu = Menu()
    menu.display_option()
                  
class Boards:
    def __init__(self):
 #       self.sudoku_board = [[" ", "A","B","C","D","E","F","G","H","I"],
  #                          ["A", 5, 3, 0, 0, 7, 0, 0, 0, 0],
   #                         ["B", 6, 0, 0, 1, 9, 5, 0, 0, 0],
    #                        ["C", 0, 9, 8, 0, 0, 0, 0, 6, 0],
     #                       ["D", 8, 0, 0, 0, 6, 0, 0, 0, 3],
      #                      ["E", 4, 0, 0, 8, 0, 3, 0, 0, 1],
       #                     ["F", 7, 0, 0, 0, 2, 0, 0, 0, 6],
        #                    ["G", 0, 6, 0, 0, 0, 0, 2, 8, 0],
         #                   ["H", 0, 0, 0, 4, 1, 9, 0, 0, 5],
          #                  ["I", 0, 0, 0, 0, 8, 0, 0, 7, 9]]
        self.sudoku_board = [[" ", "A","B","C","D","E","F","G","H","I"],
                                      ["A", 5, 3, 0, 6, 7, 8, 9, 1, 2],
                                      ["B", 6, 7, 2, 1, 9, 5, 3, 4, 8],
                                      ["C", 1, 9, 8, 3, 4, 2, 5, 6, 7],
                                      ["D", 8, 5, 9, 7, 6, 1, 4, 2, 3],
                                      ["E", 4, 2, 6, 8, 5, 3, 7, 9, 1],
                                      ["F", 7, 1, 3, 9, 2, 4, 8, 4, 6],
                                      ["G", 9, 6, 1, 5, 3, 7, 2, 8, 4],
                                      ["H", 2, 8, 7, 4, 1, 9, 6, 3, 5],
                                      ["I", 3, 4, 5, 2, 8, 6, 1, 7, 9]]
                            
        self.sudoku_board_start = [[" ", "A","B","C","D","E","F","G","H","I"],
                                   ["A", 5, 3, 0, 0, 7, 0, 0, 0, 0],
                                   ["B", 6, 0, 0, 1, 9, 5, 0, 0, 0],
                                   ["C", 0, 9, 8, 0, 0, 0, 0, 6, 0],
                                   ["D", 8, 0, 0, 0, 6, 0, 0, 0, 3],
                                   ["E", 4, 0, 0, 8, 0, 3, 0, 0, 1],
                                   ["F", 7, 0, 0, 0, 2, 0, 0, 0, 6],
                                   ["G", 0, 6, 0, 0, 0, 0, 2, 8, 0],
                                   ["H", 0, 0, 0, 4, 1, 9, 0, 0, 5],
                                   ["I", 0, 0, 0, 0, 8, 0, 0, 7, 9]]
        self.sudoku_board_solution = [[" ", "A","B","C","D","E","F","G","H","I"],
                                      ["A", 5, 3, 4, 6, 7, 8, 9, 1, 2],
                                      ["B", 6, 7, 2, 1, 9, 5, 3, 4, 8],
                                      ["C", 1, 9, 8, 3, 4, 2, 5, 6, 7],
                                      ["D", 8, 5, 9, 7, 6, 1, 4, 2, 3],
                                      ["E", 4, 2, 6, 8, 5, 3, 7, 9, 1],
                                      ["F", 7, 1, 3, 9, 2, 4, 8, 4, 6],
                                      ["G", 9, 6, 1, 5, 3, 7, 2, 8, 4],
                                      ["H", 2, 8, 7, 4, 1, 9, 6, 3, 5],
                                      ["I", 3, 4, 5, 2, 8, 6, 1, 7, 9]]
                            
class Menu:
    def __init__(self):
        self.previous_games = {}
        self.menu_options = {
            1: "Traditional Sudoku",
            2: "Instructions",
            3: "Replay",
            4: "Exit",
        }
        input("\n Welcome to Sudoku! (Hit any key to continue)")
        
    def get_input(self, menu):
        while(True):
            if (menu == "home"):
                self.print_menu()
            elif (menu == "replay"):
                self.print_replay_menu()
            option = ""
            try:
                option = int(input("\n Please choose an option: "))
                return option
                break
            except:
                input("\n Invalid input - Please enter a number that corresponds to a displayed option!")
   
    def display_option(self):
        while(True):
            option = self.get_input("home")
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
                input("\n Thanks for playing!")
                exit()
            else:
                input("\n Invalid input - Please enter a number that corresponds to a displayed option!")
   
    def print_menu(self):
        print("\n Home Menu:")
        for key in self.menu_options.keys():
            print ("", key, "-", self.menu_options[key] )

    def print_replay_menu(self):
        print("\n Previous Games:")
        self.i = 1
        for key in self.previous_games.keys():
            print ("", self.i,"-", key)
            self.i += 1
        print (" " + str(self.i) +" - Exit to menu")
        
    def option1(self):
        current_game = Game()
        game_moves = Game().new_game()
        if (game_moves != "exit"):
            self.previous_games[game_moves[0]] = game_moves[1]
        print(self.previous_games)
        self.display_option()
         
    def option2(self):
        input(" Intructions:\n 1. Normal Sudoku Rules apply - these can be found online.\n 2. The Sudoku board will be displayed with a letter corresponding to each row and column. To enter a value in the board you will be asked to enter the letter that corresponds to the row and then the column of the square you wish to select. You will then be asked for the value you wish to enter in that square.\n 3. You cannot enter a value in a square that is populated at the beginning of the game.\n 4. Once you think you have finished you can use the game menu to submit your board to be checked.")
        self.display_option()
         
    def option3(self):
        while(True):
            replay = self.get_input("replay")
            if (replay == self.i):
                self.display_option()
            elif (replay >= 1 and replay <= (len(self.previous_games)+1)):
                print("Test Success")
            else:
                input("\n Invalid input - Please enter a number that corresponds to a displayed option!")
            
class Game:
    def new_game(self):
        boards = Boards()
        self.game_board = boards.sudoku_board
        self.start_board = boards.sudoku_board_start
        self.solution_board = boards.sudoku_board_solution
        self.menu = Game_Menu()
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
        while True:
            self.print_board(self.game_board)
            choice = self.menu.get_input()
            if(choice == 1):
                self.game_input()
                self.insert_value()
            elif(choice == 2):
                self.undo()
            elif(choice == 3):
                self.redo()
            elif(choice == 4):
                if(self.submit_board()):
                    self.game_name = input("\n Correct - Well Done! Enter a name to save with this game so you can play it back later: ")
                    return [self.game_name, self.moves]
                    #break
                else:
                    input("\n Not quite - keep trying!")
            elif(choice == 5):
                return "exit"
                #break
            else:
                input("\n Invalid input - Please enter a number that corresponds to a displayed option!")
    
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
                   
class Game_Menu:
    def __init__(self):
        self.menu_options = {
            1: "Enter value",
            2: "Undo move",
            3: "Redo move",
            4: "Submit board",
            5: "Exit to menu"
        }
        
    def get_input(self):
        while(True):
            self.print_menu()
            option = ""
            try:
                option = int(input("\n Please choose an option: "))
                return option
                break
            except:
                input("\n Invalid input - Please enter a number that corresponds to a displayed option!")
   
    def print_menu(self):
        print("\n Game Menu:")
        for key in self.menu_options.keys():
            print ("", key, "-", self.menu_options[key] )
     
if __name__ == "__main__":
    main()