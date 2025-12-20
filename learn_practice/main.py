import time
from datetime import date, datetime, timedelta
import calendar

from file_lessons import file_lessons
from time_practice import time_lessons
from dict_practice import dict
from string_lessons import string_practice
from lists_lessons import list_practice
from main_menu import start_menu
LINE = "═" * 70

if __name__ == "__main__":
    while True:
        start_menu.main()