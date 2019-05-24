# Sample automation test project using WhiteLibrary (and SikuliLibrary as a helper)

This is a sample automation test project which will create an user-defined Library extended from WhiteLibrary (also included SikuliLibrary). For more information regarding the 2 included libraries:

[WhiteLibrary](https://github.com/Omenia/robotframework-whitelibrary)

[SikuliLibrary](https://github.com/rainmanwy/robotframework-SikuliLibrary)

## How to run

1. Download & Install Python 3.7 or newer version. Might require to install latest .Net framework to run sample WPF application.

3. Download & Install Windows Application Driver (WinAppDriver) at [WinAppDriver GitHub Release Link](https://github.com/Microsoft/WinAppDriver/releases). This is a service to support Selenium-like UI Test Automation on Windows Applications. This service supports testing Universal Windows Platform (UWP), Windows Forms (WinForms), Windows Presentation Foundation (WPF), and Classic Windows (Win32) apps on Windows 10 PCs. WinAppDriver complies to the JSON Wire Protocol standard and some application management functionalities defined by Appium.

4. Pull/Download the project from Git. Also pull/download the sample WPF application (more sample application will be updated later) [Restaurant_Order_Application GitHub Link](https://github.com/mtran21081990/WinAppAutomation/tree/master/SampleApplication/Restaurant_Order_Application)

5. Open a Python IDE (prefered PyCharm), then open the AppiumLibraryAutomation project. Create a new Interpreter for this project in File > Settings > Project Interpreter. Restart IDE (if need).

6. Install all required packages by executing file "required_packages.bat". The installed libraries are: robotframework, robotframework-SikuliLibrary, robotframework-appiumlibrary and pyyaml.

7. Add environment variable "DISABLE_SIKULI_LOG" = 1 to disable sikuli's log files

8. Run test suite in Tests\Suites. There are 02 sample tests suites for now. 
