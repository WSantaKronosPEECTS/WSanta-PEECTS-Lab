@echo off
echo ========================================
echo   Welcome to Kronas AI Virtual Terminal
echo ========================================
:menu
echo.
echo [1] Start Kronas
echo [2] Explain PEECTS Concept
echo [3] Voice On
echo [4] Exit
set /p choice=Select an option: 
if "%choice%"=="1" echo Kronas is initializing with Elastic Time Logic...
if "%choice%"=="2" echo Explaining Palindromic Entangled Elastic Crystal Time Strings...
if "%choice%"=="3" echo Voice module is now active.
if "%choice%"=="4" exit
goto menu
