from turtle import *
from tkinter import * 
from tkinter import messagebox

def main():
    menu = Menu()
    menu.display_option()
    done()
    
class Board:  
    def __init__(self, size):
        game = Sudoku()
        self.board = game.sudoku_board
        self.start_board = game.sudoku_board_start
        self.size = size
        hideturtle()
        Screen().tracer(0,0)
        self.grid()
        update()
        Screen().onscreenclick(self.tap)
        
    def grid(self):
        clear()
        if (self.size == 700):    
            setup(700, 700)
            color("black")
            self.grid_9x9()
            color("blue")
            self.display_game_values(self.board)
            color("black")
            self.display_game_values(self.start_board)
               
    def grid_9x9(self):
        #Main board
        self.line(-105, 315, -105, -315, 2, "black")
        self.line(105, 315, 105, -315, 2, "black")
        self.line(315, -105, -315, -105, 2, "black")
        self.line(315, 105, -315, 105, 2, "black")      
        self.line(315, 315, -315, 315, 3, "black")
        self.line(315, -315, -315, -315, 3, "black")
        self.line(-315, -315, -315, 315, 3, "black")
        self.line(315, -315, 315, 315, 3, "black")
        #Top left
        self.line(-245, 315, -245, 105, 1, "black")
        self.line(-175, 315, -175, 105, 1, "black")
        self.line(-315, 245, -105, 245, 1, "black")
        self.line(-315, 175, -105, 175, 1, "black")  
        #Top right
        self.line(245, 315, 245, 105, 1, "black")
        self.line(175, 315, 175, 105, 1, "black")
        self.line(315, 245, 105, 245, 1, "black")
        self.line(315, 175, 105, 175, 1, "black")
        #Top middle
        self.line(-35, 315, -35, 105, 1, "black")
        self.line(35, 315, 35, 105, 1, "black")
        self.line(-105, 245, 105, 245, 1, "black")
        self.line(-105, 175, 105, 175, 1,"black") 
        #Middle left
        self.line(-245, 105, -245, -105, 1, "black")
        self.line(-175, 105, -175, -105, 1, "black")
        self.line(-315, 35, -105, 35, 1, "black")
        self.line(-315, -35, -105, -35, 1, "black")
        #Middle right
        self.line(245, 105, 245, -105, 1, "black")
        self.line(175, 105, 175, -105, 1, "black")
        self.line(315, 35, 105, 35, 1, "black")
        self.line(315, -35, 105, -35, 1, "black")     
        #Middle
        self.line(-35, 105, -35, -105, 1, "black")
        self.line(35, 105, 35, -105, 1, "black")
        self.line(-105, 35, 105, 35, 1, "black")
        self.line(-105, -35, 105, -35, 1, "black")
        #Bottom left
        self.line(-245, -315, -245, -105, 1, "black")
        self.line(-175, -315, -175, -105, 1, "black")
        self.line(-315, -245, -105, -245, 1, "black")
        self.line(-315, -175, -105, -175, 1, "black")
        #Bottom right
        self.line(245, -315, 245, -105, 1, "black")
        self.line(175, -315, 175, -105, 1, "black")
        self.line(315, -245, 105, -245, 1, "black")
        self.line(315, -175, 105, -175, 1, "black")
        #Bottom middle
        self.line(-35, -315, -35, -105, 1, "black")
        self.line(35, -315, 35, -105, 1, "black")
        self.line(-105, -245, 105, -245, 1, "black")
        self.line(-105, -175, 105, -175, 1, "black") 
    
    def line(self, a, b, x, y, size, colour):
        pencolor(colour)
        pensize(size)
        up()
        goto(a, b)
        down()
        goto(x, y)
        
    def highlight(self, x, y, square):
        if(x > -316 and x < 315 and y > -316 and y < 315 and self.start_board[square[1]][square[0]] == 0):
            self.grid()
            self.line(x, y, x, y + 70, 4, "green")
            self.line(x + 70, y, x + 70, y + 70, 4, "green")
            self.line(x + 70, y + 70, x, y + 70, 4, "green")
            self.line(x, y, x + 70, y, 4, "green")
            self.line(x, y, x + 70, y, 4, "green")
    
    def floor(self, value):
        "Round value down to grid with square size 133."
        return ((value + 175) // 70) * 70 - 175
        
    def tap(self, x, y):
        x = self.floor(x)
        y = self.floor(y)
        square = self.identify_square(x, y)
        self.highlight(x, y, square)
        self.enter_value(square, x, y)
        update()
        
    def display_game_values(self, board):
        y = 255
        for row in board:
            x = -280
            for value in row:
                penup()
                if (value != 0):
                    goto(x, y)
                    write((str(value)), align = "center", font=("Arial", 30, "normal"))
                x += 70
            y -= 70
        
    def identify_square(self, x, y):
        check_y = 245
        for z in range(9):
            check_x = -315
            for i in range(9):
                if (x == check_x and y == check_y):
                    square = [i,z]
                    return(square)
                    break
                check_x += 70
            check_y -= 70
        
    def enter_value(self, square, x, y):
        if (square is not None and self.start_board[square[1]][square[0]] == 0):
            value = textinput("Sudoku", "Enter Value")
            if (value is not None):
                try:
                    value = int(value)
                    if (int(value) > 0 and int(value) < 10):
                        self.board[square[1]][square[0]] = value
                        self.grid()
                        self.highlight(x, y, square)
                    else:
                        messagebox.showinfo("Error", "Invalid entry - please enter a number between 1 and 9")
                except ValueError:
                    messagebox.showinfo("Error", "Invalid entry - please enter a number between 1 and 9")
        
class Sudoku:
    def __init__(self):
        self.sudoku_board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                            [6, 0, 0, 1, 9, 5, 0, 0, 0],
                            [0, 9, 8, 0, 0, 0, 0, 6, 0],
                            [8, 0, 0, 0, 6, 0, 0, 0, 3],
                            [4, 0, 0, 8, 0, 3, 0, 0, 1],
                            [7, 0, 0, 0, 2, 0, 0, 0, 6],
                            [0, 6, 0, 0, 0, 0, 2, 8, 0],
                            [0, 0, 0, 4, 1, 9, 0, 0, 5],
                            [0, 0, 0, 0, 8, 0, 0, 7, 9]]
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
        #self.welcome_screen()
        self.menu_options = {
            1: "Traditional Sudoku",
            2: "Option 2",
            3: "Option 3",
            4: "Exit",
        }
        print("\nWelcome to Sudoku!\n")

    def welcome_screen(self):
        Screen().setup(900, 400)
        title("Sudoku")
        penup()
        Screen().tracer(1, 100)
        hideturtle()
        x = -100
        for letter in "Sudoku":
            goto(x,0)
            color("red")
            write(letter, align = "center", font=("Arial", 50, "bold"))
            x +=40
        goto(0,-50)
        color("black")
        write("Choose a gamemode using the command prompt menu to begin", align = "center", font=("Arial", 15, "normal"))
    
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
         board_9x9 = Board(700)

    def option2(self):
         print("\nOption 2")
         exit()

    def option3(self):
         print("\nOption 3")
         exit()
         
if __name__ == "__main__":
    main()