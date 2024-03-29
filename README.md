# WeatherApp-Qt5
<img src="./source/cover_ui.jpg"  alt="error" title="cover-project">

## ___WeatherApp___ - a local project written to improve knowledge.

### ___About the project___
This application is like https://github.com/SMamashin/WeatherApp allows you to get detailed weather at the moment in any existing* city or country. 🌤

---
### ___Features of my project___ 
* Maximally open source
* Unique design
* Two versions on eel/js & only PyQt

This version is pure Python 🐍
For the UI interface I used Qt Designer 💚
---

## **Preview**
<img src="./source/ui_view.png"  alt="error" title="ui_view">


---
### ___PIP modules that I used in this* version___
* PyQt5
  * Ui
* PyOWM
  * Get weather
  * Get detailed status
  * In these variables I got detailed information
      ```python
        tg = weather.temperature("celsius")
        local_temp = tg['temp']
        f_like = tg['feels_like']
        max_temp = tg['temp_max']
        min_temp = tg['temp_min']
        wind = weather.wind()['speed']
        pressure = weather.pressure['press']
        moisture = weather.humidity
        status = weather.detailed_status
---
### ___How to build?___
To run the code you will need Python on your PC and also install a couple of modules
  * pip install pyqt5
  * pip install pyowm
    
You can also build the code in .exe using <u>Pyinstaller</u>
  * pip install pyinstaller
  * pyinstaller -F weather.py
    
Compiled .the exe will be waiting for you in the "dist" folder

---
### ___ChangeLog___
Version 5.0
 * Fix .css/.scss import
 * Build .exe
 * Icon app
 * Build msi installer
   
Version 5.5 [12.01.2024]
 * Fix bug with window
 * Try fixed favicon.ico
 * New build.exe
 * Logging in console
 * Logging in /logs/logs.txt/
 * New button {back}
   
Version before Qt - [here](https://github.com/SMamashin/WeatherAppWeb)


---
## Author
Stepan Mamashin
