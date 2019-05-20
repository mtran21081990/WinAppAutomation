*** Settings ***
Library   WinAppLibrary
Library  Collections
Resource  ../Pages/Home_Page/Home_Page.robot
Variables  Data/settings.yaml

*** Keywords ***
User Open Application
    #Sleep  5s
    Setup Application Under Test

Setup Application Under Test
    ${settings} =  Convert To Dictionary  ${APPLICATION}
    Setup Application  ${settings}

User Prepare The Test Environment
    User Open Application
    #User Access To Application Home Page

User Cleanup The Test Environment
    Close Application

User Setup Test Case
    # Setup here

User Cleanup Test Case
    Capture Screen

User Access To Application Home Page
    User Should See Application Home Page

