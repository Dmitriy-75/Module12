# Задача "Проверка на выносливость":
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.
#
# Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
# test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
# test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
# test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
# Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.

from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        self.walker = Runner(self)
        for i in range(0, 10):
            self.walker.walk()
        self.assertEqual(self.walker.distance, 50)

    def test_run (self):
        self.runner = Runner(self)
        for i in range(0, 10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 100)
        pass

    def test_challenge(self):
        self.runner = Runner(self)
        self.walker = Runner(self)
        for i in range(0, 10):
            self.runner.run()
            self.walker.walk()
        self.assertNotEqual(self.runner.distance, self.walker.distance)
        pass


RunnerTest()




