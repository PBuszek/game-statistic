import reports
import export

def printing_count_games():
    print("Number of games: ", reports.count_games('game_stat.txt'))
    export.export_count(reports.count_games('game_stat.txt'))

printing_count_games()


def printing_decide():
    year = input("Given year: ")
    print(reports.decide('game_stat.txt', year))
    export.export_decide(reports.decide('game_stat.txt', year))

printing_decide()


def printing_latest():
    print(reports.get_latest('game_stat.txt'))
    export.export_latest(reports.get_latest('game_stat.txt'))

printing_latest()


def printing_count_by_genre():
    genre = input("Given genre: ")
    print("Number of RPGs: ", reports.count_by_genre('game_stat.txt', genre))
    export.export_genre(reports.count_by_genre('game_stat.txt', genre))

printing_count_by_genre()


def printing_get_line_number_by_title():
    title = input("Given title: ")
    print("Line number: ", reports.get_line_number_by_title('game_stat.txt', title))
    export.export_title_line_number(reports.get_line_number_by_title('game_stat.txt', title))

printing_get_line_number_by_title()

#
