from player import Player
from game import Game

# Main function to start the game.

def main():
    name = input("Type your astronaut name: ")
    player = Player(name)
    game = Game(player)
    game.start_adventure()

if __name__ == "__main__":
    main()