*** Settings ***
Library  AppiumAppLibrary
Resource  SubPage_Variables.robot

*** Keywords ***

# Veriify Home Page

Switch To Sub Page
    Switch To New Window  ${SUBPAGE_ID}  ${SUBPAGE_TITLE}

Sub Page Title Should Be Correct
	Window Title Should Equal To  ${SUBPAGE_ID}  ${SUBPAGE_TITLE}

Sub Page Content Should Appears
	Element Text Should Be  ${SUBPAGE_HEADER_ID}   ${SUBPAGE_HEADER_TEXT}

Input Text Into Sub Page Text Box 1
	[Arguments]  ${value}
	Input Text  ${SUBPAGE_TEXTBOX1_ID}  ${value}

Input Text Into Sub Page Text Box 2
	[Arguments]  ${value}
	Input Text  ${SUBPAGE_TEXTBOX2_ID}  ${value}

Input Text Into Sub Page Text Box 3
	[Arguments]  ${value}
	Input Text  ${SUBPAGE_TEXTBOX3_ID}  ${value}

Input Text Into Sub Page Text Box 4
	[Arguments]  ${value}
	Input Text  ${SUBPAGE_TEXTBOX4_ID}  ${value}

Sub Page Text Box 1 Value Must Be
	[Arguments]  ${value}
	Element Text Should Be  ${SUBPAGE_TEXTBOX1_ID}  ${value}

Sub Page Text Box 2 Value Must Be
	[Arguments]  ${value}
	Element Text Should Be  ${SUBPAGE_TEXTBOX2_ID}  ${value}

Sub Page Text Box 3 Value Must Be
	[Arguments]  ${value}
	Element Text Should Be  ${SUBPAGE_TEXTBOX3_ID}  ${value}

Sub Page Text Box 4 Value Must Be
	[Arguments]  ${value}
	Element Text Should Be  ${SUBPAGE_TEXTBOX4_ID}  ${value}





