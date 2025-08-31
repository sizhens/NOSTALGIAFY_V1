import nostalgia_years
import dates_lister
import requests
import json
import urllib.request
import random

def values_generator():
    random_numbers = random.sample(range(40), 4)
    return random_numbers

selected_numbers = values_generator()

years_list = nostalgia_years.nostalgia_years_generator()

first_date = dates_lister.date_finder(years_list[0])

# print(first_date)

selected_date = []

def song_selector(selected_numbers, selected_date):
    intermediate_list = []
    chart_req = requests.get(f'https://raw.githubusercontent.com/mhollingshead/billboard-hot-100/main/date/{selected_date}.json')
    chart_data = chart_req.json()
    song_rank_list = chart_data.get("data")
    for selected_number in selected_numbers:
        song_selection = song_rank_list[selected_number]['song']
        song_artist = song_rank_list[selected_number]['artist']
        intermediate_list.append(f"{song_selection} by {song_artist}")
    return intermediate_list

def dates_maker(years_list):
    board_dates_list = []
    for x in years_list:
        new_date = dates_lister.date_finder(x)
        board_dates_list.append(new_date)
    # print(board_dates_list)
    return board_dates_list

dates = dates_maker(years_list)

# print(dates)

def final_compiler(dates):
    final_list = []
    for x in dates:
        selected_date = x
        final_entries = song_selector(selected_numbers, selected_date)
        final_list.append(final_entries)
    print(final_list)

print("Here is your selection of Nostalgia Jams")
final_compiler(dates)
