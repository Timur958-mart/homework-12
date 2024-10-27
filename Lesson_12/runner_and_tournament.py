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

        """Новый список для сортировки переданных параметров и исключения дублирования объектов"""
        self.participants_new = []

    """Функция для сортировки и обработки списка с объектами класса"""
    def sorting(self):
        [self.participants_new.append(part) for part in self.participants if part not in self.participants_new]
        self.participants_new.sort(key=lambda x: x.speed, reverse=True)
        return self.participants_new

    def start(self):
        finishers = {}
        place = 1
        self.sorting()

        '''Новое условие цикла для обеспечения последовательности перебора объектов и правильной работы на маленьких 
        дистанциях'''
        while len(finishers) < len(self.participants_new):
            for participant in self.participants_new:
                if participant not in finishers.values():
                    participant.run()
                    if participant.distance >= self.full_distance:
                        finishers[place] = participant
                        place += 1
                        participant.distance = 0
        return finishers
