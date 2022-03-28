# Workshop Python - vooraf

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

Om de installatie te verifiëren open je de terminal op windows (Command Prompt) en voer `py -3 --version` uit. Nu zou de versie die je gedownload hebt tevoorschijn moeten komen.

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
