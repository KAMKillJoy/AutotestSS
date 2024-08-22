cd "%~dp0"
call .\.venv\Scripts\activate.bat
python -m pytest .\Tests.py --alluredir .\results
allure serve .\results
pause