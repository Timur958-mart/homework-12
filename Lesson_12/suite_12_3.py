import unittest
import tests_12_3

test_run_tourn = unittest.TestSuite()
test_run_tourn.addTest(unittest.makeSuite(tests_12_3.RunnerTest))
test_run_tourn.addTest(unittest.makeSuite(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_run_tourn)
