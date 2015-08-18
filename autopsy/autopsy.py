import pygame, sys, time

def animate_linear(displaysurf, ptsFrom, ptsTo, timems, colour):
	if len(ptsFrom) == len(ptsTo):
		delta = []
		for i in range(0, len(ptsFrom)):
			delta.append([(ptsTo[i][0] - ptsFrom[i][0]) / float(timems), (ptsTo[i][1] - ptsFrom[i][1]) / float(timems)])
		#end
		temp = ptsFrom[:]
		count = 0
		sleeptime = 1.0 / timems
		while count <= 1:
			top = left = sys.maxint
			bottom = right = 0
			for pt in temp:
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
			rect = pygame.Rect(left, top, rw, rh).inflate(3, 3)
			print rect.left, rect.top, rect.height, rect.width
			surf = displaysurf.subsurface(rect).copy()
			pygame.draw.polygon(displaysurf, colour, temp)
			time.sleep(sleeptime)
			displaysurf.blit(surf, rect)
			for j in range(0, len(temp)):
				temp[j] = ([temp[j][0] + delta[j][0], temp[j][1] + delta[j][1]])
			#end
			count += sleeptime
		#end
	#end
#end
