import csv

class Player:
    def __init__(self, ID, name, score, age):
        self.ID = ID
        self.name = name
        self.score = score
        self.age = age

    def __str__(self):
        return f'{self.ID}, {self.name}, {self.score}, {self.age}'



class PlayerList:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_all(self):
        for gamer in self.players:
            print(gamer)

    def sort(self, reverse=False):
        self.players.sort(key=lambda player: player.score, reverse=True)

    def from_csv(self, filename, delimiter=','):
        with open(filename, 'r') as players_file:
            reader = csv.DictReader(players_file, delimiter=delimiter)
            for player_data in reader:
                gamer = Player(
                    player_data['ID'],
                    player_data['name'],
                    player_data['score'],
                    player_data['age']
                )
                self.add_player(gamer)


if __name__ == '__main__':


    lista_graczy = PlayerList()
    lista_graczy.from_csv('players.csv')
    lista_graczy.display_all()

    print('TOP 10 po sortowaniu')
    lista_graczy.sort()
    lista_graczy.display_all()
    top_10 = print(lista_graczy[0])
