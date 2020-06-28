#!/usr/bin/env python3

import math
import imageio
import matplotlib.pyplot as plt
import numpy as np

im = imageio.imread('icon-app-clip-codes.png')
# it is a grayscale image.

def process_circle(radius):
    circle = []
    for phi in range(0, 360*radius):
        x = radius * math.cos(math.radians(phi/radius)) + 400
        y = radius * math.sin(math.radians(phi/radius)) + 400
        pixel = im[int(x),int(y)]
#        im[int(x),int(y)] = 128
        if pixel == ref1:
            val = 1
        elif pixel == ref2:
            val = 2
        else:
            val = 0
        circle.append(val)
    # shift to first stop
    stopPos = circle.index(0)
    circle = circle[stopPos:] + circle[0:stopPos]

    circleEval = list()
    for i in circle:
        if len(circleEval) == 0:
            # first item
            circleEval.append( (i, 1) )
            continue
        else:
            if circleEval[-1][0] == i:
                circleEval[-1] = (i, circleEval[-1][1] + 1)
            else:
                circleEval.append( (i, 1) )
    referencesize = np.mean([y for (x,y) in circleEval if x == 0])
    for i in range(len(circleEval)):
        circleEval[i] = (circleEval[i][0], circleEval[i][1] / referencesize)
    return circleEval

# 5th circle:  32px from border (outer circle)
# 4th circle:  80px
# 3rd circle: 128px
# 2nd circle: 176px
# 1st circle: 224px (inner circle)

# reference colors from center point
# color 1 @ 400,400
ref1 = im[400,400]
# color 2 @ 318,400
ref2 = im[318,400]

values = [2, 5, 8, 11, 14, 17]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

print("process circle 1")
x, y = zip(*process_circle(176))
ax.scatter(x,y, color="green", label='1')

print("process circle 2")
x, y = zip(*process_circle(224))
ax.scatter(x,y, color="yellow", label='2')

print("process circle 3")
x, y = zip(*process_circle(272))
ax.scatter(x,y, color="black", label='3')

print("process circle 4")
x, y = zip(*process_circle(320))
ax.scatter(x,y, color="blue", label='4')

print("process circle 5")
#imageio.imwrite('pixels.png', im[:, :])

x, y = zip(*process_circle(368))
ax.scatter(x,y, color="red", label='5')
#plt.show()
