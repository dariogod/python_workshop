# Workshop Python

## Installeer Visual Studio Code (VSC)
Visual Studio code is een software-ontwikkelplatform (Engels: IDE (integrated development environment)) voor programmeurs om code te schrijven, aan te passen en uit te voeren. 

>[Visual Studio Code](https://code.visualstudio.com/)


## Installeer Python extension
Deze extensie levert ondersteuning voor Python in VSC.

>[Python Extensie](https://marketplace.visualstudio.com/items?itemName=ms-python.python)


## Installeer Python interpreter

Voor deze workshop gebruiken we Python. Python is de meest abstracte taal en daarom het meest geschikt om mee te beginnen als programmeertaal.

### Windows
Om python te installeren volg je deze link: [Installeer Python](https://www.python.org/downloads/)

Om de installatie te verifiëren open je de terminal op windows (Command Prompt) en voer  
`py -3 --version`  
uit.   
Nu zou de versie die je gedownload hebt tevoorschijn moeten komen.

Voor meer informatie: [Python gebruiken op windows](https://docs.python.org/3.9/using/windows.html)

### macOS
De systeeminstallatie van Python op macOS wordt niet ondersteund. Gebruik daarom een installatie via [Homebrew](https://brew.sh/). 
Om Homebrew te installeren voer 
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` 
uit in de Terminal.
Om Python te installeren voer `brew install python3` uit.

Om de installatie te verifiëren open je de terminal en voer `python3 --version` uit. Nu zou de versie die je gedownload hebt tevoorschijn moeten komen.


### Linux
De systeeminstallatie van Python 3 werkt goed. Om Python packages te installeren moet men eerst pip installeren via
`apt install python3-pip` in de terminal.

Om de installatie te verifiëren open je de terminal en voer `python3 --version` uit. Nu zou de versie die je gedownload hebt tevoorschijn moeten komen.


## Hello World!
In deze sectie gaan we over enkele basisvaardigheden die men nodig heeft om een eerste programma te schrijven.

### Directory opstellen
Ga naar uw bureaublad en maak een nieuwe map. Noem deze bijvoorbeeld *Workshop_Python*
In deze map zullen we al onze programma's steken.
Open nu VSC.
Ga naar File > Open Folder.. 
Kies hier de map die we zonet hebben aangemaakt.

### Hello World!
Hello World is het eerste programma van elke programmeur.





## Pong
Programmeren leer je door te doen. En het is altijd leuker om iets visueel te programmeren. Daarom programmeren we nu Pong.
Doel: https://user-images.githubusercontent.com/81807266/160153440-caea3456-0ab1-49cd-9a6b-d8ab990ee676.mp4

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

Nu hebben we twee paddles nodig om mee te spelen. Deze maken we als volgt aan.
```
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
```

Een bal kan ook handig zijn
```
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1
```
