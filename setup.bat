@echo off

if not defined PYTHON (set PYTHON=python)
if not defined VENV_DIR (set VENV_DIR=venv)

mkdir tmp 2>NUL

%PYTHON% -c "" >tmp/stdout.txt 2>tmp/stderr.txt
if %ERRORLEVEL% == 0 goto :start_venv
echo Couldn't launch python
goto :show_stdout_stderr

:start_venv
if [%VENV_DIR%] == [-] goto :skip_venv

dir %VENV_DIR%\Scripts\Python.exe >tmp/stdout.txt 2>tmp/stderr.txt
if %ERRORLEVEL% == 0 goto :activate_venv

for /f "delims=" %%i in ('CALL %PYTHON% -c "import sys; print(sys.executable)"') do set PYTHON_FULLNAME="%%i"
echo Creating venv in directory %VENV_DIR% using python %PYTHON_FULLNAME%
%PYTHON_FULLNAME% -m venv %VENV_DIR% >tmp/stdout.txt 2>tmp/stderr.txt
if %ERRORLEVEL% == 0 goto :activate_venv
echo Unable to create venv in directory %VENV_DIR%
goto :show_stdout_stderr

:activate_venv
set PYTHON="%~dp0%VENV_DIR%\Scripts\Python.exe"
echo venv %PYTHON%
echo Installing dependencies
%PYTHON% -m pip install -r requirements.txt

:endofscript

echo.
echo Requirements installed.
pause