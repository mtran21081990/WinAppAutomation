*** Settings ***
Resource  MainPage_Variables.robot

*** Keywords ***

# Veriify Home Page

Main Page Title Should Be Correct
	Window Title Should Equal To  ${MAINPAGE_ID}  ${MAINPAGE_TITLE}

Main Page Content Should Appears
	Element Text Should Be  ${MAINPAGE_HEADER_ID}   ${MAINPAGE_HEADER_TEXT}

Click Main Pape Next Button
	Click On Button  ${MAINPAGE_NEXT_ID}

Select Drink ListBox Value
	[Arguments]  ${value}
    Select Item On ListBox  ${MAINPAGE_ORDER_TAB_DRINK_LISTBOX}  ${value}

Drink ListBox Value Is
	[Arguments]  ${value}
    ListBox Selection Should Equal To  ${MAINPAGE_ORDER_TAB_DRINK_LISTBOX}  ${value}

Select Dishes ListBox Value
	[Arguments]  ${value}
    Select Item On ListBox  ${MAINPAGE_ORDER_TAB_DISHES_LISTBOX}  ${value}

Dishes ListBox Value Is
	[Arguments]  ${value}
    ListBox Selection Should Equal To  ${MAINPAGE_ORDER_TAB_DISHES_LISTBOX}  ${value}

Click On Top Seat View Button
	Click On Button  ${MAINPAGE_ORDER_TAB_TOP_SEAT_VIEW_TOGGLEBUTTON}

Top Seat View Button Should Be Toggled
	Button Should Be Toggled  ${MAINPAGE_ORDER_TAB_TOP_SEAT_VIEW_TOGGLEBUTTON}

Click On Botton Seat View Button
	Click On Button  ${MAINPAGE_ORDER_TAB_BOTTOM_SEAT_VIEW_TOGGLEBUTTON}

Botton Seat View Button Should Be Toggled
	Button Should Be Toggled  ${MAINPAGE_ORDER_TAB_BOTTOM_SEAT_VIEW_TOGGLEBUTTON}

Click On Left Seat View Button
	Click On Button  ${MAINPAGE_ORDER_TAB_LEFT_SEAT_VIEW_TOGGLEBUTTON}

Left Seat View Button Should Be Toggled
	Button Should Be Toggled  ${MAINPAGE_ORDER_TAB_LEFT_SEAT_VIEW_TOGGLEBUTTON}

Click On Right Seat View Button
	Click On Button  ${MAINPAGE_ORDER_TAB_RIGHT_SEAT_VIEW_TOGGLEBUTTON}

Right Seat View Button Should Be Toggled
	Button Should Be Toggled  ${MAINPAGE_ORDER_TAB_RIGHT_SEAT_VIEW_TOGGLEBUTTON}

Click On Center Seat View Button
	Click On Button  ${MAINPAGE_ORDER_TAB_CENTER_SEAT_VIEW_TOGGLEBUTTON}

Center Seat View Button Should Be Toggled
	Button Should Be Toggled  ${MAINPAGE_ORDER_TAB_CENTER_SEAT_VIEW_TOGGLEBUTTON}

Select Value In Date Person Combobox
	[Arguments]  ${value}
	Select Value On Combobox  ${MAINPAGE_ORDER_TAB_DATE_PERSON_COMBOBOX}  ${value}

Date Person Combobox Selection Should Be
	[Arguments]  ${value}
	Combobox Selection Should Equal To  ${MAINPAGE_ORDER_TAB_DATE_PERSON_COMBOBOX}  ${value}

Click On Banana Dessert Radio Button
	Click On Radio Button  ${MAINPAGE_ORDER_TAB_BANANA_DESSERT_RADIOBUTTON}

Banana Dessert Radio Button Should Be Selected
	Radio Button Should Be Selected  ${MAINPAGE_ORDER_TAB_BANANA_DESSERT_RADIOBUTTON}

Click On Watermelon Dessert Radio Button
	Click On Radio Button  ${MAINPAGE_ORDER_TAB_WATERMELON_DESSERT_RADIOBUTTON}

Watermelon Dessert Radio Button Should Be Selected
	Radio Button Should Be Selected  ${MAINPAGE_ORDER_TAB_WATERMELON_DESSERT_RADIOBUTTON}

Click On Pinapple Dessert Radio Button
	Click On Radio Button  ${MAINPAGE_ORDER_TAB_PINEAPPLE_DESSERT_RADIOBUTTON}

Pinapple Dessert Radio Button Should Be Selected
	Radio Button Should Be Selected  ${MAINPAGE_ORDER_TAB_PINEAPPLE_DESSERT_RADIOBUTTON}

Click On Guava Dessert Radio Button
	Click On Radio Button  ${MAINPAGE_ORDER_TAB_GUAVA_DESSERT_RADIOBUTTON}

Guava Dessert Radio Button Should Be Selected
	Radio Button Should Be Selected  ${MAINPAGE_ORDER_TAB_GUAVA_DESSERT_RADIOBUTTON}

Click On Mango Dessert Radio Button
	Click On Radio Button  ${MAINPAGE_ORDER_TAB_MANGO_DESSERT_RADIOBUTTON}

Mango Dessert Radio Button Should Be Selected
	Radio Button Should Be Selected  ${MAINPAGE_ORDER_TAB_MANGO_DESSERT_RADIOBUTTON}

Click On Orange Dessert Radio Button
	Click On Radio Button  ${MAINPAGE_ORDER_TAB_ORANGE_DESSERT_RADIOBUTTON}

Orange Dessert Radio Button Should Be Selected
	Radio Button Should Be Selected  ${MAINPAGE_ORDER_TAB_ORANGE_DESSERT_RADIOBUTTON}

Click On Ice Cream Dessert Radio Button
	Click On Radio Button  ${MAINPAGE_ORDER_TAB_ICE_CREAM_DESSERT_RADIOBUTTON}

Ice Cream Dessert Radio Button Should Be Selected
	Radio Button Should Be Selected  ${MAINPAGE_ORDER_TAB_ICE_CREAM_DESSERT_RADIOBUTTON}

Click On Yaourt Dessert Radio Button
	Click On Radio Button  ${MAINPAGE_ORDER_TAB_YAOURT_DESSERT_RADIOBUTTON}

Yaourt Dessert Radio Button Should Be Selected
	Radio Button Should Be Selected  ${MAINPAGE_ORDER_TAB_YAOURT_DESSERT_RADIOBUTTON}

Click On Arrive Late Optional Request Checkbox
	Click On Checkbox  ${MAINPAGE_ORDER_TAB_ARRIVE_LATE_OPTIONAL_REQUESTS_CHECKBOX}

Arrive Late Optional Request Checkbox Should Be Checked
	Checkbox Should Be Checked  ${MAINPAGE_ORDER_TAB_ARRIVE_LATE_OPTIONAL_REQUESTS_CHECKBOX}

Click On Arrive Early Optional Request Checkbox
	Click On Checkbox  ${MAINPAGE_ORDER_TAB_ARRIVE_EARLY_OPTIONAL_REQUESTS_CHECKBOX}

Arrive Early Optional Request Checkbox Should Be Checked
	Checkbox Should Be Checked  ${MAINPAGE_ORDER_TAB_ARRIVE_EARLY_OPTIONAL_REQUESTS_CHECKBOX}

Click On Need More Seat Optional Request Checkbox
	Click On Checkbox  ${MAINPAGE_ORDER_TAB_MORE_SEAT_OPTIONAL_REQUESTS_CHECKBOX}

Need More Seat Optional Request Checkbox Should Be Checked
	Checkbox Should Be Checked  ${MAINPAGE_ORDER_TAB_MORE_SEAT_OPTIONAL_REQUESTS_CHECKBOX}

Click On Need More Drink Optional Request Checkbox
	Click On Checkbox  ${MAINPAGE_ORDER_TAB_MORE_DRINK_OPTIONAL_REQUESTS_CHECKBOX}

Need More Drink Optional Request Checkbox Should Be Checked
	Checkbox Should Be Checked  ${MAINPAGE_ORDER_TAB_MORE_DRINK_OPTIONAL_REQUESTS_CHECKBOX}

Click On Need More Dishes Optional Request Checkbox
	Click On Checkbox  ${MAINPAGE_ORDER_TAB_MORE_DISHES_OPTIONAL_REQUESTS_CHECKBOX}

Need More Dishes Optional Request Checkbox Should Be Checked
	Checkbox Should Be Checked  ${MAINPAGE_ORDER_TAB_MORE_DISHES_OPTIONAL_REQUESTS_CHECKBOX}

Click On Change Date Person Optional Request Checkbox
	Click On Checkbox  ${MAINPAGE_ORDER_TAB_CHANGE_DATE_PERSON_OPTIONAL_REQUESTS_CHECKBOX}

Change Date Person Optional Request Checkbox Should Be Checked
	Checkbox Should Be Checked  ${MAINPAGE_ORDER_TAB_CHANGE_DATE_PERSON_OPTIONAL_REQUESTS_CHECKBOX}

Click On Change Seat View Optional Request Checkbox
	Click On Checkbox  ${MAINPAGE_ORDER_TAB_CHANGE_SEAT_VIEW_OPTIONAL_REQUESTS_CHECKBOX}

Change Seat View Optional Request Checkbox Should Be Checked
	Checkbox Should Be Checked  ${MAINPAGE_ORDER_TAB_CHANGE_SEAT_VIEW_OPTIONAL_REQUESTS_CHECKBOX}

Click On Change Dessert Optional Request Checkbox
	Click On Checkbox  ${MAINPAGE_ORDER_TAB_CHANGE_DESSERT_OPTIONAL_REQUESTS_CHECKBOX}

Change Dessert Optional Request Checkbox Should Be Checked
	Checkbox Should Be Checked  ${MAINPAGE_ORDER_TAB_CHANGE_DESSERT_OPTIONAL_REQUESTS_CHECKBOX}

Set Rate Slider Value
	[Arguments]  ${value}
	Set Slider Value  ${MAINPAGE_ORDER_TAB_RATE_SLIDER}  ${value}

Rate Slider Value Should Be
	[Arguments]  ${value}
	Slider Value Should Equal To  ${MAINPAGE_ORDER_TAB_RATE_SLIDER}  ${value}

Click On Order Tab
	Click Element  ${MAINPAGE_ORDER_TAB}

Click On Summary Tab
	Click Element  ${MAINPAGE_SUMMARY_TAB}
