import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    def testFirstTournament(self):
        tournament = Tournament(90, self.r1, self.r3)
        results = tournament.start()
        self.all_results['First Tournament'] = results
        last_name = list(results.values())[-1]
        self.assertTrue(last_name == 'Ник')

    def testSecondTournament(self):
        tournament = Tournament(90, self.r2, self.r3)
        results = tournament.start()
        self.all_results['Second Tournament'] = results
        last_name = list(results.values())[-1]
        self.assertTrue(last_name == 'Ник')

    def testThirdTournament(self):
        tournament = Tournament(90, self.r1, self.r2, self.r3)
        results = tournament.start()
        self.all_results['Third Tournament'] = results
        last_name = list(results.values())[-1]
        self.assertTrue(last_name == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for _ in cls.all_results:
            print(f'Results of {_}: {cls.all_results[_]}')


if __name__ == '__main__':
    unittest.main()
