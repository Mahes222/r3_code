from game_round import game
try:
    size = int(input("Enter the size of the Box u want : ")) 
    games = game(size)
    games.round()
except ValueError:
    print("Enter the valid size : ")
