## Pong
Programmeren leer je door te doen. En het is altijd leuker om iets visueel te programmeren. Daarom programmeren we nu Pong.
Doel: [video](https://user-images.githubusercontent.com/81807266/160153440-caea3456-0ab1-49cd-9a6b-d8ab990ee676.mp4)


Maak een nieuw bestand aan en noem deze *pong.py*.  
Kopieer de inhoud van *pong.py* uit deze github repository en plak deze in het bestand.

Om te beginnen laden we de module turtle in. Dit zal ons helpen om Pong visueel voor te stellen.
```python
import turtle
```

Vervolgens maken we eerst een scherm waarin we het spel in gaan programmeren. 
```python
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
``` 

Elk spel heeft iets nodig zoals een main game loop. Dit is het hart van het spel waar alle logica en algoritmen achter zitten. Omdat we het simpel gaan houden wil dit zeggen dat het deze lus steeds zal doorlopen en alles uitvoeren. Voor meer info [Game Loop](https://www.informit.com/articles/article.aspx?p=2167437&seqNum=2#:~:text=The%20game%20loop%20is%20the,is%20known%20as%20a%20frame)
```python
while True:
    wn.update()
```
Wanneer je dit programmaatje uitvoert, krijg je een zwart scherm met breedte 800 en hoogte 600 en coordinaten (0,0) in het centrum.

Nu hebben we twee paddles nodig om mee te spelen. Deze maken we als volgt aan. Aangezien dit vooral setup is en je hier niet zoveel mee bijleert, kan je deze code gewoon copy-pasten. (Een tweede paddle volledig analoog)
```python
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
```
Voer dit programmaatje nog eens uit en kijk wat er verandert is en of het voldoet aan de verwachtingen. Dit is heel belangrijk om fouten te vinden.

Een bal kan ook handig zijn en wordt analoog aangemaakt zoals de paddles.
```python
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
```

Nu beginnen we aan het echte werk. Er zijn 2 paddles en een bal. Hoe gaan we ze laten bewegen?
```python
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
```
We hebben een functie nodig die paddle a omhoog laat gaan. We willen dat deze opgeroepen wordt telkens wanneer een toets wordt ingedrukt. We gaan de functie dus binden aan een toets op het toetsenbord.
```python
wn.listen()
wn.onkeypress(paddle_a_up, "z")
```
Test it!  
Je zal zien dat je de paddle uit het scherm kan laten bewegen. Dit is niet de bedoeling. Hoe los je dit op?  
Doe dit nu ook om de paddle naar beneden te laten gaan. En dan ook voor paddle b.

Wat we nu willen doen is de bal een snelheid geven.  
We gaan deze splitsen in een x- en y-movement.  
We gaan dus naar het stukje code waar we de bal aangemaakt hebben en geven deze een beginsnelheid.  
Je kan spelen met deze nummers om met de snelheid te spelen.
```python
ball.dx = 1
ball.dy = 1
```

Nu staat alles klaar om de logica van het spel te implementeren. We gaan terug naar de main game loop.
Wat moet er steeds gebeuren tijdens een game loop?
- Alle objecten (turtles) moeten getekend worden
- Fysica toepassen op het spel:
    * De posities moeten geüpdatet worden (rekening houdend met de snelheid)
    * Controleren of er botsingen gebeuren tussen objecten 
    * Zo ja, de snelheden en richtingen aanpassen

Beginnen met het begin, de posities aanpassen rekening houdend met de snelheid
```python
ball.setx(ball.xcor() + ball.dx)
ball.sety(ball.ycor() + ball.dy)
```
Test it!  
De bal vliegt uit het scherm!

We willen echter dat de bal botst op de randen.
```python
    # Border checking
    
    # Top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
```
Test it!  
Maak een analoge conditie voor de onderkant.  

Wanneer de bal voorbij de paddles gaan willen we dat er een punt wordt gescoord en dat de bal terug naar het centrum gaat.
```python
    # right
    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.dx *= -1
```
Test it!  
Maak opnieuw een analoge conditie voor de linkerzijde.

Stap 2: Controleren of er botsingen gebeuren tussen objecten
```python
    # Paddle and ball collisions
    if ball.dx < 0 and ball.xcor() < -330 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
    
    elif ball.dx > 0 and ball.xcor() > 330 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
```
Test it!  
Proficiat! Je hebt nu een werkend spel!  

Om het spel competitief te maken kunnen we ook een scorebord bijhouden.  
Om de score op het scherm te schrijven gebruiken we opnieuw een turtle.  
Deze code kan je copy-pasten.
```python
# Text: Score
txt_score = turtle.Turtle()
txt_score.speed(0)
txt_score.shape("square")
txt_score.color("white")
txt_score.penup()
txt_score.hideturtle()
txt_score.goto(0, 260)
txt_score.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
```
Het scorebord staat nu vast op 0:0.  
Het is natuurlijk de bedoeling dat we scores bijhouden en deze ook updaten wanneer een punt wordt gemaakt.   
We houden dus twee variabelen bij.
```python
# Score
score_a = 0
score_b = 0
```

Pas de game loop aan zodat de scores worden geupdatet (Dit zal gebeuren in borderchecking left en right).  

Om de juiste score te tekenen kan je volgende code gebruiken.
```python
pen.clear()
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
```

Proficiat! Het spel is volledig af!  
Nu is er nog een mogelijkheid om wat leuke extraatjes toe te voegen.  
Denk maar aan:
- Geluid bij een botsing toevoegen
- Tekst om een het spel af te sluiten ('Press Q to quit')
- Een obstakel toevoegen dat het wat moeilijker wordt
- Een algoritme schrijven voor paddle_b zodat je ook singleplayer kan spelen
- De bal laten versnellen bij contact met paddle zodat het spel gradueel moeilijker wordt

Voorbeeld 1:
Om telkens wanneer de bal botst een geluidje te laten afspelen kan je de module os inladen en volgende code gebruiken
```python
import os
```
aplay voor Linux, afplay voor macOS
```python
os.system("aplay -q bounce.wav&")
```
voor windows
```python
import winsound
winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
```

Voorbeeld 2:
Nu blijft de game loop eeuwig doorgaan en is er geen andere mogelijkheid dan het "hard" te sluiten, we willen dit ook manueel kunnen afsluiten door een keybinding te maken met het toetsenbord
Het plan is dus dat de game loop blijft doorgaan zolang de toets niet is ingedrukt. We kunnen dus een running conditie aanmaken.
```python
running = True
```
De game loop verandert nu naar:
```python
while running:
```
Om running naar False te kunnen zetten, moeten we een toets binden aan een functie die running op False zet.
```python
def quit():
    global running
    running = False

wn.onkeypress(quit, "q")
```
Nu wil je de gebruiker ook laten weten dat dit een mogelijkheid is. Dit kan je doen door het op het scherm te schrijven.
```python
# Text: Quit
txt_quit = turtle.Turtle()
txt_quit.speed(0)
txt_quit.shape("square")
txt_quit.color("white")
txt_quit.penup()
txt_quit.hideturtle()
txt_quit.goto(0, -280)
txt_quit.write("Press q to quit", align="center", font=("Courier", 24, "normal"))
```
