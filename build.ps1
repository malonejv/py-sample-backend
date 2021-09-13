.\venv\Scripts\deactivate.bat venv
.\venv\Scripts\activate.ps1
python -m pip install --upgrade setuptools wheel
python setup.py sdist bdist_wheel
if(!(Test-Path "..\LocalPackages\")){
    New-Item -Type dir "..\LocalPackages\"
}
Copy-Item ".\dist\*.whl" -Destination "..\LocalPackages\"