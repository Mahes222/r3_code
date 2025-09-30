from boardf import board

class game:
    def __init__(self,size):
        self.board = board(size)
        # print(self.board.grid)
        self.board.printgrind()
    
    def round(self):

        while(True):
            self.column = int(input("enter the column :"))
            self.color = input("enter the color :")
            if self.board.fillcolor(self.column,self.color):
                self.board.printgrind()
                # option  = input("do you want to continue y/n")
                # if option == "y":
                #     continue
                # else:
                #     print("game over!!!")
                #     break

            else:
                print("column filled :")
                break