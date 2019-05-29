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
    Select Item In Drink List Box  Tea
    Drink List Box Selection Should Be  Tea
    Select Item In Drink List Box  Milk
    Drink List Box Selection Should Be  Milk
    Select Item In Drink List Box  Coffee
    Drink List Box Selection Should Be  Coffee
    Select Item In Dishes List Box  Pizza
    @{list}  Create List  Pizza
    Dishes List Box Selection Should Be  @{list}
    Select Item In Dishes List Box  Hamburger
    @{list}  Create List  Pizza  Hamburger
    Dishes List Box Selection Should Be  @{list}
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
    Select Value In Date Person Combobox  Brad Pitt
    Date Person Combobox Selection Value Should Be  Brad Pitt
    Select Value In Date Person Combobox  Angelina Jolie
    Date Person Combobox Selection Value Should Be  Angelina Jolie
    Select Value In Date Person Combobox  Tom Cruise
    Date Person Combobox Selection Value Should Be  Tom Cruise
    Select Value In Date Person Combobox  Jennifer Aniston
    Date Person Combobox Selection Value Should Be  Jennifer Aniston
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
