from operator import attrgetter
from Entities import People


def main():
    print(int(round(68.10 - 68.08, 2) // 0.01))
    print('Введите название мясяца:')
    mouth = input()
    peoples = []
    sums = []
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
        print(join_dates(dates))
        visiting = list(map(lambda x: bool(int(x)), input().split(' ')))
        people.set_visiting(dates, visiting)
        peoples.append(people)
    print('\n'.join(list(map(lambda x: str(x), peoples))))
    for i in dates:
        print('Введите сумму за день ' + str(i) + ' ' + mouth)
        sums.append(float(input()))
    print(sums)
    peoples = calculate_sums(sums, peoples, dates)
    write_to_file(peoples, dates, sums)


def write_to_file(peoples, dates, sums):
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

    with open('info.txt', mode='w') as f:
        f.write(result)


def round_to_floor(x, length):
    s_x = str(x)
    index = s_x.find('.')
    if index == -1 or index + length >= len(s_x):
        return x
    return float(s_x[0:index + length + 1])


def join_dates(dates):
    result = ''
    for date in dates:
        if len(str(date)) == 1:
            result += str(date) + ' '
        else:
            result += str(date)
    return result


def calculate_sums(sums, peoples, dates):
    for i in range(0, len(sums)):
        sum = sums[i]
        date = dates[i]
        visited_peoples = get_visited_peoples(date, peoples)
        calculate_sum(sum, date, visited_peoples)
        peoples = sorted(peoples, key=attrgetter('count_of_increment'))
    return peoples


def calculate_sum(sum, date, peoples):
    n = len(peoples)
    sum_per_people = round_to_floor(sum / n, 2)
    count_of_rest = int(round(round_to_floor(sum, 2) - round_to_floor(sum_per_people * n, 2), 2) / 0.01)
    for people in peoples:
        if count_of_rest > 0:
            people.add_sum(date, calculate_increment(sum_per_people))
            people.on_increment()
            count_of_rest -= 1
        else:
            people.add_sum(date, sum_per_people)


def get_visited_peoples(date, peoples):
    result = []
    for people in peoples:
        if people.visiting[date]:
            result.append(people)
    return result


def calculate_increment(x):
    up_x = x + 0.01
    rounded = round_to_floor(up_x, 2)
    if rounded == x:
        return round(up_x, 2)
    return rounded


if __name__ == '__main__':
    main()
