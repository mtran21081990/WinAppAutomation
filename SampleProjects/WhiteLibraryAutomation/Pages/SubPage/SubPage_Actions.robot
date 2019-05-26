*** Settings ***
Library  WhiteAppLibrary
Resource  SubPage_Variables.robot

*** Keywords ***

# Veriify Home Page

Switch To Sub Page
    Attach Window  ${SUBPAGE_TITLE}

Sub Page Title Should Be Correct
	Window Title Should Be  ${SUBPAGE_TITLE}

Sub Page Content Should Appears
	Verify Label  ${SUBPAGE_HEADER_ID}   ${SUBPAGE_HEADER_TEXT}

Input Text Into Sub Page Text Box 1
	[Arguments]  ${value}
	Input Text To Textbox  ${SUBPAGE_TEXTBOX1_ID}  ${value}

Input Text Into Sub Page Text Box 2
	[Arguments]  ${value}
	Input Text To Textbox  ${SUBPAGE_TEXTBOX2_ID}  ${value}

Input Text Into Sub Page Text Box 3
	[Arguments]  ${value}
	Input Text To Textbox  ${SUBPAGE_TEXTBOX3_ID}  ${value}

Input Text Into Sub Page Text Box 4
	[Arguments]  ${value}
	Input Text To Textbox  ${SUBPAGE_TEXTBOX4_ID}  ${value}

Sub Page Text Box 1 Value Must Be
	[Arguments]  ${value}
	Verify Text In Textbox  ${SUBPAGE_TEXTBOX1_ID}  ${value}

Sub Page Text Box 2 Value Must Be
	[Arguments]  ${value}
	Verify Text In Textbox  ${SUBPAGE_TEXTBOX2_ID}  ${value}

Sub Page Text Box 3 Value Must Be
	[Arguments]  ${value}
	Verify Text In Textbox  ${SUBPAGE_TEXTBOX3_ID}  ${value}

Sub Page Text Box 4 Value Must Be
	[Arguments]  ${value}
	Verify Text In Textbox  ${SUBPAGE_TEXTBOX4_ID}  ${value}





