# http://docs.cython.org/en/latest/src/userguide/wrapping_CPlusPlus.html

import rect

x0, y0, x1, y1 = 1,2,3,4
rect_obj = rect.PyRectangle(x0, y0, x1, y1)

print(dir(rect_obj))

ar = rect_obj.get_area()
print("Area: ", ar)

sz = rect_obj.get_size()
print("Size: ", sz)

mv = rect_obj.move(x0, y0)
print("Move: ", mv)