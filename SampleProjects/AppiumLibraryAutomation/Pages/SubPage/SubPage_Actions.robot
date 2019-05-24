*** Settings ***
Resource  SubPage_Variables.robot

*** Keywords ***

# Veriify Home Page

Sub Page Title Should Be Correct
	Window Title Should Equal To  ${SUBPAGE_ID}  ${SUBPAGE_TITLE}

Sub Page Content Should Appears
	Element Text Should Be  ${SUBPAGE_HEADER_ID}   ${SUBPAGE_HEADER_TEXT}

Input Text Into Sub Page Text Box
	[Arguments]  ${value}
	Input Text  ${SUBPAGE_TEXTBOX_ID}  ${value}
