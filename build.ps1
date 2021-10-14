try { 
    #.\venv\Scripts\deactivate.bat
    deactivate
}
catch { }

.\.venv\Scripts\activate.ps1
python -m pip install --upgrade setuptools wheel
python -m pip install -r .\requirements.txt
python setup.py sdist bdist_wheel
if(!(Test-Path "..\LocalPackages\")){
    New-Item -Type dir "..\LocalPackages\"
}
Copy-Item ".\dist\*.whl" -Destination "..\LocalPackages\"
Remove-Item .\build\ -Force -Recurse
Remove-Item .\dist\ -Force -Recurse
Get-ChildItem ./ -Recurse -Include *.egg-info | Remove-item -Recurse -Force