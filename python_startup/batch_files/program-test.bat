:: First the program calls the backend
:: Wait 10 seconds, just to make sure that the backend has fully started
:: Then call the frontend program
START backend_test.bat
timeout /t 15 /nobreak
START start_frontend.bat
start "" http://localhost:3000/?backend=ws://localhost:8999