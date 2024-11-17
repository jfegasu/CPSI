@echo off
cd apirest
start python main.py >errorapi.txt
start python routes.py >errorapp.txt
cd ..

cls
start chrome http://127.0.0.1:8000
