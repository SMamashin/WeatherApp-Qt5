from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from weather_ui import Ui_MainWindow
from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError
from pyowm.commons.exceptions import APIRequestError
from pyowm.utils import config as cfg
from pyowm.utils import timestamps

owm = OWM("421f5d580af9b36676c24f2ca5715278")

pyowmconfig = cfg.get_default_config()
pyowmconfig['language'] = 'ru'

Form, Window = uic.loadUiType("c:/dev/projects/weatherappgui/weather.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

# main function engine xD

def WeatherUI():
    try: # error handler by stepan for ui-app

        # line edit get
        city = form.lineEdit.text()

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

        return form.label.setText (f"                 В городе {city} температура: {int(local_temp)} °C {e_temp} \n\
                    Максимальная температура: {int(max_temp)} °C \n \
                    Минимальная температура: {int(min_temp)}°C \n \
                    Ощущается как: {int(f_like)} °C \n \
                    Скорость ветра: {int(wind)} м/c \n \
                    Давление: {int(pressure)} мм.рт.ст \n \
                    Влага: {int(moisture)} % \n \
                    По состоянию: {status} {status_emoji.get(status) or '🌍'}")

    except (NotFoundError, APIRequestError):
        e_error = "🚫"
        error = f'Возможные ошибки:\n 1. Вы допустили ошибку в написании города "{city}"\n 2. Города/страны "{city} не существует"\n3. Вы отправили пустой запрос.\n 4. Проблема с интернетом {e_error} \
            \n\nЕсли вы обнаружили ошибку, свяжитесь со мной: {" "} t.me/thetraextra'
        return form.label.setText( error )

# get function where user click on the my button

form.pushButton.clicked.connect( WeatherUI )


app.exec_()
