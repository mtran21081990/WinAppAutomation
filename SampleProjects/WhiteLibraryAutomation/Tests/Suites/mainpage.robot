*** Settings ***
Library  WhiteAppLibrary
Resource  ../Tests/Base_Test.robot

Suite Setup  User Prepare Test Environment For Main Page

#Test Setup  Setup Main Page Test Case

Test Teardown    User Cleanup Main Page Test Case

Suite Teardown    User Cleanup Test Environment For Main Page

Force Tags  mainpage


*** Test Cases ***

User Can Interact With Controls On Main Page
    [Tags]  mainpage_1
    User Can Interact Controls On Main Page

*** Keywords ***

User Prepare Test Environment For Main Page
	User Prepare The Test Environment

Setup Main Page Test Case
	User Setup Test Case

User Cleanup Main Page Test Case
	User Cleanup Test Case

User Cleanup Test Environment For Main Page
	User Cleanup The Test Environment
