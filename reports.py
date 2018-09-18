
# Report functions

def count_games():
    with open('game_stat.txt') as file:
        text_to_convert_to_list= file
        text_to_convert_to_list=[]
        for line in file.readlines():
            line=line.split()
            line[5]=line[5][:-1]
            text_to_convert_to_list.append(line)
    print (text_to_convert_to_list)

count_games()
