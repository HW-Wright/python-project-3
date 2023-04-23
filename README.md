# Python Monthly Budget
My third portfolio project uses Python code from the run.py file to read, retrieve and update data in a Google Sheet. The primary purpose of the project is to both maintain a historical record of the user's spending in various areas and present the user with an accurate change in spending from the previous month, in the form of a percentage. The program will have obvious use for the majority of people.

[Please view the live project here!](https://python-project-3.herokuapp.com/)

[Please find the Google Sheet here:](https://docs.google.com/spreadsheets/d/1H_ye3MRzxCeTJMHI1Xxri35Bqf9PdojsFB4kVQnV9h8/edit#gid=438650178)

![Deployed Webb App](/documentation/deployed-project.png)

## User Experience (UX)
### User Stories
----------------------------
#### First Time User Goals
- As a first time user, I want to easily understand the purpose of the program.
- As a first time user, I want to easily understand how to use the program.
#### Returning User Goals
- As a returning user, I want to be able to use the program with ease and understand what data I am going to receive from it.
#### Frequent User Goals
- As a frequent visitor, I want to use the program to better understand my spending habits and make any changes that I feel are necessary. 

### Features
----------------------------
#### Existing Features
##### User Inputs
- Eight different inputs request spending data from the user throughout the program. One for the user's income, four for various aspects of the user's living costs, and three for various aspects of the user's secondary costs.
##### Google Sheet Updating
- The data from the user inputs are stored in the connected Google Sheet, as well as the totals for each category.
##### Custom Error Messages
- If the user was to enter data the program considers invalid (such as an input that is not an integer), the program will present custom error messages. These messages will inform the user of the error and repeat the initial input until the data is valid.
##### Change in Spending Data
- The totals for the recently entered data is check against the total for the previous month's data, at which point the difference in pound sterling and percentage change is presented to the user. This is done for both living costs and secondary costs. The user will also be presented a value representing the leftover income for the current month, and how this differs from last month.
#### Features to be Added
- In the future I would like to add a feature whereby users can edit previous entries within the program. This would be a useful feature for combating human error.

### Testing
----------------------------
- The app has been tested rigorously in the gitpod terminal, and in it's deployed form on Heroku.
![Testing in terminal](/documentation/testing-1.png)
![Testing in terminal](/documentation/testing-2.png)
![Testing in terminal](/documentation/testing-3.png)
![Testing criteria](/documentation/testing-4.png)
### UI
----------------------------
- It was important to the project, that the limited control I had over the design of the deployed app, was made to be as clean and polished as possible. As a result, the inputs and print statements that make up the UX of the app are all evenly separated, with the living cost group and the secondary cost group of inputs remaining together.

### Validators
----------------------------
- The run.py file was put through a validator, please see below:
![Code validation](/documentation/code-validation.png)

### Technologies Used
----------------------------
- Python
- Google Sheets
- Google Webb API's
- Heroku

### Deployment
----------------------------
- Using Heroku, the web app was deployed via GitHub.
![Heroku Deployment](/documentation/heroku-deployment.png)
- Below are the config vars used:
![Heroku Config Vars](/documentation/config-vars.png)
- Below are the buildpacks necessary to create the web app:
![Heroku Buildpacks](/documentation/buildpacks.png)

### Credits
----------------------------
- Update_budget function: The basic code structure is borrowed from the Love Sandwiches walkthrough project.
- I would like to acknowledge Brian Macharia, my Code Institute mentor. The student support systems at Code Institute.