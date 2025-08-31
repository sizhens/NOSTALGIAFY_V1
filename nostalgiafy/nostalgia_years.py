from datetime import datetime
def nostalgia_years_generator():
    age = int(input("What is your current age? "))
    prime_age_start = int(11)
    prime_age_end = int(15)
    prime_age_range = prime_age_end - prime_age_start
    current_date_time = datetime.now()
    current_year = int(current_date_time.year)
    nostalgia_years_difference = age - prime_age_start
    nostalgia_years_start = int(current_year) - int(nostalgia_years_difference)
    nostalgia_years_list = []
    if nostalgia_years_start < 1958:
        print("Sorry! You're too old for Billboard Hot 100 Nostalgia! Congratulations!")
        quit()

    # print(f"Your age is {age} and the year is {current_year}. Is that correct?")

    print(f"Your first nostalgia year is {nostalgia_years_start}.")

    for year in range(prime_age_range):
        if nostalgia_years_list == []:
            nostalgia_years_list.append(int(nostalgia_years_start))
        else:
            nostalgia_years_list.append(
                nostalgia_years_start + year
            )

    print(f"Your nostalgia years are {nostalgia_years_list}")

    return nostalgia_years_list