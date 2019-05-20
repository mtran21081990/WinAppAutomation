*** Settings ***
Resource          Home_Page_Actions.robot

*** Keywords ***

User Should See Application Home Page
    Application Title Should Be Correct
    Application Home Page Content Should Be Appeared
