import pandas as pd
import os
import requests
import json
import sys
wowDataFinal = 'wowDataFinal.csv'
# print("Welcome to the Python WOW of Kevin Campfield and Yusuf Bolden. For this")
# print("project we are taking a users' inputs to a survey and adding them to a dataframe")
# print("that can be distributed by city and school officials at the beginning of each year")
# print("to create a database with the information which can then be used to")
# print("determine the residents and students who should be listed as priority")
# print("recipients for emergency resources and the method by which")
# print("resources would reach these residents in the fastest manner.\n")
print("The following information is collected for statistical purposes and")
print("will not be published, distributed or otherwise sold to any third party.\n")
print("You must be a United States resident between the ages of 18-50 to complete")
print("this survey. A United States resident is anyone who resides within the")
print("50 States.\n")
print("This survey consists of 20 questions. The estimated time to complete this survey is 10 minutes.")
print("Please take your time reading and answering each question. You will not be able to change your answers.\n")
#
name = input("What is your first name?\nPlease enter your name: ")
name = name.title()
print("Welcome", name)

while True:
    USResident = input("Are you a resident of the United States?\n[Please enter Yes or No]: ")
    if USResident in ["Yes", "YES", "y", "Y", "yes"]:
        print("Great! You are a United States resident.")
        break
    elif USResident in ["No", "NO", "n", "N", "no"]:
        print("Sorry! This survey is only for United States residents.")
        while True:
            USResident = input("Are you a resident of the United States?\n[Please enter Yes or No]: ")
            if USResident in ["Yes", "YES", "y", "Y", "yes"]:
                print("Great! You are a United States Resident")
                break
            elif USResident in ["No", "NO", "n", "N", "no"]:
                sys.exit("Sorry! This survey is only for United States residents. Thanks for trying.")
            else:
                print("Sorry! Invalid entry! Please try again")
        break
    else:
        print("Sorry! Invalid entry! Please try again")

while True:
    language = input("Are you able to complete this survey in English?\n[Please enter Yes or No]: ")
    if language in ["Yes", "YES", "y", "Y", "yes"]:
        print("Great! We will continue in English.")
        break
    elif language in ["No", "NO", "n", "N", "no"]:
        print("Sorry! This survey can only be completed in English.")
        while True:
                language = input("Are you able to complete this survey in English?\n[Please enter Yes or No]: ")
                if language in ["Yes", "YES", "y", "Y", "yes"]:
                    print("Great! We will continue in English.")
                    break
                elif language in ["No", "NO", "n", "N", "no"]:
                    sys.exit("Sorry! This survey can only be completed in English. Thanks for trying.")
                else:
                    print("Sorry! Invalid entry! Please try again.")
        break
    else:
        print("Sorry! Invalid entry! Please try again.")

while True:
    gender = input("Please select your gender:\n[Please enter Male, Female or Other]: ")
    if gender in ["M", "m", "MALE", "Male", "male"]:
        gender = 'm'
        print("You entered Male")
        break
    elif gender in ["F", "f", "FEMALE", "Female", "female"]:
        gender = 'f'
        print("You entered Female")
        break
    elif gender in ["O", "o", "OTHER", "Other", "other"]:
        gender = 'o'
        print("You entered Other")
        break
    else:
        print("Invalid entry! Please try again.")

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError :
            print("Invalid entry! Please try again.")
            continue
        else:
            return userInput
            break

age = inputNumber("Please enter your age: [Age must be between 18 and 50]\nPlease enter your age: ")
if age >= 18 and age <= 50:
    print(f"Great! Your age is {age}, which is within the correct range.")
else:
    print("Invalid entry! Please try again.")

while True:
    race = input("Which of the following best describes your race or ethnicity?\n[Please enter White, Black, Hispanic, Asian, Native American, Mixed or Other]: ")
    race = race.lower()
    if race in ["white", "black", "hispanic", "asian","native american", "mixed", "other"]:
        print("Great! You listed your race as", race.title())
        break
    else:
        print("Invalid entry! Please try again.")

API_KEY = "JlfALuS6idZcTt2Cn5Z3FkUEosJSRkpfNnMV58w6PD3T971F0jUPuw087c0orm37"

while True:

  zipcode = input("What is your zip code?\nPlease enter your zip code: ")

  api_url = "https://www.zipcodeapi.com/rest/" + API_KEY + "/info.json/" + zipcode + "/degrees"

  response = requests.get(api_url)
  if response.status_code == 200:
    break
  print("Invalid entry! Please try again.")

datastore = json.loads(response.content)

input_city = datastore['city']
input_state = datastore['state']

print(f"Great! You live in {input_city}, {input_state} and your zipcode is {zipcode}.")

while True:
    number_of_children_in_household = int(input("How many children under 18 years' old reside in your household?\n[Please enter a number]: "))
    if number_of_children_in_household == 0:
        other_parent_in_household = 0
        print(f"You entered there are {number_of_children_in_household} children under 18 years' old in your household.")
        break
    else:
        if number_of_children_in_household == 1:
            child_or_children = 'child'
            is_or_are = 'is'
        else:
            child_or_children = 'children'
            is_or_are = 'are'
        print(f"You entered there {is_or_are} {number_of_children_in_household} {child_or_children} under 18 years' old in your household.")
        other_parent_in_household = input(f"Does the other parent of your {child_or_children} reside in the household?\n[Enter yes or no]: ")
        if other_parent_in_household in ["Yes", "YES", "y", "Y", "yes"]:
            other_parent_in_household = 'y'
            print("You entered the other parent DOES live in the household")
            break
        elif other_parent_in_household in ["No", "NO", "n", "no"]:
            other_parent_in_household = 'n'
            print("You entered the other parent DOES NOT live in the household")
            break
        else:
            print("Invalid entry! Please try again.")
        break

while True:
    total_household_size = int(input("Including yourself, how many total persons reside in your household?\n[Please enter a number]: "))
    if total_household_size == 0:
        print("Invalid entry! Total household size must be greater than or equal to 1.")
    elif total_household_size >= 1:
        print(f"Your entered your total_household_size is {total_household_size}.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    high_school_or_higher = input("Did you receive your high school diploma or high school equivalency such as a GED?\n[Please enter yes or no]: ")
    if high_school_or_higher in ["Yes", "YES", "y", "Y", "yes"]:
        high_school_or_higher = 'y'
        print("Great! You are a high school graduate.")
        break
    elif high_school_or_higher in ["No", "NO", "n", "N", "no"]:
        high_school_or_higher = 'n'
        print("You entered you DID NOT graduate high school or obtain a high school equivalency.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    employed = input("Are you currently employed either full-time or part-time?\n[Please enter yes or no]: ")
    if employed in ["Yes", "YES", "y", "Y", "yes"]:
        employed = 'y'
        print("Great! You are currently employed.")
        break
    elif employed in ["No", "NO", "n", "N", "no"]:
        employed = 'n'
        print("You entered you ARE NOT currently employed.")
        break
    else:
        print("Invalid entry! Please try again.")
while True:
    personal_income = int(input("What is your personal income?\n[Please enter whole number than identifes your current income without using any commas, spaces or decimal]: "))
    def is_digit(personal_income):
        if personal_income.isdigit():
            print(f"You entered your personal income as {personal_income}")
        else:
            print("Invalid entry! Please enter a whole number that represents your current personal income.")
    print(f"You entered your current income is ${personal_income}.")
    break


while True:
    homeowner = input("Do you own your home?\n[Please enter yes or no]: ")
    if homeowner in ["Yes", "YES", "y", "Y", "yes"]:
        homeowner = 'y'
        print("You entered that you own your home.")
        break
    elif homeowner in ["No", "NO", "n", "N", "no"]:
        homeowner ='n'
        print("You entered you DO NOT own your home.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    transportation = int(input("Is your primary mode of travel by public or private transportation?\n[Enter 0 for public or 1 for private]: "))
    if transportation == 0:
        transportation = 'public'
        print("You entered your primary mode of travel is PUBLIC transportation.")
        break
    elif transportation == 1:
        transportation = 'private'
        print("You entered your primary mode of travel is PRIVATE transportation.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    home_internet_access = input("Do you have internet service in your home?\n[Please enter yes or no]: ")
    if home_internet_access in ["Yes", "YES", "y", "Y", "yes"]:
        home_internet_access = 'y'
        print("You entered you have internet service in your home.")
        break
    elif home_internet_access in ["No", "NO", "n", "N", "no"]:
        home_internet_access = 'n'
        print("You entered you DO NOT have internet service in your home.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    incarceration = input("Have you ever been incarcerated in a City, County, State or Federal jail or prison?\n[Please enter yes or no]: ")
    if incarceration in ["Yes", "YES", "y", "Y", "yes"]:
        incarceration = 'y'
        print("You entered YES you have been incarcerated.")
        break
    elif incarceration in ["No", "NO", "n", "N", "no"]:
        incarceration = 'n'
        print("You entered you HAVE NOT been incarcerated.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    if number_of_children_in_household == 0:
        child_incarceration = 0
        break
    child_incarceration = input("Have any of your children ever been arrested or incarcerated in a City, County, State or Federal jail or prison?[Enter 0 if you do not have children]\n[Please enter yes, no or 0]: ")
    if child_incarceration in ["Yes", "YES", "y", "Y", "yes"]:
        child_incarceration = 'y'
        print("You entered YES you have at least one child who has been incarcerated.")
        break
    elif child_incarceration in ["No", "NO", "n", "N", "no"]:
        child_incarceration = 'n'
        print("You entered you DO NOT have at least one child who has been incarcerated.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    victim_of_crime = input("Have you ever been the victim of a crime?\n[Please enter yes or no]: ")
    if victim_of_crime in ["Yes", "YES", "y", "Y", "yes"]:
        victim_of_crime = 'y'
        print("You entered YES you have been the victim of a crime.")
        break
    elif victim_of_crime in ["No", "NO", "n", "N", "no"]:
        victim_of_crime = 'n'
        print("You entered you HAVE NOT been the victim of a crime.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    if number_of_children_in_household == 0:
        child_victim_of_crime = 0
        break
    child_victim_of_crime = input("Have any of your children ever been the victim of a crime?[Enter 0 if you do not have children]\n[Please enter yes, no or 0]: ")
    if child_victim_of_crime in ["Yes", "YES", "y", "Y", "yes"]:
        child_victim_of_crime = 'y'
        print("You entered YES you have at least one child who has been the victim of a crime.")
        break
    elif child_victim_of_crime in ["No", "NO", "n", "N", "no"]:
        child_victim_of_crime = 'n'
        print("You entered you DO NOT have at least one child who has been the victim of a crime.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    stopped_and_frisked = input("Have you ever been stopped and frisked by police?\n[Please enter yes or no]: ")
    if stopped_and_frisked in ["Yes", "YES", "y", "Y", "yes"]:
        stopped_and_frisked = 'y'
        print("You entered YES you have been stopped and frisked by the police.")
        break
    elif stopped_and_frisked in ["No", "NO", "n", "N", "no"]:
        stopped_and_frisked = 'n'
        print("You entered you HAVE NOT been stopped and frisked by the police.")
        break
    else:
        print("Invalid entry! Please try again.")

s = pd.Series(dtype=str)

s['first_name'] = name
s['gender'] = gender
s['age'] = age
s['race'] = race
s['city'] = input_city
s['state'] = input_state
s['zipcode'] = zipcode
s['number_of_children_in_household'] = number_of_children_in_household
s['other_parent_in_household'] = other_parent_in_household
s['total_household_size'] = total_household_size
s['high_school_or_higher'] = high_school_or_higher
s['employed'] = employed
s['personal_income'] = personal_income
s['homeowner'] = homeowner
s['transportation'] = transportation
s['home_internet_access'] = home_internet_access
s['incarceration'] = incarceration
s['child_incarceration'] = child_incarceration
s['victim_of_crime'] = victim_of_crime
s['child_victim_of_crime'] = child_victim_of_crime
s['stopped_and_frisked'] = stopped_and_frisked

try:
    df = pd.read_csv(wowDataFinal)
except:
    df = pd.DataFrame()

df = df.append(s, ignore_index=True)

df.to_csv(wowDataFinal, mode='w', index=False)

print("The survey is now complete. Thank you for your participation!")
