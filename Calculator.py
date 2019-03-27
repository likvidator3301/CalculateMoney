from operator import attrgetter
from Entities import People
from Utils import FileReaderWriter, ConsoleReaderWriter


class Calculator:
    def __init__(self, path_to_info, path_to_report, mode='file'):
        self.dates = []
        self.sums = []
        print('Введите название месяца:')
        self.mouth = input()
        self.peoples = []
        f = FileReaderWriter()
        if mode == 'file':
            self.peoples, self.dates = f.read_from_info_file(path_to_info)
        c = ConsoleReaderWriter()
        self.sums = c.read_sums_from_console(self.dates, self.mouth)
        self.calculate_sums(self.sums, self.peoples, self.dates)
        f.write_report_to_file(self.dates, self.peoples, self.sums, path_to_report)

    def read_from_console(self):
        peoples = []
        print('Введите через пробел числа учебных дней в месяце:')
        dates = list(map(lambda x: int(x), input().split(' ')))
        print(dates)
        print("Введите количество людей:")
        n = int(input())
        for i in range(0, n):
            print('Введите имя:')
            name = input()
            people = People(name)
            print('Введите информацию о посещаемости ученика через пробел.'
                  ' Введите "0" если ученик отсутствовал в данный день и "1" в ином случае.')
            print(self.join_dates(dates))
            visiting = list(map(lambda x: bool(int(x)), input().split(' ')))
            people.set_visiting(dates, visiting)
            peoples.append(people)
        print('\n'.join(list(map(lambda x: str(x), peoples))))

    def round_to_floor(self, x, length):
        s_x = str(x)
        index = s_x.find('.')
        if index == -1 or index + length >= len(s_x):
            return x
        return float(s_x[0:index + length + 1])

    def join_dates(self, dates):
        result = ''
        for date in dates:
            if len(str(date)) == 1:
                result += str(date) + ' '
            else:
                result += str(date)
        return result

    def calculate_sums(self, sums, peoples, dates):
        for i in range(0, len(sums)):
            sum = sums[i]
            date = dates[i]
            visited_peoples = self.get_visited_peoples(date, peoples)
            self.calculate_sum(sum, date, visited_peoples)
            peoples = sorted(peoples, key=attrgetter('count_of_increment'))
        return peoples

    def calculate_sum(self, sum, date, peoples):
        n = len(peoples)
        sum_per_people = self.round_to_floor(sum / n, 2)
        count_of_rest = int(round(self.round_to_floor(sum, 2) - self.round_to_floor(sum_per_people * n, 2), 2) / 0.01)
        for people in peoples:
            if count_of_rest > 0:
                people.add_sum(date, self.calculate_increment(sum_per_people))
                people.on_increment()
                count_of_rest -= 1
            else:
                people.add_sum(date, sum_per_people)

    def get_visited_peoples(self, date, peoples):
        result = []
        for people in peoples:
            if people.visiting[date]:
                result.append(people)
        return result

    def calculate_increment(self, x):
        up_x = x + 0.01
        rounded = self.round_to_floor(up_x, 2)
        if rounded == x:
            return round(up_x, 2)
        return rounded
