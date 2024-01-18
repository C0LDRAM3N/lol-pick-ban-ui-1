cd python_startup/batch_files
START start_backend.bat
START start_frontend.bat
timeout /t 30 /nobreak
start "" http://localhost:3000/?backend=ws://localhost:8999