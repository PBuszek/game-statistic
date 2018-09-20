import reports
import export

def printing_get_most_played():
    print('Most played game: ', reports.get_most_played('game_stat.txt'))
    export.export_get_most_played(reports.get_most_played('game_stat.txt'))

printing_get_most_played()


def printing_sum_sold():
    print('Total copies sold: ', reports.sum_sold('game_stat.txt'))
    export.export_sum_sold(reports.sum_sold('game_stat.txt'))

printing_sum_sold()


def printing_get_selling_avg():
    print('Average copies sold: ', reports.get_selling_avg('game_stat.txt'))
    export.export_get_selling_avg(reports.get_selling_avg('game_stat.txt'))

printing_get_selling_avg()


def printing_get_game():
    choosen_game = input('Choose game: ')
    print('Game properties: ', reports.get_game('game_stat.txt', choosen_game))
    export.export_get_game(reports.get_game('game_stat.txt', choosen_game))

printing_get_game()
