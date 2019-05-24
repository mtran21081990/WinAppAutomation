*** Settings ***
Library  AppiumAppLibrary
Resource  ../Tests/Base_Test.robot
Resource  ../Pages/SubPage/SubPage_Page.robot

Suite Setup  User Prepare Test Environment For [This Module]

#Test Setup  Setup [This Module] Test Case

Test Teardown    User Cleanup [This Module] Test Case

Suite Teardown    User Cleanup Test Environment For [This Module]

Force Tags  subpage


*** Test Cases ***

User Can Input Text In Sub Page
    [Tags]  subpage_1
    Sleep  5s
    User Move To Sub Page
    Sleep  5s
    Switch To New Window  ${SUBPAGE_ID}  Sub Window
    #User Should See Sub Page Appears
    User Input Into Sub Page Text Box  Test Sub Page


*** Keywords ***

User Prepare Test Environment For [This Module]
	User Prepare The Test Environment

Setup [This Module] Test Case
    User Setup Test Case

User Cleanup [This Module] Test Case
	User Cleanup Test Case

User Cleanup Test Environment For [This Module]
	User Cleanup The Test Environment
