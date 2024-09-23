@echo off

REM Check if venv already exists
IF NOT EXIST "venv\" (
    echo Creating virtual environment...
    python -m venv venv
) ELSE (
    echo Virtual environment already exists.
)

REM Activate the virtual environment
call venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

echo Setup complete. You can now run the project.
