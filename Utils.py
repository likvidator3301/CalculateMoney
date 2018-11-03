from Entities import People


class ConsoleReaderWriter:
    def read_sums_from_console(self, dates, mouth):
        sums = []
        for i in dates:
            print('Введите сумму за день ' + str(i) + ' ' + mouth)
            sums.append(float(input()))
        return sums

class FileReaderWriter:
    def read_from_info_file(self, path_to_file):
        with open(path_to_file, 'r') as f:
            data = f.readlines()
        count_of_people, dates = data[0].split('-')
        count_of_people = int(count_of_people)
        dates = dates.split(' ')
        dates.remove('\n')
        dates = list(map(lambda x: int(x), dates))
        peoples = []

        for i in range(1, count_of_people + 1):
            name, visiting = data[i].split('-')
            people = People(name)
            visiting = visiting.split(' ')
            visiting.remove('\n')
            visiting = list(map(lambda x: bool(int(x)), visiting))
            people.set_visiting(dates, visiting)
            peoples.append(people)
        return peoples, dates

    def write_visiting_info_to_file(self, dates, peoples, path_to_file):
        result = ''
        result += str(len(peoples)) + '-'
        for date in dates:
            result += str(date) + ' '
        result += '\n'
        for people in peoples:
            result += people.name + '-'
            for visited in people.visiting.values():
                result += str(int(visited)) + ' '
            result += '\n'
        with open(path_to_file, 'w') as f:
            f.write(result)

    def write_report_to_file(self, dates, peoples, sums, path_to_file):
        result = ''
        max_lens = dict()
        i = 0
        for date in dates:
            max_len = max(len(str(date)), len(str(sums[i])))
            i += 1
            for people in peoples:
                if date in people.sums and len(str(people.sums[date])) > max_len:
                    max_len = len(str(people.sums[date]))
            max_lens[date] = max_len
        for date in dates:
            result += str(date) + ' ' * (max_lens[date] - len(str(date)) + 1)
        result += '\n'
        i = 0
        for date in dates:
            result += str(sums[i]) + ' ' * (max_lens[date] - len(str(sums[i])) + 1)
            i += 1
        result += '\n'
        for people in peoples:
            for date in dates:
                if date in people.sums:
                    result += str(people.sums[date]) + ' ' * (max_lens[date] - len(str(people.sums[date])) + 1)
                else:
                    result += '0' + ' ' * max_lens[date]
            result += people.name + ' ' + str(sum(people.sums.values())) + ' рублей\n'
        for date in dates:
            lsum = 0
            for people in peoples:
                if date in people.sums:
                    lsum += people.sums[date]
            result += str(lsum) + ' ' * (max_lens[date] - len(str(lsum)) + 1)

        with open(path_to_file, mode='w') as f:
            f.write(result)

