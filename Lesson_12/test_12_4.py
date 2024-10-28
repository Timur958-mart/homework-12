import logging
import unittest
from rt_with_exeptions import Runner


class RunnerTest(unittest.TestCase):


    def test_walk(self):
        try:
            run1 = Runner('Михаил', -5)
            for i in range(10):
                run1.walk()
            self.assertEqual(run1.distance, 50)
            logging.info("'test_walk' выполнен успешно")
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            run2 = Runner(5, 4)
            for i in range(10):
                run2.run()
            self.assertEqual(run2.distance, 100)
            logging.info("'test_run' выполнен успешно")
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        run3 = Runner('Игорь', 4)
        run4 = Runner('Юрий', 5)
        for i in range(10):
            run3.run()
            run4.walk()
        self.assertNotEqual(run3.distance, run4.distance)

logging.basicConfig(level=logging.INFO, filemode='w', filename="runner_test.log", encoding= "utf-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")

if __name__ == '__main__':
    unittest.main()
