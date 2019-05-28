*** Settings ***
Resource  MainPage_Actions.robot

*** Keywords ***

User Should See Main Page Appears
	Main Page Title Should Be Correct
	Main Page Content Should Appears

User Click On Main Page Next Button
	Click Main Pape Next Button

User Can Interact Controls On Main Page
    #Click On Regular Customer Register Button
    Toggle On Top Seat View Toggle Button
    Top Seat View Toggle Button State Is On
    Toggle On Bottom Seat View Toggle Button
    Bottom Seat View Toggle Button State Is On
    Toggle On Left Seat View Toggle Button
    Left Seat View Toggle Button State Is On
    Toggle On Right Seat View Toggle Button
    Right Seat View Toggle Button State Is On
    Toggle On Center Seat View Toggle Button
    Center Seat View Toggle Button State Is On
    Click On Watermelon Dessert Radio Button
    Click On Banana Dessert Radio Button
    Click On Pinapple Dessert Radio Button
    Click On Mango Dessert Radio Button
    Click On Guava Dessert Radio Button
    Click On Orange Dessert Radio Button
    Click On Yaourt Dessert Radio Button
    Click On Ice Cream Dessert Radio Button
    Click On Arrive Late Optional Request Checkbox
    Click On Arrive Early Optional Request Checkbox
    Click On Need More Seat Optional Request Checkbox
    Click On Need More Drink Optional Request Checkbox
    Click On Need More Dishes Optional Request Checkbox
    Click On Change Date Person Optional Request Checkbox
    Click On Change Seat View Optional Request Checkbox
    Click On Change Dessert Optional Request Checkbox
    Click On Summary Tab
    Click On Order Tab
