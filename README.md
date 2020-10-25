# Using Python to conduct a survey by Antwan Bolden
### May 8, 2020

For this project we are taking users' inputs to a survey and adding them to a dataframe. This type of survey can serve many real-world purposes such as aiding city or school officials assessing a districts' priority recipients for emergency resources and the method by which resources would reach these residents in the fastest manner. 

According to [usafacts.org](https://usafacts.org/articles/internet-access-students-at-home/), 4.4 million households with children don’t have consistent access to computers for online learning during the pandemic. The following graph shows the percent of student in households with no internet or computer access by income.

![According to usafacts.org, 4.4 million households with children don’t have consistent access to computers for online learning during the pandemic](https://usafactscms.azureedge.net/media/images/Tech_access_Wst00xE.width-1200.png "Percent of students in households with no internet or computer access by income")

An example usage of this survey could have been implemented in school boards' decisions to close their entire school system in response to COVID-19. Many school distrcits made this decision and presumed every household within the district had access to the necessary resources to replicate the classromm in a mobile environment.

## Explanation of the code

The following libraries were imported:

"import pandas as pd" - used import the vast toolkit that provides numerous tools for data analysis such as data structure and operations for manipulating numerical tables and times series. Pandas is abbreviated as pd as a matter of ease in typing.

"import os" - used to import the miscellaneous operating system interfaces from the os library

"import requests" - allows HTTP requests to be made.

"import json" - JSON is used to covert the python dictionary into a json string that can be written to a file

"import sys" - SYS is a library of system-specific parameters and functions.

## Validating user inputs

### Checking Yes/No inputs

After the intial question, which asks the user to input the user's name, each subsequent question is contolled by a while loop and within each while loop are if/else statements that contol the output (response to user). The first two (2) questions contain a while loop within the while loop that gives the user two (2) attemps to correctly answer the qualifying question. Should user fail to qualify on either question, the system will exit via sys.exit as shown below in Example 1. When a user's input is accepted, the While loop breaks and moves on to the next question.

#### EXAMPLE 1
### Question 2
```
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
 ```

### Validating number inputs

There are 5 questions which require the users to input numbers. To ensure the users' input is a valid number (not a negative number or containing letters, symbols or decimals), we have utlized the function displayed in Example 2. This function is written at the top of code file and given the name 'inputNumber' and it applies to any questions that call that function. The function inputNumber checks that the user inputs an integer. Any acceptable answer is received and the code will break to continue to the next question. Any input that is not an integer returns the error message. The code in Question 4 also returns an error message if the user's input age is not within the inclusice range 18-50.

### EXAMPLE 2
```
def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
            break
        except ValueError :
            print("Invalid entry! Please try again.")

    return userInput
```
### Question 4
```
while True:
    age = inputNumber("Please enter your age: [Age must be a number between 18 and 50]\nPlease enter your age: ")
    if age >= 18 and age <= 50:
        print(f"Great! Your entered your age as {age}, which qualifies for this survey.")
        break
    else:
        print("Invalid entry! Please try again.")
```
## Validating user's zipcode

The user is required to enter the zipcode of residence. Although the zipcode will be an integer, the inputNumber function is not called within this while loop. Instead, the while loop is written to check two things: 1) whether the zipcode is 5 digits in length and 2) if the zipcode is a valid United States zipcode. The zipcode length is checked with if len(zipcode) != 5, thus, if the zipcode length is not exactly 5 digits, the user will be prompted until a valid zipcode is entered. A valid zipcode is determined by calling an api_url and will only be valid upon returning a response code of 200 which is accessed by the import requests above. The user will be greeted with the city, state and zipcode based on the user's input that is stored using datastore. The variables input_city and input_state are generated from the json.loads(response.content) that the requests.get returns as shown in Example 3.
```
# Example 3

API_KEY = "JlfALuS6idZcTt2Cn5Z3FkUEosJSRkpfNnMV58w6PD3T971F0jUPuw087c0orm37"

while True:
  zipcode = input("What is your zip code?\nPlease enter your 5-digit zip code: ")
  if len(zipcode) != 5:
      print('Invalid entry! Please try again.')
      continue

  api_url = "https://www.zipcodeapi.com/rest/" + API_KEY + "/info.json/" + zipcode + "/degrees"

  response = requests.get(api_url)
  if response.status_code == 200:
    break
  print("Invalid entry! Please try again.")

datastore = json.loads(response.content)

input_city = datastore['city']
input_state = datastore['state']

print(f"Great! You live in {input_city}, {input_state} and your zipcode is {zipcode}.")
```
### Coding to output proper is/are response

When probing for number of chidren under 18 in the household, the code will accept any integer. However, the response to user will differ based on the number. If the user indicates the number of chidren is 1, the response to user will be 'You entered there IS 1 child. A response of any integer other than 1 will return the response of 'You entered there ARE n children'. In example 4, the user inputs the number of children. The code checks the input to determine: 1) if the input is valid then proceeds to check the number to determine whether you respond using 'child or children' to correspond with 'is or are'.
```
# Example 4

while True:
    number_of_children_in_household = inputNumber("How many children under 18 years old reside in your household?\n[Please enter a number]: ")
    if number_of_children_in_household < 0:
        print('Invalid entry! Please try again.')
    else:
        if number_of_children_in_household == 1:
            child_or_children = 'child'
            is_or_are = 'is'
        else:
            child_or_children = 'children'
            is_or_are = 'are'
        print(f"You entered there {is_or_are} {number_of_children_in_household} {child_or_children} under 18 years old in your household.")
        break
```
### Skipping a non-applicable question

The follow-up question to number of children in the household asks whether the other parent resides in the household. Since some users will indicate 0 children in the household, it would be unnecessary to ask if the other parent resides in the household as that question would be non-applicable. Therefore, Example 5 shows how the code compares users' input to number of children in household. If number of children in household compares to 0, the other parent in household is marked as 'NaN' in the CSV and the question is skipped. Otherwise, if number of children is 1 or greater, user is then probed for other parent in household. The code is written to where a '0' input to number of children in the household will skip any further questions relating to children in the household.
```
# Example 5 

while True:
    if number_of_children_in_household == 0:
        other_parent_in_household = "NaN"
        break
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
```
