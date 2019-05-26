*** Settings ***
Library   WhiteAppLibrary
Library  Collections
Resource  ../Pages/MainPage/MainPage_Page.robot
Variables  Data/settings.yaml


*** Keywords ***

User Open Application
    Setup Application Under Test

Setup Application Under Test
    ${settings} =  Convert To Dictionary  ${APPLICATION}
    Setup Application  ${settings}

User Prepare The Test Environment
    User Open Application
    User Access To Application Home Page

User Cleanup The Test Environment
    Close Application

User Setup Test Case
    # Setup here

User Cleanup Test Case
    Take Desktop Screenshot

User Access To Application Home Page
    User Should See Main Page Appears
