*** Settings ***
Resource  SubPage_Actions.robot

*** Keywords ***

User Should See Sub Page Appears
	Sub Page Title Should Be Correct
	Sub Page Content Should Appears

User Input Into Sub Page Text Box
	[Arguments]  ${value}
	Input Text Into Sub Page Text Box  ${value}
