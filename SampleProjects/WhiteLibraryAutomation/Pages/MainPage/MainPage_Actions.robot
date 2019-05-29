*** Settings ***
Resource  MainPage_Variables.robot
Library  DateTime

*** Keywords ***

# Veriify Main Page

Main Page Title Should Be Correct
	Window Title Should Be  ${MAINPAGE_TITLE}

Main Page Content Should Appears
	Label Text Should Be  ${MAINPAGE_HEADER_ID}   ${MAINPAGE_HEADER_TEXT}

Click Main Pape Next Button
	Click Button  ${MAINPAGE_NEXT_ID}

Click Main Pape Menu
	Click Menu Button  text=Menu 1  Item 2  Sub Item 3  Sub Sub Item 1

Select Item In Drink List Box
	[Arguments]  ${value}
    Select ListBox Value  ${MAINPAGE_ORDER_TAB_DRINK_LISTBOX}  ${value}

Drink List Box Selection Should Be
	[Arguments]  @{value}
    ListBox Selection Should Be  ${MAINPAGE_ORDER_TAB_DRINK_LISTBOX}  @{value}

Select Item In Dishes List Box
	[Arguments]  ${value}
    Select ListBox Value  ${MAINPAGE_ORDER_TAB_DISHES_LISTBOX}  ${value}

Dishes List Box Selection Should Be
	[Arguments]  @{value}
    ListBox Selection Should Be  ${MAINPAGE_ORDER_TAB_DISHES_LISTBOX}  @{value}

Toggle On Top Seat View Toggle Button
	Toggle Button  ${MAINPAGE_ORDER_TAB_TOP_SEAT_VIEW_TOGGLEBUTTON}

Top Seat View Toggle Button State Is On
	Toggle Button Should Be On  ${MAINPAGE_ORDER_TAB_TOP_SEAT_VIEW_TOGGLEBUTTON}

Toggle On Bottom Seat View Toggle Button
	Toggle Button  ${MAINPAGE_ORDER_TAB_BOTTOM_SEAT_VIEW_TOGGLEBUTTON}

Bottom Seat View Toggle Button State Is On
	Toggle Button Should Be On  ${MAINPAGE_ORDER_TAB_BOTTOM_SEAT_VIEW_TOGGLEBUTTON}

Toggle On Left Seat View Toggle Button
	Toggle Button  ${MAINPAGE_ORDER_TAB_LEFT_SEAT_VIEW_TOGGLEBUTTON}

Left Seat View Toggle Button State Is On
	Toggle Button Should Be On  ${MAINPAGE_ORDER_TAB_LEFT_SEAT_VIEW_TOGGLEBUTTON}

Toggle On Right Seat View Toggle Button
	Toggle Button  ${MAINPAGE_ORDER_TAB_RIGHT_SEAT_VIEW_TOGGLEBUTTON}

Right Seat View Toggle Button State Is On
	Toggle Button Should Be On  ${MAINPAGE_ORDER_TAB_RIGHT_SEAT_VIEW_TOGGLEBUTTON}

Toggle On Center Seat View Toggle Button
	Toggle Button  ${MAINPAGE_ORDER_TAB_CENTER_SEAT_VIEW_TOGGLEBUTTON}

Center Seat View Toggle Button State Is On
	Toggle Button Should Be On  ${MAINPAGE_ORDER_TAB_CENTER_SEAT_VIEW_TOGGLEBUTTON}

Select Value In Date Person Combobox
	[Arguments]  ${value}
	Select Combobox Value  ${MAINPAGE_ORDER_TAB_DATE_PERSON_COMBOBOX}  ${value}

Date Person Combobox Selection Value Should Be
	[Arguments]  ${value}
	Verify Combobox Selection  ${MAINPAGE_ORDER_TAB_DATE_PERSON_COMBOBOX}  ${value}

Click On Banana Dessert Radio Button
	Click Radio Button Text  ${MAINPAGE_ORDER_TAB_BANANA_DESSERT_RADIOBUTTON}

Click On Watermelon Dessert Radio Button
	Click Radio Button Text  ${MAINPAGE_ORDER_TAB_WATERMELON_DESSERT_RADIOBUTTON}

Click On Pinapple Dessert Radio Button
	Click Radio Button Text  ${MAINPAGE_ORDER_TAB_PINEAPPLE_DESSERT_RADIOBUTTON}

Click On Guava Dessert Radio Button
	Click Radio Button Text  ${MAINPAGE_ORDER_TAB_GUAVA_DESSERT_RADIOBUTTON}

Click On Mango Dessert Radio Button
	Click Radio Button Text  ${MAINPAGE_ORDER_TAB_MANGO_DESSERT_RADIOBUTTON}

Click On Orange Dessert Radio Button
	Click Radio Button Text  ${MAINPAGE_ORDER_TAB_ORANGE_DESSERT_RADIOBUTTON}

Click On Ice Cream Dessert Radio Button
	Click Radio Button Text  ${MAINPAGE_ORDER_TAB_ICE_CREAM_DESSERT_RADIOBUTTON}

Click On Yaourt Dessert Radio Button
	Click Radio Button Text  ${MAINPAGE_ORDER_TAB_YAOURT_DESSERT_RADIOBUTTON}

Click On Arrive Late Optional Request Checkbox
	Click Check Box Text  ${MAINPAGE_ORDER_TAB_ARRIVE_LATE_OPTIONAL_REQUESTS_CHECKBOX}

Click On Arrive Early Optional Request Checkbox
	Click Check Box Text  ${MAINPAGE_ORDER_TAB_ARRIVE_EARLY_OPTIONAL_REQUESTS_CHECKBOX}

Click On Need More Seat Optional Request Checkbox
	Click Check Box Text  ${MAINPAGE_ORDER_TAB_MORE_SEAT_OPTIONAL_REQUESTS_CHECKBOX}

Click On Need More Drink Optional Request Checkbox
	Click Check Box Text  ${MAINPAGE_ORDER_TAB_MORE_DRINK_OPTIONAL_REQUESTS_CHECKBOX}

Click On Need More Dishes Optional Request Checkbox
	Click Check Box Text  ${MAINPAGE_ORDER_TAB_MORE_DISHES_OPTIONAL_REQUESTS_CHECKBOX}

Click On Change Date Person Optional Request Checkbox
	Click Check Box Text  ${MAINPAGE_ORDER_TAB_CHANGE_DATE_PERSON_OPTIONAL_REQUESTS_CHECKBOX}

Click On Change Seat View Optional Request Checkbox
	Click Check Box Text  ${MAINPAGE_ORDER_TAB_CHANGE_SEAT_VIEW_OPTIONAL_REQUESTS_CHECKBOX}

Click On Change Dessert Optional Request Checkbox
	Click Check Box Text  ${MAINPAGE_ORDER_TAB_CHANGE_DESSERT_OPTIONAL_REQUESTS_CHECKBOX}

Click On Order Tab
	Select Tab Page By Title  ${MAINPAGE_TABCONTROL}  ${MAINPAGE_ORDER_TAB}

Order Tab Is Selected
	Selected Tab Page Should Be  ${MAINPAGE_TABCONTROL}  ${MAINPAGE_ORDER_TAB}

Click On Summary Tab
	Select Tab Page By Title  ${MAINPAGE_TABCONTROL}  ${MAINPAGE_SUMMARY_TAB}

Summary Tab Is Selected
	Selected Tab Page Should Be  ${MAINPAGE_TABCONTROL}  ${MAINPAGE_SUMMARY_TAB}

Click On Regular Customer Register Button
	Click Button  ${MAINPAGE_ORDER_TAB_REGULAR_CUSTOMER_REGISTER_BUTTON}

Set Rate Slider Value
	[Arguments]  ${value}
    Set Slider Value  ${MAINPAGE_ORDER_TAB_RATE_SLIDER}  ${value}

Rate Slider Value Should Be
	[Arguments]  ${value}
    Verify Slider Value  ${MAINPAGE_ORDER_TAB_RATE_SLIDER}  ${value}

#Select Available Date Calendar
#    ${date} =	Convert Date	2019-05-30
#    Set Datetime Picker  ${MAINPAGE_ORDER_TAB_AVAILABLE_DATE_CALENDAR}  ${date}


