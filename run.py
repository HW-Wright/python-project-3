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
    print("Please enter an integer below:")
    print("How much were you paid after tax this month?\n")

    while True:
        try:
            income = int(input("Enter figure here:\n"))
            break
        except ValueError:
            print("Data must be entered as an integer.\n")

    return [income]


def get_living_costs():
    """
    Get the total living costs (rent, energy,
    groceries and council tax) as a series of integers
    separated by a comma.
    """
    print("In order of: Rent -> Energy -> Groceries - >Council Tax\nEnter data as integers separated by a comma")
    print("Please enter living costs for this month.\n")
    
    living_str = input("Enter figures here:\n")

    cost_str = living_str.split(",")

    living_costs = [int(i) for i in cost_str]

    if validate_living(living_costs):
        return living_costs
    else:
        get_living_costs()
       


def validate_living(values):
    """
    Convert living costs data into integers.
    """
    try:
        if len(values) != 4:
            raise ValueError(f"Please enter 4 values, not {len(values)}.\n")
    except ValueError as err:
        print(f"Invalid data. {err}\n")
        return False

    return True


    
def update_budget(data, worksheet):
    """
    Used to update the spreadsheet with input data
    from user, in all cases.
    """
    print(f"Updating {worksheet} sheet...\n")
    updating = SHEET.worksheet(worksheet)
    updating.append_row(data)
    print("Updated.\n")


def run_functions():
    """
    Function to run all other functions.
    """
    income = get_income()
    update_budget(income, "Income")
    living_costs = get_living_costs()
    update_budget(living_costs, "Living")


run_functions()