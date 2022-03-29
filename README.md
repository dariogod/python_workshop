# Workshop Python

## Hello World!
In deze sectie gaan we over enkele basisvaardigheden die men nodig heeft om een eerste programma te schrijven.

#### Directory opstellen
Ga naar uw bureaublad en maak een nieuwe map. Noem deze bijvoorbeeld *Workshop_Python*  
In deze map zullen we al onze programma's steken.  
Open nu VSC.  
Ga naar File > Open Folder..  
Kies hier de map die we zonet hebben aangemaakt.

#### Hello World!
Hello World is het eerste programma van elke programmeur.

Maak een nieuw bestand en noem deze *hello.py*  
Ons eerste programma bestaat slechts uit 1 lijn:  
```python 
print('hello world!')
```  
Om deze code uit te voeren schuiven we de terminal naar boven en geven we in:  
`py hello.py` (windows)  
`python3 hello.py` (linux en mac)

#### Python als rekenmachine
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