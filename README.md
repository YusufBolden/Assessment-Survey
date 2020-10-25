# Using Python to conduct a survey - Antwan Bolden and Kevin Campfield

For this project we are taking users' inputs to a survey and adding them to a dataframe. This type of survey can serve many real-world purposes such as aiding city or school officials assessing a districts' priority recipients for emergency resources and the method by which resources would reach these residents in the fastest manner. 

An example usage would have been implemented in a school board's decision to close its entire school system in response to COVID-19. Many school distrcits made this decision and presumed every household within the district had access to the necessary resources to replicate the classromm in a mobile environment.

# Explanation of the code

The following libraries were imported:

"import pandas as pd" - used import the vast toolkit that provides numerous tools for data analysis such as data structure and operations for manipulating numerical tables and times series. Pandas is abbreviated as pd as a matter of ease in typing.

"import os" - used to import the miscellaneous operating system interfaces from the os library

"import requests" - allows HTTP requests to be made.

"import json" - JSON is used to covert the python dictionary into a json string that can be written to a file

"import sys" - SYS is a library of system-specific parameters and functions.

# Using code to validate user inputs

# Checking Yes/No inputs

After the intial question, which asks the user to input the user's name, each subsequent question is contolled by a while loop and within each while loop are if/else statements that contol the output (response to user). The first two (2) questions contain a while loop within the while loop that gives the user two (2) attemps to correctly answer the qualifying question. Should user fail to qualify on either question, the system will exit via sys.exit as shown below in Example 1. When a user's input is accepted, the While loop breaks and moves on to the next question.

# EXAMPLE 1

#Question 2
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