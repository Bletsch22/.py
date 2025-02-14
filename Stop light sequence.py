#modules
import time
from itertools import cycle

#defining lights in a list
lights = [("Green", 2),("yellow", 0.5),("Red", 2 )]

colors = cycle(lights)

#printing stop light sequence in a infinite loop.
while True:
  c,s = next(colors)
  print(c)
  time.sleep(s)