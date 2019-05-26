*** Settings ***

Resource  SubPage_Actions.robot

*** Keywords ***

User Switch To Sub Page
	Switch To Sub Page

User Should See Sub Page Appears
	Sub Page Title Should Be Correct
	Sub Page Content Should Appears

User Input Into Sub Page Text Box Fields
	Input Text Into Sub Page Text Box 1  Sub Page field 1
	Input Text Into Sub Page Text Box 2  Sub Page field 2
	Input Text Into Sub Page Text Box 3  Sub Page field 3
	Input Text Into Sub Page Text Box 4  Sub Page field 4

User Should See Input Texts In Sub Page Text Box Fields Are Correct
	Sub Page Text Box 1 Value Must Be  Sub Page field 1
	Sub Page Text Box 2 Value Must Be  Sub Page field 2
	Sub Page Text Box 3 Value Must Be  Sub Page field 3
	Sub Page Text Box 4 Value Must Be  Sub Page field 4


