REM lint-and-fix.bat - for python3 linting and formatting
REM uses black for formatting
REM uses flake8 for linting
REM
black iSearchWsApi
REM black --check iSearchWsApi
flake8 iSearchWsApi --max-line-length=120
