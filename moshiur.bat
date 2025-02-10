@echo off
set repo_url=https://github.com/moshiurrahmandeap11/moshiur_downlaoder
set folder_name=moshiur_downloader

:: Check if the folder exists
if exist %folder_name% (
    echo Repository already exists. Checking for updates...
    cd %folder_name%
    git fetch origin
    for /f %%i in ('git rev-parse HEAD') do set local_hash=%%i
    for /f %%i in ('git rev-parse origin/main') do set remote_hash=%%i

    if "%local_hash%"=="%remote_hash%" (
        echo Already up to date.
    ) else (
        echo Updates found! Pulling latest changes...
        git pull
    )
) else (
    echo Cloning repository...
    git clone %repo_url%
    cd %folder_name%
)

:: Run the Python script
echo Running moshiur_downloader.py...
start /min python moshiur_downloader.py

:: Wait for 2 seconds before closing
timeout /t 2 /nobreak >nul
exit
