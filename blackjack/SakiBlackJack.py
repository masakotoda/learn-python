import Game
import Person

if __name__ == '__main__':
    player = Person.Player(500)
    game = Game.Game(player)
    game.play()
    pass