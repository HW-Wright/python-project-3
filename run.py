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

    return [income]



def get_cost_entry(cost_item_name):
    """Get use input for a given cost item.

    Args:
        cost_item_name: str

    Returns:
        int: The user's response as an integer.
    """

    while True:
        user_input = input(
            f"How much did you spend on {cost_item_name.lower()}?\n"
        ).strip()

        if not user_input.isdigit():
            print("Please enter a number.")
            continue
        else:
            return int(user_input)

def get_living_costs():
    """
    Ask the user for their living costs and return them in a list.
    Returns:
        list of int: a list of numbers corresponding to each living cost.
            The total is also appended to the end of the list.
    """
    COST_ITEM_NAMES = [
        'rent',
        'energy',
        'groceries',
        'council tax',
    ] 

    print("\nPlease enter each living cost below as an integer.\n")

    living_costs = []
    for cost_item_name in COST_ITEM_NAMES:
        living_costs.append(
            get_cost_entry(cost_item_name)
        )

    global L_TOTAL
    L_TOTAL = sum(living_costs)

    living_costs.append(sum(living_costs))

    return living_costs

def get_secondary_costs():
    """
    Ask the user for their secondary costs and return them in a list.
    Returns:
        list of int: a list of numbers corresponding to each cost.
            The total is also appended to the end of the list.
    """
    COST_ITEM_NAMES = [
        'car payments',
        'entertainment',
        'social costs',
    ] 

    print("\nPlease enter each secondary cost below as an integer.\n")

    secondary_costs = []
    for cost_item_name in COST_ITEM_NAMES:
        secondary_costs.append(
            get_cost_entry(cost_item_name)
        )

    global S_TOTAL
    S_TOTAL = sum(secondary_costs)

    secondary_costs.append(sum(secondary_costs))

    return secondary_costs


    
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
    print("Calulating change in spending...\n")

    living = SHEET.worksheet("Living").get_all_values()
    living_row = living[-2]
    print(living_row)

    # l_total = []
    # for i in range(4, 4):
    #     data = living.col_values(i)
    #     l_total.append(data[-1:])
        
    # print(l_total)

    # s_total = []



    # print(f"This month your spending difference was {change}% compared to last month")


def main():
    """
    Function to run all other functions.
    """
    # income = get_income()
    # update_budget(income, "Income")
    living_costs = get_living_costs()
    update_budget(living_costs, "Living")
    # secondary_costs = get_secondary_costs()
    # update_budget(secondary_costs, "Secondary")
    show_spending_change()
    


main()