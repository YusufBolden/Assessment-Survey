import pandas as pd
import seaborn as sns
import questionary
import sys


print("Welcome to the Python WOW of Kevin Campfield and Yusuf Bolden. For this")
print("project we are taking a users' inputs to a survey and adding them to a dataframe")
print("that can be distributed by city and school officials at the beginning of each year")
print("to create a database with the information which can then be used to")
print("determine the residents and students who should be listed as priority")
print("recipients for emergency resources and the method by which")
print("resources would reach these residents in the fastest manner.\n")
print("The following information is collected for statistical purposes and")
print("will not be published, distributed or otherwise sold to any third party.\n")
print("You must be a New York City resident between the ages of 18-50 to complete")
print("this survey. A New York City resident is anyone who resides within the")
print("5 boroughs of Brooklyn, Bronx, Manhattan, Queens and Staten Island.\n")
print("This survey consists of 20 questions. The estimated time to complete this survey is 10 minutes.")
print("Please take your time reading and answering each question. You will not be able to change your answers.\n")

name = input("What is your first name?\nPlease enter your name: ")
print("Welcome", name.title())

while True:
    nycResident = input("Are you a resident of New York City?\n[Please enter Yes or No]: ")
    if nycResident in ["Yes", "YES", "y", "Y", "yes"]:
        print("Great! You are a New York City resident.")
        break
    elif nycResident in ["No", "NO", "n", "N", "no"]:
        print("Sorry! This survey is only for New York City residents.")
        while True:
            nycResident = input("Are you a resident of New York City?\n[Please enter Yes or No]: ")
            if nycResident in ["Yes", "YES", "y", "Y", "yes"]:
                print("Great! You are a New York City Resident")
                break
            elif nycResident in ["No", "NO", "n", "N", "no"]:
                sys.exit("Sorry! This survey is only for New York City residents. Thanks for trying.")
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
        print("You entered Male")
        break
    elif gender in ["F", "f", "FEMALE", "Female", "female"]:
        print("You entered Female")
        break
    elif gender in ["O", "o", "OTHER", "Other", "other"]:
        print("You entered Other")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    age = int(input("Please enter your age: [Age must be between 18 and 50]\nPlease enter your age: "))
    if age >= 18 and age <= 50:
        print(f"Great! Your age is {age}, which is within the correct range.")
        break
        while True:
            age = int(input("Please enter your age:[Age must be between 18 and 50]\nPlease enter your age: "))
            if age >= 18 and age <= 50:
                print(f"Great! Your age is {age}, which is within the correct range.")
                break
            elif age < 18 or age > 50:
                sys.exit("Sorry! This survey is only for persons between the ages of 18 and 50. Thank you for trying.")
            else:
                print("Invalid entry! Please try again.")
        break
    elif age < 18 and age > 50:
        print("Entry is not within age range! Please try again.")
    else:
        print("Invalid entry! Please try again.")

while True:
    race = input("Which of the following best describes your race or ethnicity?\n[Please enter White, Black, Hispanic, Asian, Native American, Mixed or Other]: ")
    if race in ["WHITE", "White", "white", "BLACK", "Black", "black",
                "HISPANIC", "Hispanic", "hispanic", "ASIAN", "Asian", "asian",
                "NATIVE AMERICAN", "Native American", "native american", "MIXED", "Mixed", "mixed",
                "OTHER", "Other", "other"]:
        print("Great! You listed your race as", race.title())
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    borough = input("In which borough do you reside:\n[Please enter Bronx, Brooklyn, Manhattan, Queens or Staten Island]: ")
    if borough in ["Bronx", "bronx", "BX", "Bx", "bx", "Brooklyn",
                "brooklyn", "BKLYN", "Bklyn", "bklyn", "BK", "bk", "MANHATTAN",
                "Manhattan", "manhattan", "QUEENS", "Queens", "queens",
                "STATEN ISLAND", "staten island", "Staten Island\n"]:
        print("Great. You live in", borough.title())
        break
        while True:
            if borough in ["Bronx", "bronx", "BX", "Bx", "bx", "Brooklyn",
                    "brooklyn", "BKLYN", "Bklyn", "bklyn", "BK", "bk", "MANHATTAN",
                    "Manhattan", "manhattan", "QUEENS", "Queens", "queens",
                    "STATEN ISLAND", "staten island", "Staten Island\n"]:
                print("Great. You live in", borough.title())
            break
        else:
            sys.exit("Sorry! You must reside in Bronx, Brooklyn, Manhattan, Queens or Staten Island to complete this survey. Thank you for trying.")
        break
    else:
        print("You must reside in Bronx, Brooklyn, Manhattan, Queens or Staten Island to complete this survey.")

while True:
    zipcode_Bronx = [10451, 10452, 10453, 10454, 10455, 10456, 10457, 10458, 10459,
                    10460, 10461, 10462, 10463, 10464, 10465, 10466, 10467, 10468,
                    10469, 10470, 10471, 10472, 10473, 10474, 10475]

    zipcode_Brooklyn = [11212, 11213, 11216, 11233, 11238, 11209, 11214, 11228,
                        11204, 11218, 11219, 11230, 11234, 11236, 11239, 11223,
                        11224, 11229, 11235, 11201, 11205, 11215, 11217, 11231,
                        11203, 11210, 11225, 11226, 11207, 11208, 11211, 11222,
                        11220, 11232, 11206, 11221, 11237]

    zipcode_Manhattan = [10026, 10027, 10030, 10037, 10039, 10001, 10011, 10018,
                        10019, 10020, 10036, 10029, 10035, 10010, 10016, 10017,
                        10022, 10012, 10013, 10014, 10004, 10005, 10006, 10007,
                        10038, 10280, 10002, 10003, 10009, 10021, 10028, 10044,
                        10065, 10075, 10128, 10023, 10024, 10025]

    zipcode_Queens = [11361, 11362, 11363, 11364, 11354, 11355, 11356, 11357,
                      11358, 11359, 11360, 11365, 11366, 11367, 11412, 11423,
                      11101, 11102, 11103, 11104, 11105, 11106, 11374, 11375,
                      11379, 11385, 11691, 11692, 11693, 11694, 11695, 11697,
                      11004, 11005, 11411, 11413, 11422, 11426, 11427, 11428,
                      11429, 11414, 11415, 11416, 11417, 11418, 11419, 11420,
                      11421, 11368, 11369, 11370, 11372, 11373, 11377, 11378]

    zipcode_StatenIsland = [10301, 10302, 10303, 10304, 10305, 10306, 10307,
                            10308, 10309, 10310, 10312, 10314]

    zipcode = int(input("What is your zip code?\nPlease enter your zip code: "))
    if borough in ["BRONX", "Bronx", "bronx", "BX", "Bx", "bx"] and zipcode in zipcode_Bronx:
        print(f"Great! You live in {borough.title()} and your zipcode is {zipcode}.")
        break
    elif borough in ["BROOKLYN", "Brooklyn", "brooklyn", "BKLYN", "Bklyn", "bklyn", "BK", "Bk", "bk"] and zipcode in zipcode_Brooklyn:
        print(f"Great! You live in {borough.title()} and your zipcode is {zipcode}.")
        break
    elif borough in ["MANHATTAN", "Manhattan", "manhattan"] and zipcode in zipcode_Manhattan:
        print(f"Great! You live in {borough.title()} and your zipcode is {zipcode}.")
        break
    elif borough in ["QUEENS", "Queens", "queens"] and zipcode in zipcode_Queens:
        print(f"Great! You live in {borough.title()} and your zipcode is {zipcode}.")
        break
    elif borough in ["STATEN ISLAND", "staten island", "Staten Island"] and zipcode in zipcode_StatenIsland:
        print(f"Great! You live in {borough.title()} and your zipcode is {zipcode}.")
        break
    else:
        print("Borough and zip code do not match. Please enter a valid Borough and zip code combination")

while True:
    number_of_chidren_in_household = int(input("How many children under 18 years' old reside in your household?\n[Please enter a number]: "))
    if number_of_chidren_in_household == 0:
        print(f"You entered there are {number_of_chidren_in_household} children under 18 years' old in your household.")
        break
        while True:
            other_parent_in_household = int(input("Does the other parent of your children reside in the household?\n[Enter 0 for NO and 1 for YES]: "))
            if other_parent_in_household == 0:
                print("You entered the other parent DOES NOT live in the household")
                break
            elif other_parent_in_household == 1:
                print("You entered the other parent DOES live in the household")
                break
            else:
                print("Invalid entry! Please try again.")
        break
    elif number_of_chidren_in_household == 1:
        print(f"You entered there is {number_of_chidren_in_household} child under 18 years' old in your household.")
        break
    elif number_of_chidren_in_household > 1:
        print(f"You entered there are {number_of_chidren_in_household} children under 18 years' old in your household.")
        break
    else:
        print("Invalid entry. Please try again.")

while True:
    total_household_size = int(input("Including yourself, how many persons reside in your household?\n[Please enter a number]: "))
    if total_household_size == 0:
        print("Invalid entry! Total household size must be greater than 0.")
    elif total_household_size > 0:
        print(f"Your entered your total_household_size is {total_household_size}.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    high_school_or_higher = input("Did you receive your high school diploma or high school equivalency such as a GED?\n[Please enter yes or no]: ")
    if high_school_or_higher in ["Yes", "YES", "y", "Y", "yes"]:
        print("Great! You are a high school graduate.")
        break
    elif high_school_or_higher in ["No", "NO", "n", "N", "no"]:
        print("You entered you DID NOT graduate high school or obtain a high school equivalency.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    employed = input("Are you currently employed either full-time or part-time?\n[Please enter yes or no]: ")
    if employed in ["Yes", "YES", "y", "Y", "yes"]:
        print("Great! You are currently employed.")
        break
    elif employed in ["No", "NO", "n", "N", "no"]:
        print("You entered you ARE NOT currently employed.")
        break
    else:
        print("Invalid entry! Please try again.")
while True:
    personal_income = int(input("Which range best describes your current personal income?\n[Please enter 1 for less than 15,000, 2 for 15,000 to 20,000, 3 for 20,001 to 35,000, 4 for 35,001 to 50,000, or 5 for more than 50,000]\n[Please enter number than identifes your current income]: "))
    if personal_income == 1:
        print("You entered your current income is less than $15,000.")
        break
    elif personal_income == 2:
        print("You entered your current income is between $15,001 and $20,000.")
        break
    elif personal_income == 3:
        print("You entered your current income is between $20,001 and $35,000.")
        break
    elif personal_income == 4:
        print("You entered your current income is between $35,001 and $50,000.")
        break
    elif personal_income == 5:
        print("You entered your current income is greater than $50,000.")
        break
    else:
        print("Invalid entry! Please enter a number from 1 to 5 than represents your current personal income.")

while True:
    homeowner = input("Do you own your home?\n[Please enter yes or no]: ")
    if homeowner in ["Yes", "YES", "y", "Y", "yes"]:
        print("You entered that you own your home.")
        break
    elif homeowner in ["No", "NO", "n", "N", "no"]:
        print("You entered you DO NOT own your home.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    transportation = input("Is your primary mode of travel by public or private transportation?\n[Please enter public or private]: ")
    if transportation in ["PUBLIC", "Public", "public"]:
        print("You entered your primary mode of travel is public transportation.")
        break
    elif transportation in ["PRIVATE", "Private", "private"]:
        print("You entered your primary mode of travel is public transportation.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    home_internet_access = input("Do you have internet service in your home?\n[Please enter yes or no]: ")
    if home_internet_access in ["Yes", "YES", "y", "Y", "yes"]:
        print("You entered you have internet service in your home.")
        break
    elif home_internet_access in ["No", "NO", "n", "N", "no"]:
        print("You entered you DO NOT have internet service in your home.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    incarceration = input("Have you ever been incarcerated in a City, County, State or Federal jail or prison?\n[Please enter yes or no]: ")
    if incarceration in ["Yes", "YES", "y", "Y", "yes"]:
        print("You entered YES you have been incarcerated.")
        break
    elif incarceration in ["No", "NO", "n", "N", "no"]:
        print("You entered you HAVE NOT been incarcerated.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    child_incarceration = input("Have any of your children ever been arrested or incarcerated in a City, County, State or Federal jail or prison?[Enter 0 if you do not have children]\n[Please enter yes, no or 0]: ")
    if child_incarceration in ["Yes", "YES", "y", "Y", "yes"]:
        print("You entered YES you have at least one child who has been incarcerated.")
        break
    elif child_incarceration in ["No", "NO", "n", "N", "no"]:
        print("You entered you DO NOT have at least one child who has been incarcerated.")
        break
    elif child_incarceration in ["0"]:
        print("You have skipped this question because you DO NOT have children.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    victim_of_crime = input("Have you ever been the victim of a crime?\n[Please enter yes or no]: ")
    if victim_of_crime in ["Yes", "YES", "y", "Y", "yes"]:
        print("You entered YES you have been the victim of a crime.")
        break
    elif victim_of_crime in ["No", "NO", "n", "N", "no"]:
        print("You entered you HAVE NOT been the victim of a crime.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    child_victim_of_crime = input("Have any of your children ever been the victim of a crime?[Enter 0 if you do not have children]\n[Please enter yes, no or 0]: ")
    if child_victim_of_crime in ["Yes", "YES", "y", "Y", "yes"]:
        print("You entered YES you have at least one child who has been the victim of a crime.")
        break
    elif child_victim_of_crime in ["No", "NO", "n", "N", "no"]:
        print("You entered you DO NOT have at least one child who has been the victim of a crime.")
        break
    elif child_victim_of_crime in ["0"]:
        print("You have skipped this question because you DO NOT have children.")
        break
    else:
        print("Invalid entry! Please try again.")

while True:
    stopped_and_frisked = input("Have you ever been stopped and frisked by police?\n[Please enter yes or no]: ")
    if stopped_and_frisked in ["Yes", "YES", "y", "Y", "yes"]:
        print("You entered YES you have been stopped and frisked by the police.")
        break
    elif stopped_and_frisked in ["No", "NO", "n", "N", "no"]:
        print("You entered you HAVE NOT been stopped and frisked by the police.")
        break
    else:
        print("Invalid entry! Please try again.")

print("The survey is now complete. Thank you for your participation!")
