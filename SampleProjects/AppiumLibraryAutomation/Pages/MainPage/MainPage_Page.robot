*** Settings ***
Resource  MainPage_Actions.robot

*** Keywords ***

User Should See Main Page Appears
	Main Page Title Should Be Correct
	Main Page Content Should Appears

User Click On Main Page Next Button
	Click Main Pape Next Button

User Can Interact Controls On Main Page
#    Select Drink ListBox Value  Ice Coffee
#    Drink ListBox Value Is  Ice Coffee
#    Select Drink ListBox Value  Hot Coffee
#    Drink ListBox Value Is  Hot Coffee
#    Select Drink ListBox Value  Banana Smoothy
#    Drink ListBox Value Is  Banana Smoothy
    Select Dishes ListBox Value  Ham Sandwich
    Dishes ListBox Value Is  Ham Sandwich
    Select Dishes ListBox Value  Pizza
    Dishes ListBox Value Is  Ham Sandwich, Pizza
    Select Dishes ListBox Value  Hamburger
    Dishes ListBox Value Is  Ham Sandwich, Pizza, Hamburger
#    Click On Top Seat View Button
#    Top Seat View Button Should Be Toggled
#    Click On Botton Seat View Button
#    Botton Seat View Button Should Be Toggled
#    Click On Left Seat View Button
#    Left Seat View Button Should Be Toggled
#    Click On Right Seat View Button
#    Right Seat View Button Should Be Toggled
#    Click On Center Seat View Button
#    Center Seat View Button Should Be Toggled
#    Select Value In Date Person Combobox  Tom Cruise
#    Date Person Combobox Selection Should Be  Tom Cruise
#    Click On Watermelon Dessert Radio Button
#    Watermelon Dessert Radio Button Should Be Selected
#    Click On Banana Dessert Radio Button
#    Banana Dessert Radio Button Should Be Selected
#    Click On Pinapple Dessert Radio Button
#    Pinapple Dessert Radio Button Should Be Selected
#    Click On Mango Dessert Radio Button
#    Mango Dessert Radio Button Should Be Selected
#    Click On Guava Dessert Radio Button
#    Guava Dessert Radio Button Should Be Selected
#    Click On Orange Dessert Radio Button
#    Orange Dessert Radio Button Should Be Selected
#    Click On Yaourt Dessert Radio Button
#    Yaourt Dessert Radio Button Should Be Selected
#    Click On Ice Cream Dessert Radio Button
#    Ice Cream Dessert Radio Button Should Be Selected
#    Click On Arrive Late Optional Request Checkbox
#    Arrive Late Optional Request Checkbox Should Be Checked
#    Click On Arrive Early Optional Request Checkbox
#    Arrive Early Optional Request Checkbox Should Be Checked
#    Click On Need More Seat Optional Request Checkbox
#    Need More Seat Optional Request Checkbox Should Be Checked
#    Click On Need More Drink Optional Request Checkbox
#    Need More Drink Optional Request Checkbox Should Be Checked
#    Click On Need More Dishes Optional Request Checkbox
#    Need More Dishes Optional Request Checkbox Should Be Checked
#    Click On Change Date Person Optional Request Checkbox
#    Change Date Person Optional Request Checkbox Should Be Checked
#    Click On Change Seat View Optional Request Checkbox
#    Change Seat View Optional Request Checkbox Should Be Checked
#    Click On Change Dessert Optional Request Checkbox
#    Change Dessert Optional Request Checkbox Should Be Checked
#    Click On Summary Tab
#    Click On Order Tab
