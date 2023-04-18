import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('monthly-budget')

def get_income():
    """
    Get take home income for this month from user.
    """
    print("How much were you paid after tax this month?\n")

    income = int(input("Enter figure here:\n"))

    if validate_income(income):
        print("Thank you.\n")
    
    return income


# def get_living_costs():
#     """
#     Get the total living costs (rent, energy,
#     groceries and council tax) as a series of integers
#     separated by a comma
#     """
#     print("Please enter living costs for this month.\n")
#     print("In order of: Rent->Energy->Groceries->Council Tax\nEmter data as integers separated by a comma")
    
#     living_costs = input("Enter figures here:\n")

#     if validate_living(living_costs):
#         print("Thank you")
#         break

#     return living_costs


def validate_income(value):
    """
    Ensure income data is provided as integers, 
    provide error if invalid.
    """
    if isinstance(value, int):
        return True


# def validate_living(value):
#     """
#     Convert data into integers
#     """
    


def update_budget(data, worksheet):
    """
    Used to update the spreadsheet with input data
    from user, in all cases.
    """
    print(f"Updating {worksheet} budget...\n")
    data = [data]
    updating = SHEET.worksheet(worksheet)
    updating.append_row(data)
    print("Updated.\n")


def run_functions():
    """
    Function to run all other functions.
    """
    income = get_income()
    update_budget(income, "Income")
    # living_costs = get_living_costs()
    # update_budget(living_costs, "Living")


run_functions()