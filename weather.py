import time
import datetime
import configparser
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication
from gui.weather_ui import Ui_MainWindow
from gui.weather_ui import label
from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError
from pyowm.commons.exceptions import APIRequestError
from pyowm.utils import config as cfg
from pyowm.utils import timestamps

owm = OWM(" ")
pyowmconfig = cfg.get_default_config()
pyowmconfig['language'] = 'ru'

Form, Window = uic.loadUiType('gui/weather.ui')
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
log = configparser.ConfigParser()
states = ['search', 'success', 'OWM_error', 'back']
# main function engine xD

def WeatherUI():
    local_time = datetime.datetime.now(tz=None)
    log = open("logs/logs.txt", "a+")
    try: # error handler by stepan for ui-app
        # line edit get\
        city = form.lineEdit.text()
        print(f"{states[0]} -> {city}")
        log.write(f"\n{local_time} - {states[0]} -> {city}")
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        weather = observation.weather
        tg = weather.temperature("celsius")
        local_temp = tg['temp']
        f_like = tg['feels_like']
        max_temp = tg['temp_max']
        min_temp = tg['temp_min']
        e_temp = "🌡"
        e_status = " "
        wind = weather.wind()['speed']
        pressure = weather.pressure['press']
        moisture = weather.humidity
        status = weather.detailed_status 

        # <--saxon-- 
        status_emoji = {
                "ясно": "☀️",
                "переменная облачность": "🌤",
                "облачно с прояснениями": "🌥",
                "небольшой дождь": "🌦",
                "пасмурно": "☁️",
                "небольшая облачность": "☁️",
                "дождь": "🌧",
                "мгла": "💨"
            }
        # -- saxon --> # 
        print(f"{states[1]} -> {city}")
        log.write(f"\n{local_time} - {states[1]}")
        return form.label.setText (f"                 В городе {city} температура: {int(local_temp)} °C {e_temp} \n\
                    Максимальная температура: {int(max_temp)} °C \n \
                    Минимальная температура: {int(min_temp)}°C \n \
                    Ощущается как: {int(f_like)} °C \n \
                    Скорость ветра: {int(wind)} м/c \n \
                    Давление: {int(pressure)} мм.рт.ст \n \
                    Влага: {int(moisture)} % \n \
                    По состоянию: {status} {status_emoji.get(status) or '🌍'}")
    except (NotFoundError, APIRequestError):
        print(states[2])
        log.write(f"\n{local_time} - {states[2]}")
        e_error = "🚫"
        error = f'Возможные ошибки:\n 1. Вы допустили ошибку в написании города "{city}"\n 2. Города/страны "{city} не существует"\n3. Вы отправили пустой запрос.\n 4. Проблема с интернетом {e_error} \
            \n\nЕсли вы обнаружили ошибку, свяжитесь со мной: {" "} t.me/thetraextra'
        return form.label.setText( error )

def BtnBack():
    log = open("logs/logs.txt", "a+")
    local_time = datetime.datetime.now(tz=None)
    print(states[3])
    log.write(f"\n{local_time} - {states[3]}")
    return form.label.setText( label )

# get function where user click on the my button
form.pushButton.clicked.connect( WeatherUI )
form.pushButton_2.clicked.connect( BtnBack )
app.exec_()
