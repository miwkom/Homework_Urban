import unittest
import МетодыЮнитТестирования
import ПростыеЮнитТесты

Test = unittest.TestSuite()
Test.addTest(unittest.TestLoader().loadTestsFromTestCase(ПростыеЮнитТесты.RunnerTest))
Test.addTest(unittest.TestLoader().loadTestsFromTestCase(МетодыЮнитТестирования.TournamentTest))


StartTest = unittest.TextTestRunner(verbosity=2)
StartTest.run(Test)