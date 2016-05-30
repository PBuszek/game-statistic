import reports
import unittest

class Evaluator(unittest.TestCase):
    maxpoints = 10
    points = 0

    def start(self, input_file):
        self.test1(input_file)
        self.test2(input_file)
        self.test3(input_file)
        self.test4(input_file)
        self.test5(input_file)
        self.test_bonus1(input_file)
        self.test_bonus2(input_file)
        self.test_bonus3(input_file)

        #reduce points to the maximum
        if self.points > 10:
            self.points = 10

        print("Your points: " + str(self.points) + " / " + str(self.maxpoints))

    def test1(self, input_file):
        try:
            dir(reports).index("count_games")
        except ValueError:
            print("Function 'count_games' is not found")
            return
        result = reports.count_games(input_file)
        self.assertEqual(result, 24)
        if(result == 24):
            self.points += 2
            print("Function 'count_games' is passed. 2 points.")

    def test2(self, input_file):
        try:
            dir(reports).index("decide")
        except ValueError:
            print("Function 'decide' is not found")
            return
        result = reports.decide(input_file, 2000)
        self.assertTrue(result)
        if(result == True):
            self.points += 2
            print("Function 'decide' is passed. 2 points.")

    def test3(self, input_file):
        try:
            dir(reports).index("get_latest")
        except ValueError:
            print("Function 'get_latest' is not found")
            return
        result = reports.get_latest(input_file)
        self.assertEqual(result, "Diablo III")
        if(result == "Diablo III"):
            self.points += 2
            print("Function 'get_latest' is passed. 2 points.")

    def test4(self, input_file):
        try:
            dir(reports).index("count_by_genre")
        except ValueError:
            print("Function 'count_by_genre' is not found")
            return
        result = reports.count_by_genre(input_file, "First-person shooter")
        self.assertEqual(result, 6)
        if (result == 6):
            self.points += 2
            print("Function 'count_by_genre' is passed. 2 points.")

    def test5(self, input_file):
        try:
            dir(reports).index("get_line_number_by_title")
        except ValueError:
            print("Function 'get_line_number_by_title' is not found")
            return
        result = reports.get_line_number_by_title(input_file, "Counter-Strike")
        self.assertEqual(result, 6)
        if (result == 6):
            self.points += 2
            print("Function 'get_line_number_by_title' is passed. 2 points.")

    def test_bonus1(self, input_file):
        try:
            dir(reports).index("sort_abc")
        except ValueError:
            print("Bonus function 'sort_abc' is not found")
            return
        expected_result = ['Age of Empires', 'Command & Conquer', 'Counter-Strike', 'Counter-Strike: Condition Zero', 'Crysis',
         'Diablo II', 'Diablo III', 'Doom 3', 'EverQuest', "Garry's Mod", 'Guild Wars', 'Half-Life', 'Half-Life 2',
         'Minecraft', 'Populous', 'StarCraft', 'StarCraft II', 'Terraria', 'The Sims', 'The Sims 2', 'The Sims 3',
         'Warcraft III: Reign of Chaos', 'Warhammer 40,000: Dawn of War (including expansions)', 'World of Warcraft']
        result = reports.sort_abc(input_file)

        points = 2
        self.assertEqual(len(result), len(expected_result))
        if len(result) != len(expected_result):
            --points

        L = []
        for i in range(0, min(len(result), len(expected_result))):
            self.assertEqual(result[i], expected_result[i])
            if result[i] != expected_result[i]:
                --points

        if points >= 0:
            self.points += points
            print("Bonus function 'sort_abc' is passed. " + str(points) + " points.")

    def test_bonus2(self, input_file):
        try:
            dir(reports).index("get_genres")
        except ValueError:
            print("Bonus function 'get_genres' is not found")
            return
        result = reports.get_genres(input_file)
        self.assertEqual(24, result)
        if (result == 24):
            self.points += 2
            print("Bonus function 'get_genres' is passed. 2 points.")

    def test_bonus3(self, input_file):
        try:
            dir(reports).index("when_was_top_sold_fps")
        except ValueError:
            print("Bonus function 'when_was_top_sold_fps' is not found")
            return
        result = reports.when_was_top_sold_fps(input_file)
        self.assertEqual(24, result)
        if (result == 24):
            self.points += 2
            print("Bonus function 'when_was_top_sold_fps' is passed. 2 points.")

Evaluator().start("game_stat.txt")