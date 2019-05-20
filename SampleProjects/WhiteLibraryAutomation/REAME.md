# Sample automation test project using White Library (and Sikuli Library as a helper)

This is a sample automation test project which will create a user-defined Library extended from WhiteLibrary (also included SikuliLibrary). For more information regarding included libraries:

[WhiteLibrary](https://github.com/Omenia/robotframework-whitelibrary)

[SikuliLibrary](https://github.com/rainmanwy/robotframework-SikuliLibrary)

## How to run

1. Pull/Download the project from Git. Also pull/download the sample application.

2. Open Python IDE (prefered PyCharm), open the WhiteLibraryAutomation project. Create a new Interpreter for this project in File > Settings > Project Interpreter. Restart IDE (if need).

3. Install all required package by executing file "install_required_package.bat". The file will install robotframework, robotframework-SikuliLibrary, robotframework-whitelibrary and pyyaml.

4. Copy {This_GitHub_URL}/WinAppAutomation/Prerequisites/WhiteLibrary/bin folder and paste into {Project_URL}\WinAppAutomation\venv\Lib\site-packages\WhiteLibrary. Doing this will copy the 2 required library dll files of WhiteLibrary.

