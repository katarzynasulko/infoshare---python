import csv


def add_gamer(gamers, gamer, identifier):
    gamers.append(
        {
            'ID': gamer['ID'],
            'name': gamer['name'],
            'score': gamer['score'],
            'age': gamer['age']
        }
    )


def import_from_csv(filename='players.csv', delimiter=','):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        gamers = []

        for line in reader:
            add_gamer(gamers, line, 'ID')

        return gamers, reader.fieldnames

gamers, headers = import_from_csv()
for gamer in gamers:
    print('Gamer:', gamer)

gamers_by_score = sorted(gamers, key=lambda gamer: int(gamer['score']), reverse=True)

print('Top 3 Gamers by score:', gamers_by_score[0], gamers_by_score[1], gamers_by_score[2])

#sorted_x = sorted(gamers, key=lambda x: x[2])
#for id in sorted_x:
#    print('Gamer:', gamers[id])