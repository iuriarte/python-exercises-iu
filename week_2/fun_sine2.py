import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plot
import math as math
from numpy import arange

f = 0

def f(x):
  return math.sin(x)

xs = arange(-5, 6, 0.1)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)

plot.savefig('sine2_of_x_plot.png')
plot.close()
