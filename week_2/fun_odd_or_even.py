import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plot
f = 0

def f(x):
  if x % 2 == 0:
    f = -1
  else:
    f = 1
  return f

xs = list(range(-5, 6))
ys = []
for x in xs:
    ys.append(f(x))

plot.bar(xs, ys)

plot.savefig('odd_even_fxplot.png')
plot.close()
