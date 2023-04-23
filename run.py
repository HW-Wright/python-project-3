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
    print("\nPlease enter an integer below:\n")
    print("How much were you paid after tax this month?\n")

    while True:
        try:
            income = int(input("Enter figure here:\n"))
            break
        except ValueError:
            print("\nData must be entered as an integer.\n")

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
    print(f"\nUpdating {worksheet} sheet...\n")
    updating = SHEET.worksheet(worksheet)
    updating.append_row(data)
    print("Updated.\n")


def living_spending_change():
    """
    Retrive previous month's total, calulate spending difference 
    as a percentage.
    """
    print("\nCalulating change in spending...\n")

    living = SHEET.worksheet("Living").get_all_values()
    living_row = living[-2]
    
    previous_living_total = int(living_row.pop(-1))

    l_spend_change = previous_living_total - int(L_TOTAL)
    l_percentage_change = l_spend_change / previous_living_total * 100
    l_percentage_change_two = round(l_percentage_change, 2)

    print(f"This month, your change in living costs was £{l_spend_change}.\n")
    print(f"That is a change of {l_percentage_change_two}%.\n")

    secondary = SHEET.worksheet("Secondary").get_all_values()
    secondary_row = secondary[-2]

    previous_secondary_total = int(secondary_row.pop(-1))

    s_spend_change = previous_secondary_total - int(S_TOTAL)
    s_percentage_change = s_spend_change / previous_secondary_total * 100
    s_percentage_change_two = round(s_percentage_change, 2)

    print(f"This month, your change in living costs was £{s_spend_change}.\n")
    print(f"That is a change of {s_percentage_change_two}%.\n")
    


def main():
    """
    Function to run all other functions.
    """
    income = get_income()
    update_budget(income, "Income")
    living_costs = get_living_costs()
    update_budget(living_costs, "Living")
    secondary_costs = get_secondary_costs()
    update_budget(secondary_costs, "Secondary")
    living_spending_change()
    


main()