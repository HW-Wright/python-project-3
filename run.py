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
    Get take home income for this month from user
    """
    print("How much were you paid after tax this month?\n")

    income = input("Enter figure here:\n")

    if validate_figures(income):
        print("Thank you")
    
    return income

def validate_figures(value):
    """
    Ensure all inputs are provided as integers, 
    provide error if invalid
    """
    if isinstance(value, int):
        return True
