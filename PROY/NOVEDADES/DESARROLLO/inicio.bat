cls 
rem start /b pip install -r "%CD%/requi.txt"
start /b python ./api/app.py
start /b python ./app.py"

start python -m http.server 9000
start  http://127.0.0.1:9000

