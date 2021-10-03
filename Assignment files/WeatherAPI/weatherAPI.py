import network
import socket
import urequests
import utime
import machine
import ssd1306
i2c = machine.I2C(-1, machine.Pin(18), machine.Pin(19))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
def connect_Wifi():
    display.text('connecting....', 0, 0)
    display.show()
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network')
        wlan.connect('ekcp', '*hathway123*')
        while not wlan.isconnected():
            pass
    print('network config', wlan.ifconfig())
    display.text('Connected', 0, 20)
    display.show()
    utime.sleep_ms(1000)
def get_data():
    response = urequests.get("http://dataservice.accuweather.com/forecasts/v1/daily/1day/190792?apikey=Kr7TUFyK1Rhf0AfrwT9lW0O8fpNK8rLl")
    data = response.json()
    return data
def print_climate_data(data):
    for i in range(6):
        display.fill(0)
        weather = data["Headline"]
        local = weather["MobileLink"]
        date_today = weather["EffectiveDate"]
        weather_today = weather["Category"]
        display.text(local[33:43], 0, 0)
        display.text(date_today[0:11], 0, 15)
        display.text(weather_today, 0, 30)
        display.show()
        utime.sleep_ms(5000)
connect_Wifi()
while 1:
    data=get_data()
    print_climate_data(data)
