from game_round import game
try:
    size = int(input("Enter the size of the Box : ")) 
    print("Enter the size of the Box : ")
    print("Enter the size of the Box : ")
    games = game(size)
    games.round()
    print("Enter the size of the Box : ")
except ValueError:
    print("Enter the valid size : ")
