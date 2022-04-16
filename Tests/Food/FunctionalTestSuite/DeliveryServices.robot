*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${username}   Akash
${password}   12345

*** Test Cases ***
Delivery Service Registration
    [Documentation]  Delivery boy registeration
    [Tags]  Delivery_boy
    Open Browser  http://127.0.0.1:5000/  chrome
    maximize browser window
    sleep  2s
    click link  xpath:/html/body/div/div/div/div/form/span[3]/a
    sleep  2s
    click link  xpath:/html/body/div/div/div/div/form/table/tbody/tr[6]/td[2]/a
    sleep  2s
    input text  name:NAME_OF_DELIVERYBOY  Akash
    sleep  1s
    input text  name:DELIVERYBOY_PHONE_NO  9176117999
    sleep  1s
    input text  name:DELIVERYBOY_PASSWORD  ${password}
    sleep  1s
    input text  name:confirm_PASSWORD  ${password}
    sleep  1s
    input text  name:ADDRESS  no.4,mullai street,chennai
    sleep  1s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[8]/td[2]/button

Delivery boy login
    [Documentation]  Deliveryboy login
    [Tags]  login_db
    sleep  2s
    input text  name:DELIVERYBOY_NAME  ${username}
    sleep  2s
    input text  name:DELIVERYBOY_PASSWORD  ${password}
    sleep  2s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[5]/td[2]/button
    sleep  2s
    close browser

*** Keywords ***

