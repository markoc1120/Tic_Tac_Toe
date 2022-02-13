from map import Map
from controler import Controler


game_running = True
game_map = Map()
game = Controler()
game_map.initialize(game.player)


while game_running:
    winner = game.check_winner(game_map.places)
    if winner == 0:
        answer = game.ask_player()
        while game_map.used_place(answer):
            print('That place already reserved, please try another one!')
            answer = game.ask_player()
        game_map.update_layout(answer, game.player)
        game.switch_player()
    elif winner == 3:
        print("That's a draw! 🚧")
        game_running = False
    else:
        print(f"Nice job Player {winner} you won! 🎇")
        game_running = False
