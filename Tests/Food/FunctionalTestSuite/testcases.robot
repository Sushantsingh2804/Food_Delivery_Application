*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${username}  Food-Route
${password}  6789
${email}  ram@gmail.com
${password1}  12345
${username1}  Akash
${password2}  1234
${Go Back}  Execute Javascript history.back()

*** Test Cases ***
1.Resaurant Registration
    [Documentation]  Restaurant Registeration details
    [Tags]  Restaurant Registeration
    open Browser  http://127.0.0.1:5000  chrome
    maximize browser window
    sleep  2s
    click element  xpath:/html/body/div/div/div/div/form/span[1]/a
    sleep  2s
    click link  xpath:/html/body/div/div/div/div/form/table/tbody/tr[6]/td[2]/a
    sleep  2s
    input text  name:NAME_OF_RESTAURANT  Food-Route
    sleep  1s
    input text  name:MOBILE_NO  9098909890
    sleep  1s
    input text  name:RESTAURANT_PASSWORD  6789
    sleep  1s
    input text  name:Confirm_PASSWORD  6789
    sleep  1s
    input text  name:ADDRESS  TRICHY
    sleep  1s
    input text  name:Pincode  600058
    sleep  1s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[9]/td[2]/button
    sleep  1s

2.Resaurant login
    [Documentation]  Restaurant Login Details
    [Tags]  Restaurant Login
    sleep  2s
    input text  name:NAME_OF_RESTAURANT  ${username}
    sleep  2s
    input text  name:RESTAURANT_PASSWORD  ${password}
    sleep  2s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[5]/td[2]/button
    sleep  2s
    click element  xpath:/html/body/nav/div/div/ul/li[3]/a
    sleep  2s
    input text  name:ITEM_NAME  Chicken 65
    sleep  1s
    input text  name:ITEM_CATEGORY  Non Veg
    sleep  1s
    input text  name:ITEM_PRICE  100
    sleep  1s
    input text  name:IMAGE  https://1.bp.blogspot.com/-yJBQwqQcUOs/X5gtEJXEoCI/AAAAAAAAY94/gut_UssF__8lT0P2kl9patf4FY-U4YCtQCLcBGAsYHQ/s2048/chicken%2B65%2B4.JPG
    sleep  1s
    click button  xpath:/html/body/div[1]/div/div/div/form/table/tbody/tr[6]/td[2]/button
    sleep  1s
    click element  xpath:/html/body/div[1]/div/div/div/div/div/a[1]
    sleep  1s
    input text  name:ITEM_PRICE  40
    sleep  1s
    input text  name:IMAGE  https://static.toiimg.com/thumb/54308405.cms?width=1200&height=900
    sleep  1s
    click button  xpath:/html/body/div[1]/div/div/div/form/table/tbody/tr[7]/td[2]/button
    sleep  1s
    click element  xpath:/html/body/div[1]/div/div/div[1]/div/div/a[2]
    sleep  1s
    click element  xpath:/html/body/div[1]/div/div/div/table/tbody/tr[5]/td[2]/a
    sleep  1s
    click element  xpath:/html/body/nav/div/div/ul/li[5]/a
    sleep  2s
    close browser

3.User Registration
    [Documentation]  User Registeration details
    [Tags]  User Registeration
    open Browser  http://127.0.0.1:5000  chrome
    sleep  2s
    click element  xpath:/html/body/div/div/div/div/form/span[2]/a
    sleep  2s
    click link  xpath:/html/body/div/div/div/div/form/table/tbody/tr[6]/td[2]/a
    sleep  2s
    input text  name:USER_NAME  Ram
    sleep  1s
    input text  name:USER_EMAIL  ${email}
    sleep  1s
    input text  name:USER_PHONE_NO  9898989898
    sleep  1s
    input text  name:USER_PASSWORD  ${password1}
    sleep  1s
    input text  name:confirm_PASSWORD  ${password1}
    sleep  1s
    input text  name:ADDRESS  chennai
    sleep  1s
    input text  name:Pincode  600058
    sleep  1s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[10]/td[2]/button

4.User login
    [Documentation]  User Login Details
    [Tags]  User Login
    input text  name:USER_EMAIL  ${email}
    sleep  2s
    input text  name:USER_PASSSWORD  ${password1}
    sleep  2s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[5]/td[2]/button
    sleep  2s

5.Search Restaurant and placing order
     [Documentation]  Search Restaurant and order placing
     [Tags]  To search Restaurant and place order
     click element  xpath:/html/body/nav/div/div/ul/li[2]/a
     sleep  2s
     click element  xpath:/html/body/div[1]/div/div/div/table/tbody/tr[1]/td[5]/a
     sleep  2s
     click element  xpath:/html/body/div[1]/div/div/div[1]/div/div/a
     sleep  2s
     click element  xpath:/html/body/div/div/div/div/table/tbody/tr[5]/td[2]/a
     sleep  2s
     click element  xpath:/html/body/nav/div/div/ul/li[3]/a
     sleep  60s

6.Order Status
     [Documentation]  Order Status in user
     [Tags]  to view status of order
     click element  xpath:/html/body/nav/div/div/ul/li[4]/a
     sleep  2s
     click element  xpath:/html/body/div/div/div/div/table/tbody/tr[1]/td[5]/a
     sleep  2s
     click element  xpath:/html/body/nav/div/div/ul/li[5]/a
     sleep  2s
     close browser

7.Restaurant Order Status
     [Documentation]  Restaurant Order Status
     [Tags]  To view the status of order in restaurant
     open Browser  http://127.0.0.1:5000/Restaurant  chrome
     maximize browser window
     sleep  2s
     input text  name:NAME_OF_RESTAURANT  Continental
     sleep  2s
     input text  name:RESTAURANT_PASSWORD  1234
     sleep  2s
     click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[5]/td[2]/button
     sleep  2s
     click element  xpath:/html/body/nav/div/div/ul/li[4]/a
     sleep  2s
     click element  xpath:/html/body/div/div/div/div/table[1]/tbody/tr[1]/td[5]/a
     sleep  2s
     click element  xpath:/html/body/nav/div/div/ul/li[5]/a
     sleep  2s
     close browser

8.Delivery Service Registration
    [Documentation]  Delivery boy registeration
    [Tags]  Delivery_boy
    Open Browser  http://127.0.0.1:5000  chrome
    maximize browser window
    sleep  2s
    click element  xpath:/html/body/div/div/div/div/form/span[3]/a
    sleep  2s
    click element  xpath:/html/body/div/div/div/div/form/table/tbody/tr[6]/td[2]/a
    sleep  2s
    input text  name:NAME_OF_DELIVERYBOY  Akash
    sleep  1s
    input text  name:DELIVERYBOY_PHONE_NO  9176117999
    sleep  1s
    input text  name:DELIVERYBOY_PASSWORD  ${password2}
    sleep  1s
    input text  name:confirm_PASSWORD  ${password2}
    sleep  1s
    input text  name:ADDRESS  no.4,mullai street,chennai
    sleep  1s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[8]/td[2]/button

9.Delivery boy login
    [Documentation]  Deliveryboy login
    [Tags]  login_db
    sleep  2s
    input text  name:DELIVERYBOY_NAME  ${username1}
    sleep  2s
    input text  name:DELIVERYBOY_PASSWORD  ${password2}
    sleep  2s
    click button  xpath:/html/body/div/div/div/div/form/table/tbody/tr[5]/td[2]/button
    sleep  2s
    close browser

10.Delivery boy status
    [Documentation]  Delivery boy status
    [Tags]  to view order status in delivery boy page
    open Browser  http://127.0.0.1:5000/Delivery  chrome
    maximize browser window
    sleep  2s
    input text  name:DELIVERYBOY_NAME  ${username1}
    sleep  2s
    input text  name:DELIVERYBOY_PASSWORD  ${password2}
    sleep  2s
    click button  xpath:/html/body/div[1]/div/div/div/form/table/tbody/tr[5]/td[2]/button
    sleep  2s
    click element  xpath:/html/body/nav/div/div/ul/li[2]/a
    sleep  2s
    click element  xpath:/html/body/div/div/div/div/table/tbody/tr/td[5]/a
    sleep  2s
    click element  xpath:/html/body/div/div/div/div/table/tbody/tr/td[5]/a
    sleep  2s
    click element  xpath:/html/body/nav/div/div/ul/li[4]/a
    sleep  2s
    close browser

11.Overall Order Status
    [Documentation]  Overall Status
    [Tags]  To view overall order status
     open browser  http://127.0.0.1:5000/User  chrome
     maximize browser window
     input text  name:USER_EMAIL  ${email}
     sleep  2s
     input text  name:USER_PASSSWORD  ${password1}
     sleep  2s
     click button  xpath:/html/body/div[1]/div/div/div/form/table/tbody/tr[5]/td[2]/button
     sleep  2s
     click element  xpath:/html/body/nav/div/div/ul/li[4]/a
     sleep  2s
     click element  xpath:/html/body/div[1]/div/div/div/table/tbody/tr/td[5]/a
     sleep  20s
     close browser
*** Keywords ***