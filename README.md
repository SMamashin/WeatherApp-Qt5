# WeatherApp-Qt5
<img src="./images/cover_ui.jpg"  alt="error" title="cover-project">

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
  ```
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
## Author
Stepan Mamashin
