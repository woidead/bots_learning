python -m venv env
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
env\Scripts\activate.ps1
env\Scripts\python.exe -m pip install --upgrade pip
pip install aiogram