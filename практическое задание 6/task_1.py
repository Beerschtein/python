import time


class TrafficLight:
    __color = 'red'

    def running(self):
        print('Светофор включен')

        self.__color = 'red'
        print(f'{self.__color}')
        time.sleep(7)

        self.__color = 'yellow'
        print(f'{self.__color}')
        time.sleep(2)

        self.__color = 'green'
        print(f'{self.__color}')
        time.sleep(4)

        while True:
            self.running()


traff_light = TrafficLight()
print(traff_light.running())

