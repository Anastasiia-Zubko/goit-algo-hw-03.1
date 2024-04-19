from datetime import datetime, timedelta
import random
import re

#Task 1

print("\nTask 1:\n")

def get_days_from_today(dat:str)-> int:
    try:
        now = datetime.today() # get current date
        formatted_date = datetime.strptime(dat, "%Y-%m-%d") # transform the string to the datetime format 
        result = now-formatted_date # get the difference between the dates
        print(result.days)
        return result.days # return the difference in days only 
    except ValueError: # catch ValueError in case the string {dat} does not match format '%Y-%m-%d"
        print(f"The string {dat} does not match format '%Y-%m-%d")

get_days_from_today('2021-10-09')

# Task 2

print("\nTask 2:\n")

def get_numbers_ticket(min, max, quantity):
    if quantity > (max-min): # check that the quantity is within the range 
        return print("quantity - кількість чисел, які потрібно вибрати (значення між min і max)")
    
    numbers = [] # create an empty list for numbers 
    #weights = [] # create an empty list for weights 
    for x in range(min, max+1): #loop through the range between min and max 
        numbers.append(x) # add each number within the range to the list 
        #weights.append(1) # for each added number add 1 to weights to ensure uniqueness 
    random_numbers = random.sample(numbers, quantity) # get random numbers 
    sorted_numbers = tuple(sorted(random_numbers)) # sort our tuple 
    return sorted_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

# Task 3

print("\nTask 3:\n")

def normalize_phone(phone_number:str):
    pattern_charachters = r"[^0-9+]" # all charachters except numbers and plus
    replacement = "" # empty string 
    modified_number = re.sub(pattern_charachters , replacement, phone_number) # replace all charachters except numbers and plus with an empty string

    area_code ="+380" # area code for adding to numbers
    pattern_full = "\+380" #area code for search function with escape charachter , since without it , the code throws an error 
    pattern_plus ="380" # area code without plus
    complete_number = re.search(pattern_full, modified_number) # check if numbers starts with +380 
    incomplete_number = re.search(pattern_plus, modified_number) # check if numbers starts with 380 

    if complete_number: # check if numbers starts with +380 
        return modified_number # return the number 
    elif incomplete_number: # check if numbers starts with 380 
        return re.sub(pattern_plus, area_code, modified_number) # replace 380 with +380 and return the number 
    else: # when the number is without area code 
        return area_code+modified_number # add +380 and return the number 


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

# Task 4

print("\nTask 4:\n")

def get_upcoming_birthdays(users:dict):
    upcoming_birthdays =[] # empty list for upcoming birthdays 
    today = datetime.today().date() # get current date

    for user in users: #  iterate through all the users
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date() # convert birthday into a datetime object from string
        birthday_now = datetime(year=today.year, month=birthday.month, day=birthday.day).date() # convert the date of birth into current year

        if birthday_now < today: # check if the birthday is in the past
            birthday_now = birthday_now.replace(year=today.year + 1) # add 1 year to the birthday

            
        days = birthday_now - today # calculate number of days between birthday and today

        if birthday_now.isoweekday() == 6: # check if birthday is on Saturday
            birthday_now = birthday_now + timedelta(days=2) # add 2 days to the date 
        elif birthday_now.isoweekday() == 7: # check if birthday is on Sunday
            birthday_now = birthday_now + timedelta(days=1) # add 1 day to the date 
        else: # birthday is between Mon - Fri
            pass # do not change the date

        if days.days <= 7: #check if the birthday is within the next 7 days 
            upcoming_birthdays.append({user["name"]:birthday_now.strftime("%Y-%m-%d")}) # add the birthday to upcoming_birthdays
        else:
            pass # ignore if its not within the next 7 days 
              
    if upcoming_birthdays: # check if there are upcoming birthdays  
        return upcoming_birthdays # return the birthday 
    else:
        return "No upcoming birthdays" # if there are no upcoming birthdays return "No upcoming birthdays"
        

users = [
    {"name": "John Doe", "birthday": "1985.04.19"},
    {"name": "Jane Smith", "birthday": "1990.04.20"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

