# PythonBehaveSel_Ms
A BDD touch with Behave to Python selenium End to end project where both UI and API are covered

# PreRequisites
Python => version in my machine 3.11.5
Pip => Installer for installin the packages
Chromedriver => handled through auto installer [pip install chromedriver-autoinstaller]
IDE of your choice => I used Visual Studio Code

# Reporting
behave html formatter [pip install behave-html-formatter]

# API
Requests => [pip install requests]

# Steps to run the tests: 
# Clone Repositoty using below command
1. git clone https://github.com/muneerashaik14/PythonBehaveSel_Ms.git
2. Open folder in Visual Studio Code OR any IDE of your choice
3. Navigate to Terminal

#Test Execution
1. In Terminal just run "behave" it will run all features
2. For UI Features with behave html Report => behave .\features\caseJudgementUi.feature -f html -o behave-report-ui.html [attached the report in repository for reference]
3. For API Features with behave html Report => behave .\features\caseJudgementApi.feature -f html -o behave-report-api.html [attached the report in repository for reference]

#Sample Report 
<img width="949" alt="SampleReportUI" src="https://github.com/muneerashaik14/PythonBehaveSel_Ms/assets/164380182/b49da56c-cfd8-418f-a3b6-3f41da5fbec4">



