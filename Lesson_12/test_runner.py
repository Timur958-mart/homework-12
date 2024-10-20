from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run1 = Runner('Михаил')
        for i in range(10):
            run1.walk()
        self.assertEqual(run1.distance, 50)

    def test_run(self):
        run2 = Runner('Николай')
        for i in range(10):
            run2.run()
        self.assertEqual(run2.distance, 100)

    def test_challenge(self):
        run3 = Runner('Игорь')
        run4 = Runner('Юрий')
        for i in range(10):
            run3.run()
            run4.walk()
        self.assertNotEqual(run3.distance, run4.distance)


if __name__ == '__main__':
    unittest.main()
