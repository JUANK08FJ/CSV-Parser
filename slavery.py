import csv
import extra_input


def top_slaveholder():
    skip_first = None
    slaveholder_purchases = {}

    with open('slavery.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            if not skip_first:
                skip_first = 'skipped'
                continue

            else:
                if row[1] not in slaveholder_purchases:
                    slaveholder_purchases[row[1]] = 1

                else:
                    slaveholder_purchases[row[1]] += 1

    count = 0
    person = ''
    for owner, counter in slaveholder_purchases.items():
        if counter > count:
            count = counter
            person = owner

    return count, person


def top_supplier_state():
    skip_first = None
    suppliers = {}

    with open('slavery.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            if not skip_first:
                skip_first = 'skipped'
                continue

            else:
                if row[5] not in suppliers:
                    suppliers[row[5]] = [1, row[3]]
                else:
                    suppliers[row[5]] = [suppliers[row[5]][0] + 1, row[3]]

    count = 0
    state = ''
    for supplier, slaves_state in suppliers.items():
        if slaves_state[0] > count:
            count = slaves_state[0]
            state = slaves_state[1]

    return count, state


def average_age_women():
    skip_first = None
    female_counter = 0
    sum_ages = 0

    with open('slavery.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            if not skip_first:
                skip_first = 'skipped'
                continue

            else:
                if row[9] == 'F':
                    female_counter += 1
                    sum_ages += float(row[8])

    return round(sum_ages / female_counter, 2)


def sold_slaves_by_gender():
    skip_first = None
    female_counter = 0
    male_counter = 0

    with open('slavery.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            if not skip_first:
                skip_first = 'skipped'
                continue

            else:
                if row[9] == 'F':
                    female_counter += 1
                else:
                    male_counter += 1

    return female_counter, male_counter


def average_sell_price():
    skip_first = None
    slaves_counter = 0
    total_price = 0

    with open('slavery.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            if not skip_first:
                skip_first = 'skipped'
                continue

            else:
                total_price += float(row[19])
                slaves_counter += 1

    return round(total_price / slaves_counter, 2)


def slaveholder_purchasess():
    skip_first = None
    slaveholder = [extra_input.verify_slaveholder(), 0]

    with open('slavery.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')

        if not slaveholder[0]:
            return None

        else:
            for row in reader:
                if not skip_first:
                    skip_first = 'skipped'
                    continue

                else:
                    if row[1] == slaveholder[0]:
                        slaveholder[1] += 1

    return slaveholder


def average_sell_price_by_gender():
    skip_first = None
    price_by_gender = {'Female': [0, 0], 'Male': [0, 0]}

    with open('slavery.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            if not skip_first:
                skip_first = 'skipped'
                continue

            else:
                if row[9] == 'F':
                    price_by_gender['Female'][0] += float(row[19])
                    price_by_gender['Female'][1] += 1

                else:
                    price_by_gender['Male'][0] += float(row[19])
                    price_by_gender['Male'][1] += 1

    avg_female_price = round(price_by_gender['Female'][0] / price_by_gender['Female'][1], 2)
    avg_male_price = round(price_by_gender['Male'][0] / price_by_gender['Male'][1], 2)

    return avg_female_price, avg_male_price


def total_sales_between_years():
    years_sales = 0
    skip_first = None

    with open('slavery.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        initial_year, end_year = extra_input.get_range_years(*extra_input.get_usable_years('sales'))

        if initial_year:
            for row in reader:
                if not skip_first:
                    skip_first = 'skipped'
                    continue

                else:
                    for year in range(initial_year, end_year + 1):
                        try:
                            if year == int(row[12][-4:]):
                                years_sales += 1
                        except ValueError:
                            continue

            return initial_year, end_year, years_sales

    return initial_year, end_year, None
