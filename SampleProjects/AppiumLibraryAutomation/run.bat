@ECHO OFF
REM  run all tests by tags

FOR /f "delims=" %%a IN ('wmic OS Get localdatetime  ^| find "."') DO SET dt=%%a
SET YYYY=%dt:~0,4%
SET MM=%dt:~4,2%
SET DD=%dt:~6,2%
SET HH=%dt:~8,2%
SET Min=%dt:~10,2%
SET Sec=%dt:~12,2%

set stamp=%YYYY%-%MM%-%DD%_%HH%-%Min%-%Sec%

IF EXIST "Results" RENAME "Results" "Results-%stamp%"

IF "%~1"=="" GOTO RUN_ALL

IF NOT "%~1"=="" GOTO RUN_TAG

:RUN_ALL
robot --pythonpath ./Lib -d Results Tests

:RUN_TAG
robot --pythonpath ./Lib -d Results -i %1% Tests
