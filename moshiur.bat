@echo off
set repo_url=https://github.com/moshiurrahmandeap11/moshiur_downloader.git
set folder_name=moshiur_downloader

:: Check if the folder exists
if exist %folder_name% (
    echo Repository already exists. Skipping clone...
) else (
    echo Cloning repository...
    git clone %repo_url%
)

:: Change directory to the cloned folder
cd %folder_name%

:: Run the Python script
echo Running moshiur_downloader.py...
start /min python moshiur_downloader.py

:: Wait for 2 seconds before closing
timeout /t 2 /nobreak >nul
exit
