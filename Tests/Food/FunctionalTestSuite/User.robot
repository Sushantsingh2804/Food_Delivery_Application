*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${email}  ram@gmail.com
${password}  123456

*** Test Cases ***
User Registration
    [Documentation]  User Registeration details
    [Tags]  User Registeration
    open Browser  http://127.0.0.1:5000/  chrome
    maximize browser window
    sleep  2s
    click link  xpath:/html/body/div/div/div/div/form/span[2]/a
    sleep  2s
    click link  xpath:/html/body/div/div/div/div/form/table/tbody/tr[6]/td[2]/a
    sleep  2s
    input text  name:USER_NAME  Ram
    sleep  1s
    input text  name:USER_EMAIL  ${email}
    sleep  1s
    input text  name:USER_PHONE_NO  9898989898
    sleep  1s
    input text  name:USER_PASSWORD  ${password}
    sleep  1s
    input text  name:confirm_PASSWORD  ${password}
    sleep  1s
    input text  name:ADDRESS  chennai
    sleep  1s
    input text  name:Pincode  600058
    sleep  1s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[10]/td[2]/button

User login
    [Documentation]  Restaurant Login Details
    [Tags]  Restaurant Login
    sleep  2s
    input text  name:USER_EMAIL  ${email}
    sleep  2s
    input text  name:USER_PASSSWORD  ${password}
    sleep  2s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[5]/td[2]/button
    sleep  2s
    close browser

*** Keywords ***

