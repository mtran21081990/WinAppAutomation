*** Settings ***
Resource  MainPage_Variables.robot

*** Keywords ***

# Veriify Home Page

Main Page Title Should Be Correct
	Window Title Should Equal To  ${MAINPAGE_ID}  ${MAINPAGE_TITLE}

Main Page Content Should Appears
	Element Text Should Be  ${MAINPAGE_HEADER_ID}   ${MAINPAGE_HEADER_TEXT}

Click Main Pape Next Button
	Click Element  ${MAINPAGE_NEXT_ID}

