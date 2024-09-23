@echo off

REM Activate the virtual environment
call venv\Scripts\activate

REM Run the Python script
python src\index.py

REM Deactivate the virtual environment after the program exits
deactivate

echo Program finished. Press any key to exit.
pause
