class Controler:
    def __init__(self):
        self.player = 1
        self.sign = 'X'

    def switch_player(self):
        self.player = 2 if self.player == 1 else 1
        self.sign = 'X' if self.player == 1 else 'O'

    def ask_player(self):
        answer = input(f"You are Player {self.player} with the sign of {'X' if self.player == 1 else 'O'}, "
                            f"which row and column? (2,3 means 2. row and 3. column): ")
        return answer.split(",")

    def check_winner(self, data):
        draw_list = sum(data, [])
        for i in range(3):
            if ''.join(data[i]) == "XXX":
                return 1
            elif ''.join(data[i]) == 'OOO':
                return 2

        if data[0][0] == 'X' and data[1][1] == 'X' and data[2][2] == 'X':
            return 1
        elif data[0][0] == 'O' and data[1][1] == 'O' and data[2][2] == 'O':
            return 2
        elif ' ' not in draw_list:
            return 3
        else:
            return 0
