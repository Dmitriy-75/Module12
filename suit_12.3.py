# Задача "Заморозка кейсов":
# Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с произвольным названием.
# Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
# Создайте объект класса TextTestRunner, с аргументом verbosity=2.

import unittest
import module_12_3
sum_test = unittest.TestSuite()
sum_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.RunnerTest))
sum_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(sum_test)