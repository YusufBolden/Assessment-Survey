# Using Python to conduct a survey by Antwan Bolden
### May 8, 2020

For this project we are taking users' inputs to a survey and adding them to a dataframe. This type of survey can serve many real-world purposes such as aiding city or school officials assessing a districts' priority recipients for emergency resources and the method by which resources would reach these residents in the fastest manner. 

According to usafacts.org, 4.4 million households with children don’t have consistent access to computers for online learning during the pandemic. The following graph shows the percent of student in households with no internet or computer access by income.

![According to usafacts.org, 4.4 million households with children don’t have consistent access to computers for online learning during the pandemic](https://usafactscms.azureedge.net/media/images/Tech_access_Wst00xE.width-1200.png "Percent of students in households with no internet or computer access by income")

An example usage of this survey could have been implemented in school boards' decisions to close their entire school system in response to COVID-19. Many school distrcits made this decision and presumed every household within the district had access to the necessary resources to replicate the classromm in a mobile environment.

## Explanation of the code

The following libraries were imported:

"import pandas as pd" - used import the vast toolkit that provides numerous tools for data analysis such as data structure and operations for manipulating numerical tables and times series. Pandas is abbreviated as pd as a matter of ease in typing.

"import os" - used to import the miscellaneous operating system interfaces from the os library

"import requests" - allows HTTP requests to be made.

"import json" - JSON is used to covert the python dictionary into a json string that can be written to a file

"import sys" - SYS is a library of system-specific parameters and functions.

## Using code to validate user inputs

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