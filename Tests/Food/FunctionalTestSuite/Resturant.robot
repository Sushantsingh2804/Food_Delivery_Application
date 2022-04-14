*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${username}  Thalapakatti Biriyani
${password}  6789


*** Test Cases ***
Resaurant Registration
    [Documentation]  Restaurant Registeration details
    [Tags]  Restaurant Registeration
    open Browser  http://127.0.0.1:5000/  chrome
    maximize browser window
    sleep  2s
    click link  xpath:/html/body/div/div/div/div/form/table/tbody/tr[6]/td[2]/a
    sleep  2s
    input text  name:NAME_OF_RESTAURANT  Thalapakatti Biriyani
    sleep  1s
    input text  name:MOBILE_NO  9098909890
    sleep  1s
    input text  name:RESTAURANT_PASSWORD  6789
    sleep  1s
    input text  name:Confirm_PASSWORD  6789
    sleep  1s
    input text  name:ADDRESS  marina,chennai
    sleep  1s
    input text  name:Pincode  600058
    sleep  1s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[9]/td[2]/button

Resaurant login
    [Documentation]  Restaurant Login Details
    [Tags]  Restaurant Login
    sleep  2s
    input text  name:NAME_OF_RESTAURANT  ${username}
    sleep  2s
    input text  name:RESTAURANT_PASSWORD  ${password}
    sleep  2s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[5]/td[2]/button

Menu Add Item
    [Documentation]  Add Item to The Menu
    [Tags]  Add Item
    sleep  2s
    click link  xpath:/html/body/nav/div/div/ul/li[3]/a
    sleep  2s
    input text  name:ITEM_NAME  Chiken-Biriyani
    sleep  2s
    input text  name:ITEM_CATEGORY  Non-Veg
    sleep  2s
    input text  name:ITEM_PRICE  45
    sleep  2s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[5]/td[2]/button
    sleep  4s
    close browser



*** Keywords ***

