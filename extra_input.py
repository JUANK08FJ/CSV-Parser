import csv
import re


def get_range_years(higher_year, lower_year, injury_or_sales):
    while True:
        try:
            first_year = int(input(f'\nType the first year for the {injury_or_sales} interval between ({lower_year} - '
                                   f'{higher_year}) || (0. Exit): '))
        except ValueError:
            print('\nYou must enter one year. Try again')
            continue

        if first_year == 0:
            return None, None

        elif lower_year <= first_year <= higher_year:
            while True:
                try:
                    last_year = int(
                        input(f'\nType the final year for the {injury_or_sales} interval between ({lower_year} '
                              f'- {higher_year}) || (0. Exit): '))
                except ValueError:
                    print('\nYou must enter one year. Try again')
                    continue

                if last_year == first_year:
                    print(f'\nYou have already entered the year {last_year} before')

                elif last_year == 0:
                    return None, None

                elif lower_year <= last_year <= higher_year:
                    if first_year > last_year:
                        return last_year, first_year

                    else:
                        return first_year, last_year

                else:
                    print(f'\nThe year {last_year} isn\'t between ({lower_year} - {higher_year})')

        else:
            print(f'\nThe year {first_year} isn\'t between ({lower_year} - {higher_year})')


def get_three_years(higher_year, lower_year, not_used=None):
    while True:
        try:
            first_year = int(input('\nWrite the first year for the list of torture and moral integrity between '
                                   f'({lower_year} - {higher_year}) || (0. Exit): '))
        except ValueError:
            print('\nYou must enter one year. Try again')
            continue

        if first_year == 0:
            return None, None, None

        elif lower_year <= first_year <= higher_year:
            while True:
                try:
                    second_year = int(input('\nWrite the second year for the list of torture and moral integrity '
                                            f'between ({lower_year} - {higher_year}) || (0. Exit): '))
                except ValueError:
                    print('\nYou must enter one year. Try again')
                    continue

                if second_year == 0:
                    return None, None, None

                if first_year == second_year:
                    print(f'\nYou have already entered the year {second_year} before')

                elif lower_year <= second_year <= higher_year:
                    while True:
                        try:
                            third_year = int(input('\nWrite the third year for the list of torture and moral integrity '
                                                   f'between ({lower_year} - {higher_year}) || (0. Exit): '))
                        except ValueError:
                            print('\nYou must enter one year. Try again')
                            continue

                        if third_year == 0:
                            return None, None, None

                        if first_year == third_year or second_year == third_year:
                            print(f'\nYou have already entered the year {third_year} before')

                        elif lower_year <= third_year <= higher_year:
                            return first_year, second_year, third_year

                        else:
                            print(f'\nThe year {third_year} isn\'t between ({lower_year} - {higher_year})')

                else:
                    print(f'\nThe year {second_year} isn\'t between ({lower_year} - {higher_year})')

        else:
            print(f'\nThe year {first_year} isn\'t between ({lower_year} - {higher_year})')


def get_usable_years(injury_or_sales):
    higher_year = 0
    lower_year = 2024

    if injury_or_sales == 'injury':
        with open('violencia genere.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')

            for row in reader:
                if row[0].isdigit():
                    if int(row[0]) > higher_year:
                        higher_year = int(row[0])

            f.seek(0)

            for row in reader:
                if row[0].isdigit():
                    if int(row[0]) < lower_year:
                        lower_year = int(row[0])

    else:
        skip_first = None
        with open('slavery.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')

            for row in reader:
                if not skip_first:
                    skip_first = 'skipped'
                    continue

                else:
                    try:
                        if int(row[12][-4:]) > higher_year:
                            higher_year = int(row[12][-4:])
                    except ValueError:
                        continue

            f.seek(0)
            skip_first = None

            for row in reader:
                if not skip_first:
                    skip_first = 'skipped'
                    continue

                else:
                    try:
                        if int(row[12][-4:]) < lower_year:
                            lower_year = int(row[12][-4:])
                    except ValueError:
                        continue

    return higher_year, lower_year, injury_or_sales


def verify_slaveholder():
    with open('slavery.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')

        while True:
            skip_first = None
            slaveholder = re.sub(r'\s+', ' ', input('\nWrite the slaveholder to see how many slaves he has '
                                                    'brought || (0. Exit): ').strip())

            if slaveholder == '0':
                return None

            elif slaveholder == '' or slaveholder == ' ':
                print('\nThe slaveholder is blank you must enter something')
                continue

            else:
                for row in reader:
                    if not skip_first:
                        skip_first = 'skipped'
                        continue

                    else:
                        if row[1] == slaveholder:
                            return slaveholder

            print(f'\nThe slaveholder {slaveholder} doesn\'t exist in the csv file')
            f.seek(0)
