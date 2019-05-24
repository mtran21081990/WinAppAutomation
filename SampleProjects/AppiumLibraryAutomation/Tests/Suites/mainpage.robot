*** Settings ***
Library  AppiumAppLibrary
Resource  ../Tests/Base_Test.robot

Suite Setup  User Prepare Test Environment For [This Module]

#Test Setup  Setup [This Module] Test Case

Test Teardown    User Cleanup [This Module] Test Case

Suite Teardown    User Cleanup Test Environment For [This Module]

Force Tags  mainpage


*** Test Cases ***

User Can Move To Sub Page From Main Page
    [Tags]  mainpage_1
    User Move To Sub Page


*** Keywords ***

User Prepare Test Environment For [This Module]
	User Prepare The Test Environment

Setup [This Module] Test Case
    User Setup Test Case

User Cleanup [This Module] Test Case
	User Cleanup Test Case

User Cleanup Test Environment For [This Module]
	User Cleanup The Test Environment
