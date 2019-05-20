*** Settings ***
Library  WinAppLibrary
Resource  ../Tests/Base_Test.robot

Suite Setup  User Prepare Test Environment For [This Module]

#Test Setup  Setup [This Module] Test Case

Test Teardown    User Cleanup [This Module] Test Case

#Suite Teardown    User Cleanup Test Environment For [This Module]

Force Tags  sample


*** Test Cases ***

Test Sample Case With Wait 1s
    [Tags]  sample_1
    Click Item On Application  text:File tab
    Sleep  1s
    Click Item On Application  text:New
    Sleep  1s
    Click Item On Application  text=Pencil
    Sleep  1s
    ${X} =  Convert To Integer  200
    ${Y} =  Convert To Integer  200
    :FOR    ${index}    IN RANGE    200
    \  ${Y_POS} =  Evaluate  ${Y}+${index}
    \  Mouse Click  ${X}  ${Y_POS}
    Sleep  1s
    ${X} =  Convert To Integer  200
    ${Y} =  Convert To Integer  400
    :FOR    ${index}    IN RANGE    200
    \  ${X_POS} =  Evaluate  ${X}+${index}
    \  Mouse Click  ${X_POS}  ${Y}
    Sleep  1s
    ${X} =  Convert To Integer  400
    ${Y} =  Convert To Integer  400
    :FOR    ${index}    IN RANGE    200
    \  ${Y_POS} =  Evaluate  ${Y}-${index}
    \  Mouse Click  ${X}  ${Y_POS}
    Sleep  1s
    ${X} =  Convert To Integer  400
    ${Y} =  Convert To Integer  200
    :FOR    ${index}    IN RANGE    200
    \  ${X_POS} =  Evaluate  ${X}-${index}
    \  Mouse Click  ${X_POS}  ${Y}
    Sleep  1s
    Click Item On Application  text:File tab
    Sleep  1s
    Click Item On Application  text:Save as
    Sleep  1s
    ${name}=  Get Applicable Name  example_paint
    Input Text To Textbox  id=1001  ${name}
    Sleep  1s
    Click Item On Application  text:Save

Test Sample Case With Wait 1s No Draw
    [Tags]  sample_2
    Click Item On Application  text:File tab
    Sleep  1s
    Click Item On Application  text:New
    Sleep  1s
    Click Item On Application  text=Pencil
    Sleep  1s
    Click Item On Application  text:File tab
    Sleep  1s
    Click Item On Application  text:Save as
    Sleep  1s
    ${name}=  Get Applicable Name  example_paint
    Input Text To Textbox  id=1001  ${name}
    Sleep  1s
    Click Item On Application  text:Save
    Sleep  4s

Test Sample Case 2 No Wait
    [Tags]  sample_3
    Click Item On Application  text:File tab
    #Sleep  1s
    Click Item On Application  text:New
    #Sleep  1s
    Click Item On Application  text=Pencil
    #Sleep  1s
    ${X} =  Convert To Integer  200
    ${Y} =  Convert To Integer  200
    :FOR    ${index}    IN RANGE    200
    \  ${Y_POS} =  Evaluate  ${Y}+${index}
    \  Mouse Click  ${X}  ${Y_POS}
    #Sleep  1s
    ${X} =  Convert To Integer  200
    ${Y} =  Convert To Integer  400
    :FOR    ${index}    IN RANGE    200
    \  ${X_POS} =  Evaluate  ${X}+${index}
    \  Mouse Click  ${X_POS}  ${Y}
    #Sleep  1s
    ${X} =  Convert To Integer  400
    ${Y} =  Convert To Integer  400
    :FOR    ${index}    IN RANGE    200
    \  ${Y_POS} =  Evaluate  ${Y}-${index}
    \  Mouse Click  ${X}  ${Y_POS}
    #Sleep  1s
    ${X} =  Convert To Integer  400
    ${Y} =  Convert To Integer  200
    :FOR    ${index}    IN RANGE    200
    \  ${X_POS} =  Evaluate  ${X}-${index}
    \  Mouse Click  ${X_POS}  ${Y}
    #Sleep  1s
    Click Item On Application  text:File tab
    #Sleep  1s
    Click Item On Application  text:Save as
    #Sleep  1s
    ${name}=  Get Applicable Name  example_paint
    Input Text To Textbox  id=1001  ${name}
    #Sleep  1s
    Click Item On Application  text:Save

Test Sample Calculator
    [Tags]  sample_4
    Click Item On Application  id=num7Button
    Sleep  1s
    Click Item On Application  id=plusButton
    Sleep  1s
    Click Item On Application  id=num8Button
    Sleep  1s
    Click Item On Application  id=equalButton
    Sleep  1s

Test Sample Wpf Application
    [Tags]  sample_5
    Toggle Check Box  text=Item1
    Sleep  1s
    Toggle Check Box  text=Item2
    Sleep  1s
    Toggle Check Box  text=Item3
    Sleep  1s
    Toggle Check Box  text=Item4
    Sleep  1s
    Click Item On Application  id=AComboBox
    Sleep  1s
    Click Item On Application  text=Test12
    Sleep  1s
    Click Item On Application  id=OpenMessageBox
    Sleep  1s
    #Test message box
    Click Item On Application  text=OK

*** Keywords ***

User Prepare Test Environment For [This Module]
	User Prepare The Test Environment

Setup [This Module] Test Case
    User Setup Test Case

User Cleanup [This Module] Test Case
	User Cleanup Test Case

User Cleanup Test Environment For [This Module]
	User Cleanup The Test Environment
