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
    Get income for this month from user and ensure data is an integer.
    """
    print("Please enter an integer below:")
    print("How much were you paid after tax this month?\n")

    while True:
        try:
            income = int(input("Enter figure here:\n"))
            print("Thank you.\n")
            break
        except ValueError:
            print("Data must be entered as an integer.\n")

    print([income])
    return [income]
    


def get_living_costs():
    """
    Get the total living costs (rent, energy,
    groceries and council tax) as a series of integers
    separated by a comma.
    """
    print("In order of: Rent -> Energy -> Groceries ->Council Tax\nEnter data as integers separated by a comma")
    print("Please enter living costs for this month.\n")
    while True:
        living_str = input("Enter figures here:\n")
        print("Thank you.\n")
        
        cost_str = living_str.split(",")

        living_costs = [int(i) for i in cost_str]

        if validate_living(living_costs):
            print("Thank you.\n")
            break
        else:
            get_living_costs()

    total = sum(living_costs)

    living_costs.append(total)

    return living_costs
    


def validate_living(values):
    """
    Ensure living cost data is presented as 4 separate integers.
    """
    try:
        if len(values) != 4:
            raise ValueError(f"Please enter 4 values, not {len(values)}.\n")
    except ValueError as err:
        print(f"Invalid data. {err}\n")
        return False

    return True


def get_secondary_costs():
    """
    Get the total secondary costs (Car paymnets, entertainment, social)
    as a series of integers sepparated by a comma.
    """
    print("In order of: Car Payments -> Entertainment -> Social\nEnter data as integers separated by a comma")
    print("Please enter living costs for this month.\n")

    secondary_str = input("Enter figures here:\n")

    sec_str = secondary_str.split(",")

    secondary_costs = [int(i) for i in sec_str]

    if validate_secondary(secondary_costs):
        print("Thank You.")
    else:
        get_secondary_costs()

    total = sum(secondary_costs)

    secondary_costs.append(total)

    return secondary_costs


def validate_secondary(values):
    """
    Ensure secondary cost data is presented as 3 separate integers. 
    """
    try:
        if len(values) != 3:
            raise ValueError(f"Please enter 3 values, not {len(values)}.\n")
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


def show_spending_change():
    """
    Retrive previous month's total, calulate spending difference 
    as a percentage.
    """
    print("calulating change in spending...\n")

    living = SHEET.worksheet("Living")
    # secondary = SHEET.worksheet("Secondary")

    l_total = []
    for i in range(4, 4):
        data = living.col_values(i)
        l_total.append(data[-1:])
        
    print(l_total)

    # s_total = []



    # print(f"This month your spending difference was {change}% compared to last month")


def run_functions():
    """
    Function to run all other functions.
    """
    # income = get_income()
    # update_budget(income, "Income")
    # living_costs = get_living_costs()
    # update_budget(living_costs, "Living")
    # secondary_costs = get_secondary_costs()
    # update_budget(secondary_costs, "Secondary")
    show_spending_change()


run_functions()