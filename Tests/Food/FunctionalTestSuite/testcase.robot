*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${username}   9176117999
${password}   12345
${username1}  Thalapakatti Biriyani
${password1}  6789
${username2}  ram@gmail.com
${password2}  123456

*** Test Cases ***
Delivery Service Registration
    [Documentation]  Delivery boy registeration
    [Tags]  Delivery_boy
    Open Browser  file:///C:/Users/Lenovo/PycharmProjects/Food_Delivery_Application/templates/DeliveryBoy_Login.html  chrome
    maximize browser window
    sleep  2s
    click link  xpath:/html/body/div/div/div/div/form/table/tbody/tr[6]/td[2]/a
    sleep  2s
    input text  name:name  Akash
    sleep  1s
    input text  name:mobnumber  9176117999
    sleep  1s
    input text  name:age  ${password}
    sleep  1s
    input text  name:address  ${password}
    sleep  1s
    input text  name:dob  no.4,mullai street,chennai
    sleep  1s
    input text  name:pincode  600077
    sleep  1s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[9]/td[2]/button
    close browser

Delivery boy login
    [Documentation]  Deliveryboy login
    [Tags]  login_db
    open Browser  file:///C:/Users/Lenovo/PycharmProjects/Food_Delivery_Application/templates/DeliveryBoy_Register.html  chrome
    maximize browser window
    sleep  2s
    click link  xpath:/html/body/div/div/div/div/form/table/tbody/tr[10]/td[2]/a
    sleep  2s
    input text  name:username  ${username}
    sleep  2s
    input text  name:password  ${password}
    sleep  2s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[5]/td[2]/button
    close browser

Resaurant Registration
    [Documentation]  Restaurant Registeration details
    [Tags]  Restaurant Registeration
    open Browser  file:///C:/Users/Lenovo/PycharmProjects/Food_Delivery_Application/templates/Resturant_Login.html?_ijt=8j817gosi9nqgi0jkpcvqjm8mq&_ij_reload=RELOAD_ON_SAVE  chrome
    maximize browser window
    sleep  2s
    click link  xpath:/html/body/div/div/div/div/form/table/tbody/tr[6]/td[2]/a
    sleep  2s
    input text  name:name  Thalapakatti Biriyani
    sleep  1s
    input text  name:mobnumber  9098909890
    sleep  1s
    input text  name:age  6789
    sleep  1s
    input text  name:address  6789
    sleep  1s
    input text  name:dob  marina,chennai
    sleep  1s
    input text  name:pincode  600058
    sleep  1s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[9]/td[2]/button
    close browser

Resaurant login
    [Documentation]  Restaurant Login Details
    [Tags]  Restaurant Login
    open browser  file:///C:/Users/Lenovo/PycharmProjects/Food_Delivery_Application/templates/Resturant_Login.html?_ijt=8j817gosi9nqgi0jkpcvqjm8mq&_ij_reload=RELOAD_ON_SAVE  chrome
    maximize browser window
    sleep  2s
    input text  name:username  ${username1}
    sleep  2s
    input text  name:password  ${password1}
    sleep  2s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[5]/td[2]/button
    close browser

User Registration
    [Documentation]  User Registeration details
    [Tags]  User Registeration
    open Browser  file:///C:/Users/Lenovo/PycharmProjects/Food_Delivery_Application/templates/User_login.html  chrome
    maximize browser window
    sleep  2s
    click link  xpath:/html/body/div/div/div/div/form/table/tbody/tr[6]/td[2]/a
    sleep  2s
    input text  name:name  Ram
    sleep  1s
    input text  name:Email  ${username2}
    sleep  1s
    input text  name:mobnumber  9898989898
    sleep  1s
    input text  name:age  ${password2}
    sleep  1s
    input text  name:address  ${password2}
    sleep  1s
    input text  name:dob  chennai
    sleep  1s
    input text  name:pincode  600058
    sleep  1s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[10]/td[2]/button
    close browser

User login
    [Documentation]  Restaurant Login Details
    [Tags]  Restaurant Login
    open browser  file:///C:/Users/Lenovo/PycharmProjects/Food_Delivery_Application/templates/User_Registration.html  chrome
    maximize browser window
    sleep  2s
    click link  xpath:/html/body/div/div/div/div/form/table/tbody/tr[11]/td[2]/a
    sleep  2s
    input text  name:username  ${username2}
    sleep  2s
    input text  name:password  ${password2}
    sleep  2s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[5]/td[2]/button
    close browser

*** Keywords ***

