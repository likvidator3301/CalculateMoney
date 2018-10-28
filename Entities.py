class People:
    def __init__(self, name):
        self.name = name
        self.visiting = dict()
        self.count_of_increment = 0
        self.sums = dict()

    def __str__(self):
        return self.name + '\n' + ' '.join(list(map(lambda x: str(x), self.sums.values())))

    def on_increment(self):
        self.count_of_increment += 1

    def set_visiting(self, keys, values):
        for i in range(0, len(keys)):
            self.visiting[keys[i]] = values[i]

    def add_sum(self, date, value):
        self.sums[date] = value
