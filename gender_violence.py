import csv
import extra_input


def criminal_offenses():
    total = 0

    with open('violencia genere.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[1].isdigit():
                total += int(row[1])

    return total


def coercion_average():
    years, total_coercions = 0, 0

    with open('violencia genere.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[7].isdigit():
                years += 1
                total_coercions += int(row[7])

    return round(total_coercions / years, 2)


def injures_years():
    injures = 0

    with open('violencia genere.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        initial_year, end_year = extra_input.get_range_years(*extra_input.get_usable_years('injury'))

        if initial_year:
            for row in reader:
                for year in range(initial_year, end_year + 1):
                    if row[4].isdigit() and year == int(row[0]):
                        injures += int(row[4])

            return initial_year, end_year, injures

    return initial_year, end_year, None


def total_crimes():
    higher_crimes = 0

    with open('violencia genere.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[0].isdigit():
                row_crimes = int(row[2])

                if row_crimes > higher_crimes:
                    year = row[0]
                    higher_crimes = row_crimes

    return higher_crimes, year


def years_torture_integrity():
    final_list = {}

    with open('violencia genere.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        first_year, second_year, third_year = extra_input.get_three_years(*extra_input.get_usable_years('injury'))

        if first_year:
            for row in reader:
                if row[0].isdigit() and (
                        int(row[0]) == first_year or int(row[0]) == second_year or int(row[0]) == third_year):
                    final_list[row[0]] = int(row[8])

            return dict(sorted(final_list.items(), key=lambda item: item[1], reverse=True))

    return None


def years_criminals_convictions():
    years_list = {}

    with open('violencia genere.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[0].isdigit() and row[1] == row[2]:
                years_list[row[0]] = row[2]

    return years_list


def verify_total_faults():
    total_faults = {}

    with open('violencia genere.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            if row[0].isdigit():
                total = int(row[17]) + int(row[18])
                if int(row[16]) != total:
                    total_faults[row[0]] = [int(row[16]), total]

    return total_faults
