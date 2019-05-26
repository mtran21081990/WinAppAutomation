*** Settings ***
Resource  MainPage_Variables.robot

*** Keywords ***

# Veriify Main Page

Main Page Title Should Be Correct
	Window Title Should Be  ${MAINPAGE_TITLE}

Main Page Content Should Appears
	Verify Label  ${MAINPAGE_HEADER_ID}   ${MAINPAGE_HEADER_TEXT}

Click Main Pape Next Button
	Click Button  ${MAINPAGE_NEXT_ID}

Click On Top Seat View Button
	Click Button  ${MAINPAGE_ORDER_TAB_TOP_SEAT_VIEW_TOGGLEBUTTON}

Click On Botton Seat View Button
	Click Button  ${MAINPAGE_ORDER_TAB_BOTTOM_SEAT_VIEW_TOGGLEBUTTON}

Click On Left Seat View Button
	Click Button  ${MAINPAGE_ORDER_TAB_LEFT_SEAT_VIEW_TOGGLEBUTTON}

Click On Right Seat View Button
	Click Button  ${MAINPAGE_ORDER_TAB_RIGHT_SEAT_VIEW_TOGGLEBUTTON}

Click On Center Seat View Button
	Click Button  ${MAINPAGE_ORDER_TAB_CENTER_SEAT_VIEW_TOGGLEBUTTON}

Select Value In Date Person Combobox
	[Arguments]  ${value}
	Select Combobox Value  ${MAINPAGE_ORDER_TAB_DATE_PERSON_COMBOBOX}  ${value}

Click On Banana Dessert Radio Button
	Select Radio Button  ${MAINPAGE_ORDER_TAB_BANANA_DESSERT_RADIOBUTTON}

Click On Watermelon Dessert Radio Button
	Select Radio Button  ${MAINPAGE_ORDER_TAB_WATERMELON_DESSERT_RADIOBUTTON}

Click On Pinapple Dessert Radio Button
	Select Radio Button  ${MAINPAGE_ORDER_TAB_PINEAPPLE_DESSERT_RADIOBUTTON}

Click On Guava Dessert Radio Button
	Select Radio Button  ${MAINPAGE_ORDER_TAB_GUAVA_DESSERT_RADIOBUTTON}

Click On Mango Dessert Radio Button
	Select Radio Button  ${MAINPAGE_ORDER_TAB_MANGO_DESSERT_RADIOBUTTON}

Click On Orange Dessert Radio Button
	Select Radio Button  ${MAINPAGE_ORDER_TAB_ORANGE_DESSERT_RADIOBUTTON}

Click On Ice Cream Dessert Radio Button
	Select Radio Button  ${MAINPAGE_ORDER_TAB_ICE_CREAM_DESSERT_RADIOBUTTON}

Click On Yaourt Dessert Radio Button
	Select Radio Button  ${MAINPAGE_ORDER_TAB_YAOURT_DESSERT_RADIOBUTTON}

Click On Arrive Late Optional Request Checkbox
	Toggle Check Box  ${MAINPAGE_ORDER_TAB_ARRIVE_LATE_OPTIONAL_REQUESTS_CHECKBOX}

Click On Arrive Early Optional Request Checkbox
	Toggle Check Box  ${MAINPAGE_ORDER_TAB_ARRIVE_EARLY_OPTIONAL_REQUESTS_CHECKBOX}

Click On Need More Seat Optional Request Checkbox
	Toggle Check Box  ${MAINPAGE_ORDER_TAB_MORE_SEAT_OPTIONAL_REQUESTS_CHECKBOX}

Click On Need More Drink Optional Request Checkbox
	Toggle Check Box  ${MAINPAGE_ORDER_TAB_MORE_DRINK_OPTIONAL_REQUESTS_CHECKBOX}

Click On Need More Dishes Optional Request Checkbox
	Toggle Check Box  ${MAINPAGE_ORDER_TAB_MORE_DISHES_OPTIONAL_REQUESTS_CHECKBOX}

Click On Change Date Person Optional Request Checkbox
	Toggle Check Box  ${MAINPAGE_ORDER_TAB_CHANGE_DATE_PERSON_OPTIONAL_REQUESTS_CHECKBOX}

Click On Change Seat View Optional Request Checkbox
	Toggle Check Box  ${MAINPAGE_ORDER_TAB_CHANGE_SEAT_VIEW_OPTIONAL_REQUESTS_CHECKBOX}

Click On Change Dessert Optional Request Checkbox
	Toggle Check Box  ${MAINPAGE_ORDER_TAB_CHANGE_DESSERT_OPTIONAL_REQUESTS_CHECKBOX}

Click On Order Tab
	Select Tab Page  ${MAINPAGE_TABCONTROL}  ${MAINPAGE_ORDER_TAB}

Click On Summary Tab
	Select Tab Page  ${MAINPAGE_TABCONTROL}  ${MAINPAGE_SUMMARY_TAB}
