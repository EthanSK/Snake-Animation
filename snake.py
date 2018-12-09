from math import*
import numpy as np
import time
import random
import sys


screenWidth = 150
sineArg = 0
period = 100
xShift = 20
snakePos = round(screenWidth/2)
randAmplitude = 0.0
while (True):
	#snakePos += random.randrange(-1,2)
	randAmplitude += random.uniform(-0.05, 0.05)
	randAmplitude = min(abs(randAmplitude), 0.5)
	sineOut = np.sin((2 * np.pi * sineArg)/period)
	snakePos = sineOut*sineOut * screenWidth * randAmplitude + xShift

	sineArg += 1
	snakePos = min(max(snakePos, 0), screenWidth)
	
	#sys.stdout.flush()
	#print(snakePos, randAmplitude)
	for i in range(0, screenWidth + 1):
		if (i != int(snakePos)):
			sys.stdout.write(" ")
		else:
			sys.stdout.write("(OHO)")
	time.sleep(0.08)
	sys.stdout.write("\n")
	sys.stdout.flush()
