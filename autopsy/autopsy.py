import pygame, sys
import time as Time

def animate_linear(displaysurf, ptsFrom, ptsTo, time, colour):
	if len(ptsFrom) == len(ptsTo):
		top = left = sys.maxint
		bottom = right = 0
		for pt in ptsFrom:
			if pt[0] < left:
				left = pt[0]
			#end
			if pt[1] < top:
				top = pt[1]
			#end
			if pt[0] > right:
				right = pt[0]
			#end
			if pt[1] > bottom:
				bottom = pt[1]
			#end
		#end
		rw = right - left
		rh = bottom - top
		rect = pygame.Rect(top, left, rw, rh).inflate(15, 15)
		surf = displaysurf.subsurface(rect).copy()
		temp = ptsFrom[:]
		delta = []
		for i in range(0, len(ptsFrom)):
			delta.append([(ptsTo[i][0] - ptsFrom[i][0]) / float(time), (ptsTo[i][1] - ptsFrom[i][1]) / float(time)])
		#end
		sleeptime = 1.0 / time
		count = 0
		while count <= 1:
			yatemp = temp[:]
			temp = []
			for j in range(0, len(yatemp)):
				temp.append([yatemp[j][0] + delta[j][0], yatemp[j][1] + delta[j][1]])
			#end
			pygame.draw.polygon(displaysurf, colour, temp)
			pygame.display.update()
			Time.sleep(sleeptime)
			displaysurf.blit(surf, rect)
			top = left = sys.maxint
			bottom = right = 0
			for pt in temp:
				if pt[0] < left:
					left = pt[0]
					ileft = temp.index(pt)
				#end
				if pt[1] < top:
					top = pt[1]
					itop = temp.index(pt)
				#end
				if pt[0] > right:
					right = pt[0]
					iright = temp.index(pt)
				#end
				if pt[1] > bottom:
					bottom = pt[1]
					ibottom = temp.index(pt)
				#end
			#end
			rw = right - left
			rh = bottom - top
			rect = pygame.Rect(top, left, rw, rh).inflate(15, 15)
			surf = displaysurf.subsurface(rect).copy()
			count += sleeptime
		#end
	#end
#end
			
