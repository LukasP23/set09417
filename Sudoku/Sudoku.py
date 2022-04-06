def main():
    menu = Menu()
    menu.display_option()
    
class Board:  
    def __init__(self):
        boards = Sudoku()
        self.print_board(boards.sudoku_board)
            
    def print_board(self, board):
        count = -1
        print(" -----------------------------")
        for i in board:
            string = " | %s | %s %s %s | %s %s %s | %s %s %s | " % (str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]), str(i[5]), str(i[6]), str(i[7]), str(i[8]), str(i[9]))
            print(string)
            count += 1
            if (count == 0 or count % 3 == 0):
                print(" -----------------------------")
                count = 0
class Sudoku:
    def __init__(self):
        self.sudoku_board = [[" ", "A","B","C","D","E","F","G","H","I"],
                            ["A", 5, 3, 0, 0, 7, 0, 0, 0, 0],
                            ["B", 6, 0, 0, 1, 9, 5, 0, 0, 0],
                            ["C", 0, 9, 8, 0, 0, 0, 0, 6, 0],
                            ["D", 8, 0, 0, 0, 6, 0, 0, 0, 3],
                            ["E", 4, 0, 0, 8, 0, 3, 0, 0, 1],
                            ["F", 7, 0, 0, 0, 2, 0, 0, 0, 6],
                            ["G", 0, 6, 0, 0, 0, 0, 2, 8, 0],
                            ["H", 0, 0, 0, 4, 1, 9, 0, 0, 5],
                            ["I", 0, 0, 0, 0, 8, 0, 0, 7, 9]]
        self.sudoku_board_start = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                                   [6, 0, 0, 1, 9, 5, 0, 0, 0],
                                   [0, 9, 8, 0, 0, 0, 0, 6, 0],
                                   [8, 0, 0, 0, 6, 0, 0, 0, 3],
                                   [4, 0, 0, 8, 0, 3, 0, 0, 1],
                                   [7, 0, 0, 0, 2, 0, 0, 0, 6],
                                   [0, 6, 0, 0, 0, 0, 2, 8, 0],
                                   [0, 0, 0, 4, 1, 9, 0, 0, 5],
                                   [0, 0, 0, 0, 8, 0, 0, 7, 9]]
                            
        self.sudoku_board_solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                      [7, 1, 3, 9, 2, 4, 8, 4, 6],
                                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]
                            
class Menu:
    def __init__(self):
        self.menu_options = {
            1: "Traditional Sudoku",
            2: "Option 2",
            3: "Option 3",
            4: "Exit",
        }
        print("\nWelcome to Sudoku!\n")
        
    def get_input(self):
        while(True):
            self.print_menu()
            option = ""
            try:
                option = int(input("\nPlease choose a gamemode: "))
                return option
                break
            except:
                print("\nInvalid input. Please enter a number that corresponds to a displayed option\n")
   
    def display_option(self):
        while(True):
            option = self.get_input()
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
                print("\nThanks for playing!")
                exit()
            else:
                print("\nInvalid input. Please enter a number that corresponds to a displayed option\n")
   
    def print_menu(self):
        for key in self.menu_options.keys():
            print (key, "-", self.menu_options[key] )

    def option1(self):
         board_9x9 = Board()

    def option2(self):
         print("\nOption 2")
         exit()

    def option3(self):
         print("\nOption 3")
         exit()
         
if __name__ == "__main__":
    main()