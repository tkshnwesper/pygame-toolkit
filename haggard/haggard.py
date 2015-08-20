import pygame, sys
from pygame.locals import *
from random import randint, uniform
from math import atan, atan2, sin, cos, sqrt, pi

def haggard_aaline(displaysurf, t1, t2, maxlen, maxangle):
	ini = list(t1)
	ini2 = list(t1)
	if(t2[0] - ini[0] == 0):
		if(t2[1] - ini[1] > 0):
			theta = pi / 2.0
			#~
		else:
			theta = -pi / 2.0
			#~
		#~
	else:
		theta = atan2(t2[1] - ini[1], t2[0] - ini[0])
		#~
	while True:
		if(sqrt((t2[1] - ini2[1])**2 + (t2[0] - ini2[0])**2) <= maxlen):
			pygame.draw.aaline(displaysurf, (randint(0, 255), randint(0, 255), randint(0, 255)), ini2, t2)
			return
			#~
		randangle = uniform(-maxangle, maxangle)
		length = randint(1, maxlen)
		finalangle = theta + randangle
		ini = ini2[:]
		ini2[1] = ini[1] + length * sin(finalangle)
		ini2[0] = ini[0] + length * cos(finalangle)
		pygame.draw.aaline(displaysurf, (randint(0, 255), randint(0, 255), randint(0, 255)), ini, ini2)
		if(t2[0] - ini2[0] == 0):
			if(t2[1] - ini2[1] > 0):
				theta = pi / 2.0
				#~
			else:
				theta = -pi / 2.0
				#~
			#~
		else:
			theta = atan2(t2[1] - ini2[1] , t2[0] - ini2[0])
			#~
		#~
	#~

def haggard_aaline_colour(displaysurf, t1, t2, maxlen, maxangle, colour):
	ini = list(t1)
	ini2 = list(t1)
	if(t2[0] - ini[0] == 0):
		if(t2[1] - ini[1] > 0):
			theta = pi / 2.0
			#~
		else:
			theta = -pi / 2.0
			#~
		#~
	else:
		theta = atan2(t2[1] - ini[1], t2[0] - ini[0])
		#~
	while True:
		if(sqrt((t2[1] - ini2[1])**2 + (t2[0] - ini2[0])**2) <= maxlen):
			pygame.draw.aaline(displaysurf, colour, ini2, t2)
			return
			#~
		randangle = uniform(-maxangle, maxangle)
		length = randint(1, maxlen)
		finalangle = theta + randangle
		ini = ini2[:]
		ini2[1] = ini[1] + length * sin(finalangle)
		ini2[0] = ini[0] + length * cos(finalangle)
		pygame.draw.aaline(displaysurf, colour, ini, ini2)
		if(t2[0] - ini2[0] == 0):
			if(t2[1] - ini2[1] > 0):
				theta = pi / 2.0
				#~
			else:
				theta = -pi / 2.0
				#~
			#~
		else:
			theta = atan2(t2[1] - ini2[1] , t2[0] - ini2[0])
			#~
		#~
	#~

def haggard_aacircle(displaysurf, center, radius, delradius, numpts):
	delangle = 2 * pi / numpts
	angle = -pi
	xlen = randint(-delradius, delradius)
	hypo = radius + xlen
	fx = x1 = x2 = center[0] + hypo * cos(angle)
	fy = y1 = y2 = center[1] + hypo * sin(angle)
	count = 0
	while(angle <= pi):
		angle += delangle
		count += 1
		xlen = randint(-delradius, delradius)
		hypo = radius + xlen
		x1 = x2
		y1 = y2
		x2 = center[0] + hypo * cos(angle)
		y2 = center[1] + hypo * sin(angle)
		if(count == numpts - 1):
			pygame.draw.aaline(displaysurf, (randint(0, 255), randint(0, 255), randint(0, 255)), (x2, y2), (fx, fy))
			break
			#~
		else:
			pygame.draw.aaline(displaysurf, (randint(0, 255), randint(0, 255), randint(0, 255)), (x1, y1), (x2, y2))
			#~
		#~
	#~

def haggard_aacircle_colour(displaysurf, center, radius, delradius, numpts, colour):
	delangle = 2 * pi / numpts
	angle = -pi
	xlen = randint(-delradius, delradius)
	hypo = radius + xlen
	fx = x1 = x2 = center[0] + hypo * cos(angle)
	fy = y1 = y2 = center[1] + hypo * sin(angle)
	count = 0
	while(angle <= pi):
		angle += delangle
		count += 1
		xlen = randint(-delradius, delradius)
		hypo = radius + xlen
		x1 = x2
		y1 = y2
		x2 = center[0] + hypo * cos(angle)
		y2 = center[1] + hypo * sin(angle)
		if(count == numpts - 1):
			pygame.draw.aaline(displaysurf, colour, (x2, y2), (fx, fy))
			break
			#~
		else:
			pygame.draw.aaline(displaysurf, colour, (x1, y1), (x2, y2))
			#~
		#~
	#~

def haggard_aacircle_fill(displaysurf, center, radius, delradius, numpts, colour):
	pts = []
	delangle = 2 * pi / numpts
	angle = -pi
	xlen = randint(-delradius, delradius)
	hypo = radius + xlen
	fx = x1 = x2 = center[0] + hypo * cos(angle)
	fy = y1 = y2 = center[1] + hypo * sin(angle)
	pts.append((fx, fy))
	count = 0
	while(angle <= pi):
		angle += delangle
		count += 1
		xlen = randint(-delradius, delradius)
		hypo = radius + xlen
		x2 = center[0] + hypo * cos(angle)
		y2 = center[1] + hypo * sin(angle)
		if(count == numpts - 1):
			break
			#~
		else:
			pts.append((x2, y2))
			#~
		#~
	pygame.draw.polygon(displaysurf, colour, pts)
	#~

def haggard_rect_fill(displaysurf, rect, maxlen, maxangle, colour):
	tf = [[rect.left + rect.width, rect.top], [rect.left + rect.width, rect.top + rect.height], [rect.left, rect.top + rect.height], [rect.left, rect.top]]
	ini = [rect.left, rect.top]
	pts = []
	for rpt in tf:
		ini2 = ini[:]
		if(rpt[0] - ini[0] == 0):
			if(rpt[1] - ini[1] > 0):
				theta = pi / 2.0
				#~
			else:
				theta = -pi / 2.0
				#~
			#~
		else:
			theta = atan2(rpt[1] - ini[1], rpt[0] - ini[0])
			#~
		while True:
			
			if(sqrt((rpt[1] - ini2[1])**2 + (rpt[0] - ini2[0])**2) <= maxlen):
				break
				#~
			randangle = uniform(-maxangle, maxangle)
			length = randint(1, maxlen)
			finalangle = theta + randangle
			ini = ini2[:]
			ini2[1] = ini[1] + length * sin(finalangle)
			ini2[0] = ini[0] + length * cos(finalangle)
			pts.append(tuple(ini2))
			if(rpt[0] - ini2[0] == 0):
				if(rpt[1] - ini2[1] > 0):
					theta = pi / 2.0
					#~
				else:
					theta = -pi / 2.0
					#~
				#~
			else:
				theta = atan2(rpt[1] - ini2[1] , rpt[0] - ini2[0])
				#~
			#~
		ini = rpt[:]
		#~
	pygame.draw.polygon(displaysurf, colour, pts)
	#~
