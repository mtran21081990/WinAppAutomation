*** Settings ***
Library  AppiumAppLibrary
Resource  ../Tests/Base_Test.robot

Suite Setup  User Prepare Test Environment For [This Module]

#Test Setup  Setup [This Module] Test Case

Test Teardown    User Cleanup [This Module] Test Case

Suite Teardown    User Cleanup Test Environment For [This Module]

Force Tags  sample


*** Test Cases ***

Test Paint application on Windows 10
    [Tags]  sample_1
    #${current_context}=  Get Current Context
    ${current_session_id}=  Get Appium SessionId
    Click Item On Application  name=File tab
    Click Item On Application  name=New
    Click Item On Application  name=Pencil
    Click Item On Application  name=File tab
    Click Item On Application  name=Save as
    Sleep  3s
    ${name}=  Get Applicable Name  example_paint
    Input Text  accessibility_id=1001  ${name}
    Click Item On Application  name=Save

Test Calculator application on Windows 10
    [Tags]  sample_2
    #${current_context}=  Get Current Context
    ${current_session_id}=  Get Appium SessionId
    Click Item On Application  accessibility_id=num7Button
    Click Item On Application  accessibility_id=plusButton
    Click Item On Application  accessibility_id=num8Button
    Click Item On Application  accessibility_id=equalButton
    Sleep  5s

*** Keywords ***

User Prepare Test Environment For [This Module]
	User Prepare The Test Environment

Setup [This Module] Test Case
    User Setup Test Case

User Cleanup [This Module] Test Case
	User Cleanup Test Case

User Cleanup Test Environment For [This Module]
	User Cleanup The Test Environment
