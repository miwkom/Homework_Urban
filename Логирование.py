import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только числом, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            r1 = Runner('Max', -5)
            for _ in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)
            logging.info('test_walk выполнен успешно')
        except ValueError:
            logging.error('Неверная скорость для Runner')

    def test_run(self):
        try:
            r1 = Runner(5)
            for _ in range(10):
                r1.run()
            self.assertEqual(r1.distance, 100)
            logging.info('test_run выполнен успешно')
        except TypeError:
            logging.error('Неверный тип данных для объекта Runner')

    def test_challenge(self):
        r1 = Runner('Max')
        r2 = Runner('Garry')
        for _ in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    unittest.main()
logging.basicConfig(level=logging.INFO,
                    filemode='w',
                    filename='runner test.log',
                    encoding='utf-8',
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
                    )