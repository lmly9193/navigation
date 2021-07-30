@echo off
cls
echo 1.Start the Hugo server
echo 2.Build static pages
echo 3.Close

:selector
choice /c 123 /m "choice:"

if errorlevel 3 goto end
if errorlevel 2 goto build
if errorlevel 1 goto server

:server
hugo server -D
goto end

:build
hugo -D
goto end

:end
exit /b 