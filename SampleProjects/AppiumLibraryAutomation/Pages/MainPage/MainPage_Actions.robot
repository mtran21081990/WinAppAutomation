*** Settings ***
Resource          Home_Page_Variables.robot

*** Keywords ***

# Veriify Home Page

Application Title Should Be Correct
	Window Title Should Equal To  ${APPLICATION_TITLE}

Application Home Page Content Should Be Appeared
	#Element Should Be Visible  ${APPLICATION_MENU}
	Element Should Be Visible  ${APPLICATION_ELEMENT}

Wait Unil Home Page Appeared
	#Wait Until Element Is Visible  ${APPLICATION_MENU}
	#Wait Until Element Is Visible  ${APPLICATION_ELEMENT}
