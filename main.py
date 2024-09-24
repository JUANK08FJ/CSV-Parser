import gender_violence
import slavery

while True:
    try:
        csv_selector = int(input('\033[1;33mWhich csv would you like to access for information?\n\033[1;33m1 |\033[;34m'
                                 ' Gender Violence\n\033[1;33m2 |\033[;34m Slavery\n\033[1;33m0 |\033[;34m Exit\n'
                                 '\033[1;33mEnter the number: \033[0;m'))

        if csv_selector == 0:
            print('\n\033[1;31mGOODBYE ;>)\033[0;m')
            break

        elif csv_selector == 1:
            while True:
                try:
                    gv_select = int(input('\n\033[1;35mWhat action do you want to take in the gender violence csv?\n1 |'
                                          ' \033[;32mTotal criminal offenses \n\033[1;35m2 | \033[;32mCoercion average'
                                          '\n\033[1;35m3 | \033[;32mTotal injuries between two years\n\033[1;35m4 | '
                                          '\033[;32mYear with the highest number of crimes\n\033[1;35m5 | \033[;32m'
                                          'List of tortures and moral integrity, selecting three years\n\033[1;35m6 | '
                                          '\033[;32mYears in which crimes have resulted in criminal convictions \n'
                                          '\033[1;35m7 | \033[;32mTotal faults\n\033[1;35m0 | \033[;32mExit\n\033[1;35m'
                                          'Enter the number: \033[0;m'))

                    if gv_select == 0:
                        print('\n\033[1;31mBack to the initial menu...\n\033[0;m')
                        break

                    elif gv_select == 1:
                        print(f'\n\033[;31mThere have been \033[4;34m{gender_violence.criminal_offenses()}\033[;31m '
                              'criminal offenses in total\033[;m')

                    elif gv_select == 2:
                        print(f'\n\033[;31mThe average total coercion was \033[4;34m'
                              f'{gender_violence.coercion_average()}\033[;m')

                    elif gv_select == 3:
                        initial_year, end_year, injures = gender_violence.injures_years()

                        if not initial_year:
                            print('\n\033[1;31mSearch for injured between years was cancelled\033[;m')

                        else:
                            print(f'\n\033[;31mThe total number of injured people between \033[4;34m{initial_year}'
                                  f'\033[;31m and \033[4;34m{end_year}\033[;31m was \033[4;34m{injures}\033[;31m people'
                                  '\033[;m')

                    elif gv_select == 4:
                        crimes, year = gender_violence.total_crimes()
                        print(f'\n\033[4;34m{year}\033[;31m is the year with the highest number of crimes in total, '
                              f'with \033[4;34m{crimes}\033[;31m crimes\033[;m')

                    elif gv_select == 5:
                        count = 1
                        order_list = gender_violence.years_torture_integrity()

                        if not order_list:
                            print('\n\033[1;31mTorture and moral integrity list search was cancelled\033[;m')

                        else:
                            print('\n\033[1;31mDescending ordered list of torture and moral integrity in the years '
                                  'provided\033[;m\n\033[3;31mTop || Year || Torture and moral integrity\033[;m')

                            for year, tortures in order_list.items():
                                print(f'\033[3;34m {count}  || {year} || {tortures}\033[;m')
                                count += 1

                    elif gv_select == 6:
                        years = gender_violence.years_criminals_convictions()

                        print(f'\n\033[1;31mThere have been \033[4;34m{len(years)}\033[;31m years in which the '
                              'offenses have resulted in criminal convictions:\n\033[3;31mYear || Criminal offenses '
                              'equal to crimes\033[;m')

                        for year, crimes in years.items():
                            print(f'\033[3;34m{year} || {crimes}\033[;m')

                    elif gv_select == 7:
                        faults_dic = gender_violence.verify_total_faults()
                        print()

                        for year, faults in faults_dic.items():
                            print(f'\033[;31mThe year \033[4;34m{year}\033[;31m has now \033[4;34m{faults[0]}\033[;31m '
                                  f'total faults and should be \033[4;34m{faults[1]}\033[;31m faults\033[;m')

                    else:
                        print('\n\033[1;31mYou must enter a correct number. Try again\033[;m')

                except ValueError:
                    print('\n\033[1;31mYou must enter a number. Try again\033[;m')

        elif csv_selector == 2:
            while True:
                try:
                    svy_select = int(input('\nWhat action do you want to do in the slavery csv?\n1 | Slaveholder who '
                                           'bought more slaves\n2 | State of the supplier who sold the most slaves\n'
                                           '3 | Average age of each female slave\n4 | Total slaves sold by gender\n'
                                           '5 | Average selling price\n6 | See how many slaves a slaveholder bought\n'
                                           '7 | Average selling price by gender\n8 | Total sales between two years\n'
                                           '0 | Exit\nEnter the number: '))

                    if svy_select == 0:
                        print('\nBack to the initial menu...\n')
                        break

                    elif svy_select == 1:
                        slaves_count, slaveholder = slavery.top_slaveholder()
                        print(f'\nThe slaveholder {slaveholder} has bought the largest number of slaves with '
                              f'{slaves_count} slaves')

                    elif svy_select == 2:
                        slaves_count, state = slavery.top_supplier_state()
                        print(f'\nThe supplier with the highest number of slaves sold was from {state} and sold '
                              f'{slaves_count} slaves')

                    elif svy_select == 3:
                        print(f'\nThe average age of female slaves was {slavery.average_age_women()} years')

                    elif svy_select == 4:
                        female, male = slavery.sold_slaves_by_gender()
                        print(f'\nA total of, {female} female slaves and {male} male slaves were sold')

                    elif svy_select == 5:
                        print(f'\nThe average sell price for a slave was ${slavery.average_sell_price()}')

                    elif svy_select == 6:
                        slaveholder = slavery.slaveholder_purchasess()

                        if not slaveholder:
                            print('\nSearch for the number of purchases by slaveholder was cancelled')

                        else:
                            print(f'\nThe slaveholder {slaveholder[0]} has bought {slaveholder[1]} slaves')

                    elif svy_select == 7:
                        avg_female_price, avg_male_price = slavery.average_sell_price_by_gender()

                        print(f'\nThe average selling price for female slaves was ${avg_female_price} and '
                              f'${avg_male_price} for male slaves')

                    elif svy_select == 8:
                        initial_year, end_year, sales = slavery.total_sales_between_years()

                        if not initial_year:
                            print('\nSearch for sales between years was cancelled')

                        else:
                            print(f'\nThe total number of people sold between {initial_year} and {end_year} was '
                                  f'{sales} people')

                    else:
                        print('\nYou must enter a correct number. Try again')

                except ValueError:
                    print('\nYou must enter a number. Try again')

        else:
            print('\n\033[1;31mYou must enter a correct number. Try again\n\033[;m')

    except ValueError:
        print('\033[1;31m\nYou must enter a number. Try again\n\033[;m')
