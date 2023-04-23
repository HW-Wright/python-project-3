# Python Monthly Budget
My third portfolio project uses Python code from the run.py file to read, retrive and update data in a Google Sheet. The primary purpose of the project is to both maintain a historical record of the user's spending in various areas, and present the user with an accurate change in spending from the previous month, in the form of a percentage. The program will have obvious use for the majority of people.

[Please view the live project here!]()

## User Experience (UX)
### User Stories
----------------------------
#### First Time User Goals
- As a first time user, I want to easily understand the purpose of the program.
- As a first time user, I want to easily understand how to use the program.
#### Returning User Goals
- As a returning user, I want to be able to use the program with ease and understand what data I am going to receive from it.
#### Frequent User Goals
- As a frequent visitor, I want to use the program to better understand my spending habbits and make any changes that I feel are necessary. 

### Features
----------------------------
#### Existing Features
##### User Inputs
- Eight different inputs request spending data from the user throughout the program. One for the user's income, four for various aspects of the user's living costs, and three for various apects of the user's secondary costs.
##### Google Sheet Updating
- The data from the user inputs are stored in the connected Google Sheet, as well as the totals for each category.
##### Custom Error Messages
- If the user was to enter data the program consider's invalid (such as an input that is not an integer), the program will present custom error messages. These messages will inform the user of the error and repeat the initial input until the data is valid.
##### Change in Spending Data
- The totals for the recently entered data is check against the total for the previous month's data, at which point the difference in pound sterling and percentage change is presented to the user. Thi sis done for both living costs and secondary costs. The user will also be presented a value representing the leftover income for the current month, and how this differs from last month.
#### Features to be Added
- In the future I would like to add a feature whereby users can edit previous entires within the program. This would be a useful feature for combating human error.

### Testing
----------------------------

### UX
----------------------------

### Validators
----------------------------

### Technologies Used
----------------------------

### Deployment
----------------------------

### Credits
----------------------------