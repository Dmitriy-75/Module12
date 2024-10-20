#                          Задача "Логирование бегунов":

# Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
# В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
# Уровень - INFO
# Режим - запись с заменой('w')
# Название файла - runner_tests.log
# Кодировка - UTF-8
# Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.
#
# Дополните методы тестирования в классе RunnerTest следующим образом:
# test_walk:
# Оберните основной код конструкцией try-except.
# При создании объекта Runner передавайте отрицательное значение в speed.
# В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
# В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".
# test_run:
# Оберните основной код конструкцией try-except.
# При создании объекта Runner передавайте что-то кроме строки в name.
# В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
# В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".

import logging
from rt_with_exceptions import Runner
import unittest

logging.basicConfig(filename="runner_tests.log", level=logging.INFO, filemode='w', encoding="UTF-8",
                    format="s%(asctime)s| %(levelname)s| %(message)s-%(funcName)s")


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            self.walker = Runner('Вася', speed=-5)
            if self.walker.speed>0:
                logging.info('test_walk" выполнен успешно')
            for i in range(0, 10):
                self.walker.walk()
            self.assertEqual(self.walker.distance, 50)

        except ValueError:
            logging.warning('Неверная скорость для Runner')

    def test_run (self):
        try:
            self.runner = Runner(13, speed=5)
            if isinstance(self.runner.name,str):
                logging.info('test_run" выполнен успешно')
            for i in range(0, 10):
                self.runner.run()
            self.assertEqual(self.runner.distance, 100)

        except TypeError:
            logging.warning('Неверный тип данных для Runner')


if __name__ == '__main__':
    unittest.main()




