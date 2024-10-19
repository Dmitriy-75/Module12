# Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True. Напишите
# соответствующий декоратор к каждому методу (кроме @classmethod), который при значении is_frozen = False будет
# выполнять тесты, а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'.


from runner import Runner
import unittest
from runner_and_tournament import Runner,Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        self.walker = Runner(self)
        for i in range(0, 10):
            self.walker.walk()
        self.assertEqual(self.walker.distance, 50)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run (self):
        self.runner = Runner(self)
        for i in range(0, 10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 100)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.runner = Runner(self)
        self.walker = Runner(self)
        for i in range(0, 10):
            self.runner.run()
            self.walker.walk()
        self.assertNotEqual(self.runner.distance, self.walker.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = Runner('Усэйн',10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tur1(self):
        couple1 = Tournament(90,self.runner1, self.runner3)
        TournamentTest.all_results.append(couple1.start())
        self.assertTrue(TournamentTest.all_results[-1][2] == self.runner3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tur2(self):
        couple2 = Tournament(90,self.runner2, self.runner3)
        TournamentTest.all_results.append(couple2.start())
        self.assertTrue(TournamentTest.all_results[-1][2] == self.runner3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tur3(self):
        couple3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        TournamentTest.all_results.append(couple3.start())
        self.assertTrue(TournamentTest.all_results[-1][3] == self.runner3)

    @classmethod
    def tearDownClass(cls):
        for test in cls.all_results:
            print(test)

if __name__ == "__main__":
    unittest.main()