import pygame, sys, math, thread

_displaysurfacecopy = ''

def updateDisplaySurface(dispsurf):
	global _displaysurfacecopy
	_displaysurfacecopy = dispsurf
#end

refresh_lock = thread.allocate_lock()

def refreshDisplaySurface(displaysurf, surf, rect):
	if not refresh_lock.acquire(False):
		return
	#end
	pygame.time.wait(10)
	displaysurf.blit(surf, rect)
	refresh_lock.release()
#end

def collisionCorrection(displaysurf, animationStack, FPS):
	#~ sleeptime = int(math.ceil(1000.0 / FPS))
	sleeptime = 1
	while True:
		astack = animationStack[:]
		if astack != []:
			obj = astack.pop()
			collisionList = obj.collidelistall(astack)
			if collisionList != []:
				unionRect = obj.unionall([astack[r] for r in collisionList]).inflate(10, 10)
				if unionRect.left < 0:
					unionRect.left = 0
				#end
				if unionRect.right < 0:
					unionRect.right = 0
				#end
				if unionRect.top < 0:
					unionRect.top = 0
				#end
				if unionRect.bottom < 0:
					unionRect.bottom = 0
				#end
				surf = _displaysurfacecopy.subsurface(unionRect)
				displaysurf.blit(surf, unionRect)
				refreshDisplaySurface(displaysurf, surf, unionRect)
			#end
		#end
		pygame.time.wait(sleeptime)
	#end
#end

def animate_linear(displaysurf, animationStack, ptsFrom, ptsTo, timems, colour):
	if len(ptsFrom) == len(ptsTo):
		delta = []
		for i in range(0, len(ptsFrom)):
			delta.append([(ptsTo[i][0] - ptsFrom[i][0]) / float(timems), (ptsTo[i][1] - ptsFrom[i][1]) / float(timems)])
		#end
		temp = ptsFrom[:]
		sleeptime = int(math.ceil(1000.0 / timems))
		while True:
			reached = []
			for i in range(0, len(ptsFrom)):
				if abs(ptsTo[i][0] - temp[i][0]) > abs(delta[i][0]) or abs(ptsTo[i][1] - temp[i][1]) > abs(delta[i][1]):
					break
				#end
				else:
					reached.append(True)
				#end
			#end
			if len(reached) == len(ptsFrom):
				break
			#end
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
			collisionIndex = rect.collidelistall(animationStack)
			animationStack.append(rect)
			if collisionIndex == []:
				surf = _displaysurfacecopy.subsurface(rect).copy()
			#end
			pygame.draw.polygon(displaysurf, colour, temp)
			pygame.time.wait(sleeptime)
			if collisionIndex == []:
				displaysurf.blit(surf, rect)
			#end
			for j in range(0, len(temp)):
				temp[j] = ([temp[j][0] + delta[j][0], temp[j][1] + delta[j][1]])
			#end
			animationStack.remove(rect)
		#end
	#end
#end
