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

Om de installatie te verifiëren open je de terminal op windows (Command Prompt) en voer `py -3 --version` uit.  
Nu zou de versie die je gedownload hebt tevoorschijn moeten komen.

Voor meer informatie: [Python gebruiken op windows](https://docs.python.org/3.9/using/windows.html)

### macOS
De systeeminstallatie van Python op macOS wordt niet ondersteund. Gebruik daarom een installatie via [Homebrew](https://brew.sh/). 
Om Homebrew te installeren voer  
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`  
uit in de Terminal.

Om Python te installeren voer `brew install python3` uit.

Om de installatie te verifiëren open je de terminal en voer `python3 --version` uit. Nu zou de versie die je gedownload hebt tevoorschijn moeten komen

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

Maak een nieuw bestand en noem deze *hello.py*  
Ons eerste programma bestaat slechts uit 1 lijn:  
```python 
print('hello world!')
```  
Om deze code uit te voeren schuiven we de terminal naar boven en geven we in:  
`py hello.py` (windows)  
`python3 hello.py` (linux en mac)

### Python als rekenmachine
probeer eens:  
```python
print(5+5)
print('5+5')
```
Merk je het verschil op?

nu gaan we onze eerste variabelen declareren:
```python
x = 20
y = 'hallo' + ','
print(x)
print(y)
print(x/2)
print(y + ' mijn naam is ...')
print(x*4-2, 'is een getal')
```

Sommige wiskundige functies en constanten zitten niet standaard in Python.  
Hiervoor moet je eerst een module importeren: *math*  
Een module importeren doe je als volgt:  
```python
import math
print(math.pi)
print(math.floor(3.7))
print(math.ceil(3.7))
```

### Eerste functies
Om het nog wat interessanter te maken leren we nu werken met functies. Net zoals iemand ergens het gedrag van math.floor heeft gedefinieerd, zullen wij hetzelfde doen met onze functies.

We schrijven bijvoorbeeld een functie die de input vermenigvuldigt met 2:
```python
def maal_2(x):
    y = x*2
    return y
```
om deze functie te gebruiken zullen we de functie moeten aanroepen:
```python
print(maal_2(10))
print(maal_2(12))
```

Deze functie is natuurlijk redelijk zinloos. We maken het iets moeilijker..  
We willen de oppervlakte van een cirkel berekenen, gegeven de straal.
```python
import math

def bereken_opp(r):
    return r*r*math.pi

print(bereken_opp(2))
print(bereken_opp(3))
```

### Lussen

#### If ... Else
Deze structuur is redelijk voor de hand liggend.  
Als iets waar is, dan doe dit. In het andere geval, doe dit.
```python
if 2 < 3:
    print('2 is kleiner dan 3!')
else:
    print('2 is groter dan 3!')
```

### While
Zolang iets waar is, doe dit.
```python
i = 0
while i < 5:
    print(i)
    i = i + 1 
```

De constanten *true* en *false* worden ook wel eens gebruikt in deze context
```python
i = 0
while True:
    print(i)
    i = i + 1
```
U ziet dat de functie nooit stopt..  
Je kunt deze (gelukkig) handmatig stoppen door de toetsencombinatie Ctrl + X.

### Geneste lussen
Voer de volgende functie eens uit.  
Is de output hetgeen je verwacht had?
```python
running = True
i = 0
while running:
    if i == 6:
        running = False
    i = i + 1
```

## Pong
Programmeren leer je door te doen. En het is altijd leuker om iets visueel te programmeren. Daarom programmeren we nu Pong.
Doel: https://user-images.githubusercontent.com/81807266/160153440-caea3456-0ab1-49cd-9a6b-d8ab990ee676.mp4

Open opgave.py

Om te beginnen laden we enkele modules in.
```python
import turtle
import os
import time
```

Vervolgens maken we eerst een scherm waar het spel in gaan programmeren. 
```python
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
```python
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1
```
