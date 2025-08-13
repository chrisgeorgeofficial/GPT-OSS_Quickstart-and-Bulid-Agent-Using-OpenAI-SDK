@echo off
REM Check if virtual environment already exists
IF NOT EXIST venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Install requirements
echo Installing dependencies from requirements.txt...
pip install --upgrade pip
pip install -r requirements.txt

REM Run the Python script
echo Running simpleagent.py...
python simpleagent.py

echo.
echo ✅ All done! Script executed successfully.
pause
