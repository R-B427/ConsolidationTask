@ECHO OFF
REM ------------------------------------------------------------
REM Command file for building Sphinx documentation on Windows
REM Updated for docs/ root structure (no 'source' folder)
REM ------------------------------------------------------------

REM Save current directory and switch to script directory
pushd %~dp0

REM Use SPHINXBUILD environment variable if set, otherwise default
if "%SPHINXBUILD%" == "" (
    set SPHINXBUILD=sphinx-build
)

REM Set directories
set SOURCEDIR=.
set BUILDDIR=_build

REM Check if sphinx-build exists
%SPHINXBUILD% --version >NUL 2>NUL
if errorlevel 9009 (
    echo.
    echo The 'sphinx-build' command was not found. Make sure you have Sphinx
    echo installed, then set the SPHINXBUILD environment variable to point
    echo to the full path of the 'sphinx-build' executable.
    echo.
    exit /b 1
)

REM If no argument, show help
if "%1" == "" goto help

REM Run Sphinx with the target passed (html, clean, etc.)
%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
REM Return to original directory
popd
