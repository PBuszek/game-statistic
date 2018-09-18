def count_games(file_name):
    global count
    count = len(open(file_name).readlines())
    return (count)

def decide(file_name, year):
    with open(file_name) as file:
        for line in file.readlines():
            line=line.split("\t")
            line[4]=line[4][:-1]
            choice = str(year)
            if choice in line:
                return True

# I DONT UNDERSTAND THAT FUNCTION!!!!!!
def get_latest(file_name):
    with open(file_name) as file:
        latest_game = (max(file, key=lambda line:int(line.split("\t")[2])).split("\t"))
        return latest_game[0]

def count_by_genre(file_name, genre):
    genre_list = []
    with open(file_name) as file:
        for line in file.readlines():
            line=line.split("\t")
            line[4]=line[4][:-1]
            if genre in line:
                genre_list.append(genre)
        games_by_genre = len(genre_list)
        return games_by_genre

#I DONT UNDERSTAND WELL "ENUMERATE"!!!!!!
def get_line_number_by_title(file_name, title):
     with open(file_name) as f:
        for i, line in enumerate(f, 1):
            if title in line:
                return i
