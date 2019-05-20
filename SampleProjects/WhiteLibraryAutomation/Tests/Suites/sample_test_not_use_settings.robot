*** Settings ***
Library  WinAppLibrary
Resource  ../Tests/Base_Test.robot

#Suite Setup  User Prepare Test Environment For [This Module]

#Test Setup  Setup [This Module] Test Case

#Test Teardown    User Cleanup [This Module] Test Case


#Suite Teardown    User Cleanup Test Environment For [This Module]

Force Tags  sample_not_setting


*** Test Cases ***

User automates on Paint application
    [Tags]  sample_no_1
    # Open Application
    ${settings} =  Create Dictionary  TYPE=wpf  PATH=C:\\Windows\\System32\\mspaint.exe  ALREADY_OPENED=No  MAIN_WINDOW_NAME=Untitled - Paint
    Setup Application  ${settings}
    Sleep  5s

    # Run automation test
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

    # Close Application
    Close Application

Test Sample Wpf Application
    [Tags]  sample_no_2

    # Open Application
    ${settings} =  Create Dictionary  TYPE=wpf  PATH=D:\\GitHub\\WinAppAutomation\\SampleApplication\\WPF_Application\\UsingInvokeCommandAction.exe  ALREADY_OPENED=No  MAIN_WINDOW_NAME=
    Setup Application  ${settings}
    Sleep  1s

    # Execute Test on ListBox 1
    User Can Select Listbox 1 By Index
    Sleep  1s
    User Can Select Listbox 1 By Value
    Sleep  1s

    # Execute Test on ListBox 2
    User Can Select Listbox 2 By Index
    Sleep  1s

    # Execute Test on Calendar
    User Can Select Calendar
    Sleep  1s

    # Execute Test on Radio Button
    User Can Select Radio Button
    Sleep  1s

    # Execute Test on List of Buttons with same AutomationId
    User Can Input On Each Textbox In List
    Sleep  1s

    # Execute Test on Tooltip
    #User Can Verify Tooltip
    Sleep  1s

    # Execute Test on Toggle Button
    User Can Toggle Button
    Sleep  1s

    # Execute Test on Expander Button
    User Can Expand
    Sleep  1s

    # Execute Test on Combobox
    User Can Select Combobox
    Sleep  1s

    # Execute Test on Date Picker
    User Can Select Date Picker
    Sleep  1s

    # Execute Test on Password field
    User Can Input Password
    Sleep  1s

    # Execute Test on Checkbox
    User Can Toggle Checkbox
    Sleep  1s

    # Execute Test on Tree View
    User Can Select Tree Node
    Sleep  1s

    # Execute Test on Group Box
    User Can Select Element In Group Box
    Sleep  1s

    # Execute Test on Popup
    User Can Reach Element In Popup
    Sleep  1s

    # Execute Test on Progress Bar
    User Can Work With Progress Bar
    Sleep  1s

    # Execute Test on Dialoag
    User Can Open Dialog
    Sleep  1s

    # Execute Test on Context Menu
    User Can Open Context Menu
    Sleep  1s

    # Execute Test on Slider
    User Can Set Slider
    Sleep  1s

    # Execute Test on Frame
    User Can Reach Element In Frame
    Sleep  1s

    # Execute Test on Tab
    User Can Open Tab  Table and Custom Control
    Sleep  1s
    User Can Open Tab  General WPF Control
    Sleep  1s
    User Can Open Tab  Table and Custom Control
    Sleep  1s

    # Execute Test on User Control
    User Can Reach User Control

    # Execute Test on Custom Control
    User Can Reach Custom Control

    # Close Application
    Close Application



*** Keywords ***

User Can Select Listbox 1 By Index
    Select Listbox Index  id=listbox-1  0
    Listbox Selection Should Be  id=listbox-1  Coffie
    Sleep  1s
    Select Listbox Index  id=listbox-1  1
    Listbox Selection Should Be  id=listbox-1  Tea
    Sleep  1s
    Select Listbox Index  id=listbox-1  3
    Listbox Selection Should Be  id=listbox-1  Milk
    Sleep  1s

User Can Select Listbox 1 By Value
    #Select Listbox Value  id=listbox-1  Mango Shake
    #Listbox Selection Should Be  id=listbox-1  Mango Shake
    Select Listbox Value  id=listbox-1  Coffie
    Listbox Selection Should Be  id=listbox-1  Coffie
    Sleep  1s
    Select Listbox Value  id=listbox-1  Tea
    Listbox Selection Should Be  id=listbox-1  Tea
    Sleep  1s
    Select Listbox Value  id=listbox-1  Milk
    Listbox Selection Should Be  id=listbox-1  Milk
    Sleep  1s

User Can Select Listbox 2 By Index
    Select Listbox Index  id=listbox2  0
    Listbox Selection Should Be  id=listbox2  Coffie
    Sleep  1s
    Select Listbox Index  id=listbox2  1
    Listbox Selection Should Be  id=listbox2  Coffie
    Sleep  1s
    Select Listbox Index  id=listbox2  3
    Listbox Selection Should Be  id=listbox2  Coffie
    Sleep  1s
    #Select Listbox Index  id=listbox-1  7
    #Listbox Selection Should Be  id=listbox-1  Orange Juice  Coffie

User Can Select Calendar
    Click Button  text=Sunday, May 12, 2019
    Sleep  1s

User Can Select Radio Button
    Select Radio Button  text=Windows 7
    ${state}  Get Radio Button State  text=Windows 7
    Should Be True  ${state}  Radio Button "Windows 7" is not selected
    Sleep  1s
    Select Radio Button  text=Microsoft Office 2003
    ${state}  Get Radio Button State  text=Microsoft Office 2003
    Should Be True  ${state}  Radio Button "Microsoft Office 2003" is not selected
    Sleep  1s

User Can Input On Each Textbox In List
    @{list}  Get Items  id=textbox1
    :FOR    ${textbox}    IN    @{list}
    \  Input Text To Textbox  ${textbox}  Input Sample Text
    \  Sleep  1s
    \  Verify Text In Textbox  ${textbox}  Input Sample Text

User Can Verify Tooltip
    Click Button  id=button-1
    Sleep  1s
    Window Tooltip Should Equal To   Textbox in Tooltip

User Can Toggle Button
    Click Button  id=toggle-button-1
    Sleep  1s

User Can Expand
    Click Button  id=HeaderSite
    Sleep  1s
    Toggle Check Box  text=Option 1
    Sleep  1s

User Can Select Combobox
    Select Combobox Value  id=combobox-1  ComboBox Item #3
    Sleep  1s
    Verify Combobox Selection  id=combobox-1  ComboBox Item #3

User Can Select Date Picker
    Click Button  text=Show Calendar
    Sleep  1s
    Click Button  text=Wednesday, May 15, 2019
    Sleep  1s

User Can Input Password
    Input Text To Textbox  id=password-1  Password
    Sleep  1s

User Can Toggle Checkbox
    Toggle Check Box  id=checkbox-1
    Sleep  1s
    Toggle Check Box  id=checkbox-2
    Sleep  1s
    Toggle Check Box  id=checkbox-3
    Sleep  1s
    Verify Check Box  id=checkbox-1  True
    Verify Check Box  id=checkbox-2  True
    Verify Check Box  id=checkbox-3  True

User Can Select Tree Node
    Double Click Tree Node  id=tree-view-1  Level 1
    Sleep  2s
    Select Tree Node  id=tree-view-1  Level 1  Level 2.2  Level 3.2
    Sleep  1s

User Can Select Element In Group Box
    Toggle Check Box  text=Cheese
    Sleep  1s

User Can Reach Element In Popup
    Click Button  id=toggle-button-popup-1
    Sleep  1s
    Input Text To Textbox  id=popup-textbox-1  Text in Popup
    Sleep  1s
    Click Button  id=toggle-button-popup-1
    Sleep  1s

User Can Work With Progress Bar
    Click Button  id=progress-bar-button-1
    Element Should Be Visible  id=progress-bar-1
    Wait Until Keyword Succeeds  30 sec  10 sec  Element Should Not Be Visible  id=progress-bar-1

User Can Open Dialog
    Click Button  id=button-dialog-1
    Sleep  2s
    Attach Window  Input
    Input Text To Textbox  id=txtAnswer  Text in Dialog
    Sleep  1s
    Click Button  id=btnDialogOk
    Sleep  2s
    Attach Window  class_name:Window

User Can Open Context Menu
    Right Click Item  id=button-context-menu-1
    Sleep  1s
    Click Item In Popup Menu  Menu item 1
    Sleep  1s
    Right Click Item  id=button-context-menu-1
    Sleep  1s
    Click Item In Popup Menu  Menu item 2
    Sleep  1s

User Can Set Slider
    Set Slider Value  id=slider-1  50
    Sleep  1s
    Verify Slider Value  id=slider-1  50

User Can Reach Element In Frame
    Input Text To Textbox  id=textbox-frame-1  Text in Frame
    Sleep  1s

User Can Open Tab
    [Arguments]  ${tab_name}
    Select Tab Page  id=tab-control-1  ${tab_name}

User Can Reach User Control
    Input Text To Textbox  id=custom-control-textbox-1  Text in User-defined Control
    Click Button  id=custom-control-button-1

User Can Reach Custom Control
    ${button}  Get Item  text=Play
    Click Button  ${button}
    Sleep  1s


