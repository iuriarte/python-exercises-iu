import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plot

def f(x):
  return x*x

xs = list(range(-100, 101))
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)

plot.savefig('mysqrofxplot.png')
plot.close()
