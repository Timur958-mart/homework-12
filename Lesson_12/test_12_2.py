import unittest

from Lesson_12.runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run1 = Runner('Усейн', 10)
        self.run2 = Runner('Андрей', 9)
        self.run3 = Runner('Ник', 3)

    def test1_start(self):
        tourn_1 = Tournament(90, self.run1, self.run3)
        result_1 = tourn_1.start()
        k = max(result_1.keys())
        self.assertTrue(result_1[k] == 'Ник')
        self.all_results[1] = result_1

    def test2_start(self):
        tourn_2 = Tournament(90, self.run2, self.run3)
        result_2 = tourn_2.start()
        k = max(result_2.keys())
        self.assertTrue(result_2[k] == 'Ник')
        self.all_results[2] = result_2

    def test3_start(self):
        tourn_3 = Tournament(90, self.run1, self.run2, self.run3)
        result_3 = tourn_3.start()
        k = max(result_3.keys())
        self.assertTrue(result_3[k] == 'Ник')
        self.all_results[3] = result_3

    def test4_start(self):
        tourn_4 = Tournament(5, self.run3, self.run2, self.run1)
        result_4 = tourn_4.start()
        k = max(result_4.keys())
        self.assertTrue(result_4[k] == 'Ник')
        self.all_results[4] = result_4

    def test5_start(self):
        tourn_5 = Tournament(10, self.run3, self.run3, self.run1)
        result_5 = tourn_5.start()
        self.assertTrue( len(result_5) == 2)
        self.all_results[5] = result_5

    def test6_start(self):
        tourn_6 = Tournament(4, self.run2, self.run2, self.run2)
        result_6 = tourn_6.start()
        self.assertTrue(len(result_6) == 1)
        self.all_results[6] = result_6

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print({keys: str(values) for keys, values in result.items()})


if __name__ == '__main__':
    unittest.main()
