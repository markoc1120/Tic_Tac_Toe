class Map:
    def __init__(self):
        self.places = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.signs = ['X', 'O']

    def initialize(self, player):
        self.places = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.draw_map(player)

    def draw_map(self, player):
        print('Tic Tac Toe Game')
        for i in range(3):
            print(f" {self.places[i][0] if self.places[i][0] == ' ' or type(self.places[i][0]) == str else self.signs[player - 1]} | "
                  f"{self.places[i][1] if self.places[i][1] == ' ' or type(self.places[i][1]) == str else self.signs[player - 1]} | "
                  f"{self.places[i][2] if self.places[i][2] == ' ' or type(self.places[i][2]) == str else self.signs[player - 1]}")
            if i < 2:
                print("------------")

    def used_place(self, pos):
        if self.places[int(pos[0]) - 1][int(pos[1]) - 1] != ' ':
            return True

    def update_layout(self, pos, player):
        print("\n" * 50)
        self.places[int(pos[0]) - 1][int(pos[1]) - 1] = self.signs[player - 1]
        self.draw_map(player)
