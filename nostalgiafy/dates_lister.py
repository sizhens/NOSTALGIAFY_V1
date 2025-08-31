import pandas as pd
import numpy as np
import datetime
import json
import urllib.request, json
import requests

linked_file = requests.get('https://raw.githubusercontent.com/mhollingshead/billboard-hot-100/main/valid_dates.json')

def date_finder(year):
    loaded_data = linked_file.json()
    dates_in_year = []
    for dates in loaded_data:
        if dates.startswith(f"{year}"):
            dates_in_year.append(dates)

    last_date = max(dates_in_year)
    return last_date