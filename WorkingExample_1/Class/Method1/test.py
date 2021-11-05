# http://ovainola.github.io/jekyll/update/2016/08/07/Wrapping-C++.html

import pyCar

car = pyCar.PyCar(b"Volkwagen", b"Passat", 2007, 120)

speed = car.get_speed()
print('Speed: ', speed)

car.set_car_speed(12)

speed = car.get_speed()
print('Speed: ', speed)