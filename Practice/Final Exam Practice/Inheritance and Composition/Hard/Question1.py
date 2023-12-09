class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)


    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()

class WeatherDisplay:
    def update(self, temperature, humidity, pressure):

        print(f"Updated display with temperature: {temperature}, humidity: {humidity}, pressure: {pressure}")


weather_station = WeatherStation()
display = WeatherDisplay()

weather_station.register_observer(display)
weather_station.set_measurements(70, 65, 30)  
