# Workshop Python

## Install Visual Studio Code
Ga naar deze link en installeer Visual Studio Code. Dit is een code editor waarin je code kan schrijven, aanpassen en uitvoeren. 

>https://code.visualstudio.com/

## Install Python extension



## Install Python interpreter

Voor deze workshop gebruiken we Python. Python is de meest abstracte taal en daarom het meest geschikt om mee te beginnen als programmeertaal.

### Windows
Om python te installeren volg je deze link: [Install Python](https://www.python.org/downloads/)

Om zeker te zijn open je de terminal op windows (Command Prompt) en voer `python` uit. Nu zou de versie die je gedownload hebt tevoorschijn moeten komen.

Voor meer informatie: [Using Python on Windows at Python.org](https://docs.python.org/3.9/using/windows.html)

### macOS
The system install of Python on macOS is not supported. Instead, an installation through Homebrew is recommended. To install Python using Homebrew on macOS use brew install python3 at the Terminal prompt.

Note On macOS, make sure the location of your VS Code installation is included in your PATH environment variable. See these setup instructions for more information.

### Linux
The built-in Python 3 installation on Linux works well, but to install other Python packages you must install pip with get-pip.py.

## Theorie

## Pong
Programmeren leer je door te doen. En het is altijd leuker om iets visueel te programmeren. Daarom programmeren we nu Pong.

Open opgave.py

Om te beginnen laden we enkele modules in.
```
import turtle
import os
import time
```

Vervolgens maken we eerst een scherm waar het spel in gaan programmeren. 
```
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
``` 
