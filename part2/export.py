
from reports import *
# Export functions

my_file = 'reports.txt'


def clear():
    with open(my_file, 'w'):
        pass


def write(line):
    with open(my_file, mode='a') as myfile:
        myfile.write(str(line) + '\n')

clear()

write('What is the title of the most played game?:')
answer = get_most_played(txt_file)
write(answer)

write('How many copies have been sold total?:')
answer = sum_sold(txt_file)
write(answer)

write('What is the average selling?:')
answer = get_selling_avg(txt_file)
write(answer)

write('How many characters long is the longest title?:')
answer = count_longest_title(txt_file)
write(answer)

write('What is the average of the release dates?:')
answer = get_date_avg(txt_file)
write(answer)

write('What properties has a game?:')
answer = get_game(txt_file, "Counter-Strike")
write(answer)

write('How many games are there grouped by genre?:')
answer = count_grouped_by_genre(txt_file)
write(answer)

write('What is the date ordered list of the games?:')
answer = get_date_ordered(txt_file)
write(answer)
