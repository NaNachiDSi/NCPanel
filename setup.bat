pip install pynput
pip install twitchio
pip install speechrecognition
pip install gtts
pip install pygame
@echo off
echo DID YOU SET THE FOLLOWING ENVIRONMENTAL VARIABLES? "OAUTH_TOKEN", "BOTNICK", "CHANNEL"
:loop
set /p user_input=PLEASE TYPE "YES": 
if "%user_input%"=="YES" exit
goto loop