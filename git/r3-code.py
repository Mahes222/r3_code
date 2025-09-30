class board:

    def __init__(self,size):
        self.size = size
        self.grid = [['- ' for i in range(size)] for _ in range(size)]
        self.position = [size-1] * size


    def printgrind(self):
        self.str = ""
        for i in range (self.size):
            for j in range (self.size):
                self.str+=((self.grid[i][j]))
            print(self.str)
            self.str=""


    def fillcolor(self,column,color):
        for i in range (len(color)):
            row = (self.position[column-1] )
            if (row >= 0):
                self.grid[row][column-1] = color[i]+" "
                self.left(row,column-1)
                self.right(row,column-1)
                self.center(row,column-1)
                self.bottom(row,column-1)
                self.lefttop(row,column-1)
                self.leftbottom(row,column-1)

                self.position[column-1] -= 1
                if (column == self.size):
                    column = 1
                else:
                    column += 1
            else:
                return False
            # self.check_all()
        return True


    def left(self,row,column):
        if(column > 1 ):
            if(self.grid[row][column]==self.grid[row][column-1] and self.grid[row][column]==self.grid[row][column-2]):
                self.grid[row][column]="- "
                self.grid[row][column-1]="- "
                self.getdown(row,column-1)
                self.grid[row][column-2]="- "
                self.getdown(row,column-2)
                self.position[column] += 1
                self.position[column-1] += 1
                self.position[column-2] += 1


    def right(self,row,column):
        if(column < self.size-2 ):
            if(self.grid[row][column]==self.grid[row][column+1] and self.grid[row][column]==self.grid[row][column+2]):
                self.grid[row][column]="- "
                self.grid[row][column+1]="- "
                self.getdown(row,column+1)
                self.grid[row][column+2]="- "
                self.getdown(row,column+2)
                self.position[column] += 1
                self.position[column+1] += 1
                self.position[column+2] += 1


    def center(self,row,column):
        if(column < self.size-1 and  column > 0):
            if(self.grid[row][column]==self.grid[row][column+1] and self.grid[row][column]==self.grid[row][column-1]):
                self.grid[row][column]="- "
                self.grid[row][column+1]="- "
                self.getdown(row,column+1)
                self.grid[row][column-1]="- "
                self.getdown(row,column-1)
                self.position[column] += 1
                self.position[column+1] += 1
                self.position[column-1] += 1


    def bottom(self,row,column):
        if(row < self.size-2 ):
            if(self.grid[row][column]==self.grid[row+1][column] and self.grid[row][column]==self.grid[row+2][column]):
                self.grid[row][column]="- "
                self.grid[row+1][column]="- "
                self.grid[row+2][column]="- "
                self.position[column] += 1
                self.position[column] += 1
                self.position[column] += 1


    def lefttop(self,row,column):
        if(column > 1 and row > 1):
            if(self.grid[row][column]==self.grid[row-1][column-1] and self.grid[row][column]==self.grid[row-2][column-2]):
                self.grid[row][column]="- "
                self.grid[row-1][column-1]="- "
                self.getdown(row-1,column-1)
                self.grid[row-2][column-2]="- "
                self.getdown(row-2,column-2)
                self.position[column] += 1
                self.position[column-1] += 1
                self.position[column-2] += 1


    def leftbottom(self,row,column):
        if(column > 1 and row < self.size-2):
            if(self.grid[row][column]==self.grid[row+1][column-1] and self.grid[row][column]==self.grid[row+2][column-2]):
                self.grid[row][column]="- "
                self.grid[row+1][column-1]="- "
                self.getdown(row+1,column-1)
                self.grid[row+2][column-2]="- "
                self.getdown(row+2,column-2)
                self.position[column] += 1
                self.position[column-1] += 1
                self.position[column-2] += 1    
    
    
    def getdown(self,row,column):
        rows = row
        while True : 
            if(row > 0):
                if (self.grid[row-1][column] != "- "):
                    self.grid[row][column] = self.grid[row-1][column]
                    self.grid[row-1][column] = "- "
                    # self.left(row, column)
                    # self.right(row, column)
                    # self.center(row, column)
                    # self.bottom(row, column)
                    # self.lefttop(row, column)
                    # self.leftbottom(row, column)
                    row -= 1
            else:
                break


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
try:
    size = int(input("Enter the size of the Box : ")) 
    games = game(size)
    games.round()
except ValueError:
    print("Enter the valid size : ")