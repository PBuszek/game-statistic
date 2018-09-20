# I DON'T UNDERSTAND THAT FUNCTION!!!!!
def get_most_played(file_name):
    with open(file_name) as file:
        most_played = (max(file, key=lambda line:float(line.split('\t')[1])).split('\t'))
        return most_played[0]

def sum_sold(file_name):
    copies_sold = []
    with open(file_name) as file:
        for line in file.readlines():
            line=line.split('\t')
            line[4] = line[4][:-1]
            copies_sold.append(float(line[1]))
        total_copies_sold = sum(copies_sold)
        return total_copies_sold

def get_selling_avg(file_name):
    copies = []
    with open(file_name) as file:
        for line in file.readlines():
            line=line.split('\t')
            line[4] = line[4][:-1]
            copies.append(float(line[1]))
        average_copies_sold = sum(copies)/len(copies)
        return average_copies_sold

def get_game(file_name, title):
    with open(file_name) as file:
        for line in file.readlines():
            line=line.split('\t')
            line[4] = line[4][:-1]
            choice = str(title)
            if choice in line:
                return line
