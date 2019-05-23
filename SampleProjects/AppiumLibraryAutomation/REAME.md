# Sample automation test project using White Library (and Sikuli Library as a helper)

This is a sample automation test project which will create an user-defined Library extended from WhiteLibrary (also included SikuliLibrary). For more information regarding the 2 included libraries:

[Appiumibrary](https://github.com/serhatbolsu/robotframework-appiumlibrary)

[SikuliLibrary](https://github.com/rainmanwy/robotframework-SikuliLibrary)

## How to run

1. Download & Install Python 3.7 or newer version. Might require to install latest .Net framework to run sample WPF application.

2. Pull/Download the project from Git. Also pull/download the sample WPF application (more sample application will be updated later) [Sample WPF Application GitHub Link](https://github.com/mtran21081990/WinAppAutomation/tree/master/SampleApplication/WPF_Application)

3. Open a Python IDE (prefered PyCharm), then open the AppiumLibraryAutomation project. Create a new Interpreter for this project in File > Settings > Project Interpreter. Restart IDE (if need).

4. Install all required packages by executing file "required_packages.bat". The installed libraries are: robotframework, robotframework-SikuliLibrary, robotframework-whitelibrary and pyyaml.

5. Add environment variable "DISABLE_SIKULI_LOG" = 1 to disable sikuli's log files

6. Run test suite in Tests\Suites. There are 02 sample test suites for now. 
+ sample_test.robot: Contains test cases which require input in Tests/Data/settings.yaml: MAIN_WINDOW_NAME: "Untitled - Paint"; PATH: "C:\\Windows\\System32\\mspaint.exe"
  - Test case "Test Sample Case With Wait 1s" with tag "sample_1": Open a Paint and draw a rectangle then save.
  - Test case "Test Sample Case With Wait 1s No Draw" with tag "sample_2": Open a Paint and then save.
+ sample_test_not_use_settings.robot: Contains test cases which don't need to input anything more. 
  - Test case "User automates on Paint application" with tag "sample_no_1": Open a Paint and draw a rectangle then save.
  - Test case "Test Sample Wpf Application" with tag "sample_no_2": Open the dowloaded WPF application and verify/click on all controls.




