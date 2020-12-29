@echo off
pyuic5 -x mlock.ui -o mlock.py
pause
pyrcc5 -o resources_rc.py resources.qrc
pause