# Workshop Python

## Hello World!
In deze sectie gaan we over enkele basisvaardigheden die men nodig heeft om een eerste programma te schrijven.

#### Directory opstellen
Ga naar uw bureaublad en maak een nieuwe map. Noem deze bijvoorbeeld *workshop*  
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

#### Python als rekenmachine, leren werken met variabelen en datatypes
probeer eens:  
```python
print(5+5)
print('5+5')
```
Merk je het verschil op?  
Wanneer we beiden combineren, kunnen we iets doen als:
```python
print('5+5=', 5+5)
```

De print functie zal 5+5 en '5+5' anders verwerken omdat ze van een ander datatype zijn. In wat volgt zullen we een aantal verschillende datatypes zien en hun gedrag
in verschillende contexten gaan vergelijken.

Om het simpel te houden zullen we kijken naar 4 verschillende types om data op te slaan:
| Naam  | Voorbeeld | Uitleg |
| ------------- | ------------- | ------------- |
| Integer  | 42  | Geheel getal |
| Float  | 7.32  | Decimaal getal |
| String | 'Engage' of "Engage" | Zin, kan al dan niet getallen bevatten|
| Boolean | True of False | Neemt enkel deze 2 waarden aan|

Het gedrag hiervan bestuderen zullen we experimenteel doen, have fun!:
```python
#Integers
x = 20
print(x)
print(x/2)
print(x**2)
x++
print(x)

#String
y = 'hallo' + ','
print(y)
print(y + ' mijn naam is ...')

print(x*4-2, ' is een getal')

#Booleans
z = 15
print(z<5)
print(z>12)
print(z==15) #Zie je het verschil tussen = en == ? 

```

Programmeurs zijn per definitie luie mensen, hoemeer code je kan hergebruiken of zelf niet hoeft te schrijven hoe beter! Maar hoe importeren we die code (beter gekend als een module) in onze bestanden? Hieronder zie je een voorbeeldje.

Sommige wiskundige functies en constanten zitten niet standaard in Python.  
Hiervoor moet je eerst een module importeren: *math*  
Een module importeren doe je als volgt:  
```python
import math
print(math.pi)              #De constante pi
print(math.floor(3.7))      #Naar beneden afronden
print(math.ceil(3.7))       #Naar boven afronden
```

### Eerste functies
Het zou natuurlijk vrij nutteloos zijn om exact dezelfde code steeds opnieuw te moeten schrijven, de remedie: functies! Functies zijn **losstaande** stukken code die een ingang (argument) omzetten in een uitgang (return waarde).

Net zoals iemand ergens het gedrag van math.floor heeft gedefinieerd, zullen wij hetzelfde doen met onze functies.

We schrijven bijvoorbeeld een functie die de input vermenigvuldigt met 2:
```python
def maal_2(x):  #Definitie van de functie
    y = x*2     #Gedrag van de funcite
    return y    #Return de gewenste waarde
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

***Oefening: maak een functie die de omtrek van een cirkel terug geeft met als argument de straal.***

### Lussen

#### If ... Else
Deze structuur is redelijk voor de hand liggend.  
Als iets waar is, dan doe dit. In het andere geval, doe dit.
```python
if 2 < 3:                           #Conditie
    print('2 is kleiner dan 3!')    #Indien waar doe iets
else:
    print('2 is groter dan 3!')     #Zoniet doe iets anders
```

### While
Zolang iets waar is, doe dit.
```python
i = 0
while i < 5:
    print(i)
    i = i + 1 
```

De constanten *True* en *False* worden ook wel eens gebruikt in deze context
```python
i = 0
while True:
    print(i)
    i = i + 1
```
We zien dat de lus nooit stopt..  
Je kunt deze (gelukkig) handmatig stoppen door de toetsencombinatie Ctrl + C.

### Geneste lussen
Voer de volgende functie eens uit.  
Is de output hetgeen je verwacht had?
```python
running = True
i = 0
while running:
    print(i)
    if i == 6:
        running = False
    i = i + 1
```
### For lussen
Wil je iets een bepaald aantal keren uitvoeren, een simpele manier om dit gedrag te bereiken is via for lussen.
Voer de volgende functie eens uit. Welke nummers worden er afgeprint? Is range inclusief of exclusief de laatste waarde (het argument)? 
```python
for i in range(10):
    print(i)
```

***Oefening: Schrijf de functie som_kwadraat(n) die de som van kwadraten terug geeft van 0 tot een bepaald getal n (zonder n zelf). Vb. som_kwadraat(3) = 0 + 1 + 4 = 5***
