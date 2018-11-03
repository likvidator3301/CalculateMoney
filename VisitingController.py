from Utils import FileReaderWriter
from Entities import People


class VisitingController:
    def __init__(self):
        self.peoples = []
        self.dates = []
        f = FileReaderWriter()
        try:
            self.peoples, self.dates = f.read_from_info_file('info.txt')
        except Exception:
            with open('names.txt', 'r') as file:
                for name in file.readlines():
                    self.peoples.append(People(name[0:len(name) - 1]))
        finally:
            self.read_visiting_data()

    def read_visiting_data(self):
        print('Введите число:')
        current_date = int(input())
        self.dates.append(current_date)
        print('Введите информацию о посещаемости учеников.'
              ' Введите 0, если ученик отсутствовал в данный день, 1 в ином случае.')
        for people in self.peoples:
            print(people.name + ':')
            people.visiting[current_date] = bool(int(input()))
        f = FileReaderWriter()
        f.write_visiting_info_to_file(self.dates, self.peoples, 'info.txt')
