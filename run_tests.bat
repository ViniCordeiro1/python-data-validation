@echo off
call .\venv\Scripts\activate.bat
set PYTHONPATH=.
pytest
pause
