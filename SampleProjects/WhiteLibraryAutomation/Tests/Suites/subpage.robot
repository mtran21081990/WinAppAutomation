*** Settings ***
Library  WhiteAppLibrary
Resource  ../Tests/Base_Test.robot
Resource  ../Pages/SubPage/SubPage_Page.robot

Suite Setup  User Prepare Test Environment For Sub Page

#Test Setup  Setup Sub Page Test Case

Test Teardown    User Cleanup Sub Page Test Case

Suite Teardown    User Cleanup Test Environment For Sub Page

Force Tags  subpage


*** Test Cases ***

User Can Input Text In Sub Page
    [Tags]  subpage_1
	Given User Navigates To Sub Page
	When User Input Into Sub Page Text Box Fields
	Then User Should See Input Texts In Sub Page Text Box Fields Are Correct


*** Keywords ***

User Prepare Test Environment For Sub Page
	User Prepare The Test Environment

Setup Sub Page Test Case
	User Setup Test Case

User Cleanup Sub Page Test Case
	User Cleanup Test Case

User Cleanup Test Environment For Sub Page
	User Cleanup The Test Environment

User Navigates To Sub Page
	Sleep  2s
	User Click On Main Page Next Button
	Sleep  2s
	User Switch To Sub Page
