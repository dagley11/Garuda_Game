#!/usr/bin/env python
"""
This simple example is used for the line-by-line tutorial
that comes with pygame. It is based on a 'popular' web banner.
Note there are comments here, but for the full explanation,
follow along in the tutorial.
"""

#Import Modules
import os, pygame, random, Graph as G
from pygame.locals import *
from pygame.compat import geterror
if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')

main_dir = os.path.split(os.path.abspath(__file__))[0]
print main_dir
data_dir = os.path.join(main_dir, 'Player_Cards')

#functions to create our resources
def load_image(name, colorkey=None):
	fullname = os.path.join(data_dir, name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error:
		print ('Cannot load image:', fullname)
		raise SystemExit(str(geterror()))
	image = image.convert()
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	return image, image.get_rect()
						   



def writer(word,pos,clean=True):
	#background.fill(pygame.Color("black"))	
	if clean==True:
		background.blit(eraser, (510,430))	
		screen.blit(background, (0, 0))
	pygame.display.flip()	
	color=(0,0,0)	
	font = pygame.font.Font(None, 24)
	text = font.render(word, 0, color)
	textpos = text.get_rect(topleft=(pos))
	background.blit(text, textpos)		
	screen.blit(background, (0, 0))
	pygame.display.flip()	

  
def main():

	"""this function is called when the program starts.
	   it initializes everything it needs, then runs in
	   a loop until the function returns."""
#Set global variables
	#global item_sprites
	#global score
	#global capn
	#global sandwich
	global background
	global stuff
	global screen
	global start_screen
	global eraser
	start = False

#Initialize Everything
	pygame.init()
	screen = pygame.display.set_mode((900, 580))
	pygame.display.set_caption('Garuda Game')
	speed = 1
	

#Create The Backgound
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	

#Prepare Game Objects
	clock = pygame.time.Clock()
	#whiff_sound = load_sound('whiff.wav')
	#punch_sound = load_sound('punch.wav')
	#chimp = Chimp()
	#item = Item()
	#item_sprites = pygame.sprite.Group()
	#item_sprites.add(item)
	demon = 100
#Main Loop
	going = True
	cnt = 0
	speed = 1
	#sprites = item_sprites.sprites()
	time = 0
	avail=[]
	imgs=['A.png','B.png','C.png','D.png','E.png','F.png','G.png','H.png','I.png','J.png','K.png','L.png','M.png','N.png','O.png','P.png','Q.png','R.png','S.png','T.png','U.png','V.png','W.png','X.png','Y.png','Z.png','AA.png','AB.png','AC.png','AD.png','AE.png','AF.png','AG.png','AH.png','AI.png','AJ.png','AK.png','AL.png','AM.png','AN.png','AO.png','AP.png','AQ.png','AR.png','AS.png','AT.png','AU.png','AV.png','AW.png','AX.png','AY.png','AZ.png','BA.png','BB.png','BC.png','BD.png','BE.png','BF.png','BG.png','BH.png']
	random.shuffle(imgs)
	avail.append(imgs.pop(0))
	avail.append(imgs.pop(0))
	avail.append(imgs.pop(0))
	while True:
		pygame.mouse.set_visible(1)
		start_screen = pygame.image.load('back.jpg')
		eraser = pygame.image.load('Eraser.png')
		background.blit(start_screen, (0,0))
		#Display The Background
		screen.blit(background, (0, 0))
		events = pygame.event.get()
		pygame.display.flip()
		while going:			
			clock.tick()			
			for event in events:			
				if event.type == QUIT:
					going = False
			for i in range(50):
				if i == 0:
					im1 = pygame.image.load(data_dir+"/"+avail[0])
					im2 = pygame.image.load(data_dir+"/"+avail[1])
					im3 = pygame.image.load(data_dir+"/"+avail[2])
					background.blit(im1,(50,10))
					background.blit(im2,(350,10))
					background.blit(im3,(650,10))
					screen.blit(background, (0, 0))
					pygame.display.flip()
				if i not in G.pract:
					day = i+1 
					inp1= "Day " + str(day) +":"
					writer(inp1,(520,420))
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[0],(520,440),False)
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[1],(520,460),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[2],(520,480),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[3],(520,500),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[4],(520,520),False)	 					
					while G.out == 'True':
						rsp=raw_input("Please enter a result ex. p1 (-g) (a:f,a:d,-d:j) >>> ")
						if rsp=='next':
							break
						elif rsp=='':
							continue
						elif rsp=='display':
							inp1= "p1 "+ str(G.G1.nodes())+" "+str(G.G1.edges())
							inp2= "p2 "+ str(G.G2.nodes())+" "+str(G.G2.edges())
							inp3= "p3 "+ str(G.G3.nodes())+" "+str(G.G3.edges())
							inp4= "p4 "+ str(G.G4.nodes())+" "+ str(G.G4.edges())
							print inp1
							print inp2
							print inp3
							print inp4
						elif rsp=='scores':
							try:
								G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4) 
							except G.nx.NetworkXError:
								print "issue with one of the graphs. Likely one is disconnected."
					
						elif rsp[0]=='w':
							if rsp == 'w1':
								G.w1+=.05 
							if rsp == 'w2':
								G.w2+=.05 
							if rsp == 'w3':
								G.w3+=.05 
							if rsp == 'w4':
								G.w4+=.05			   						
						elif rsp[0]=='p':
							try:
								cl=G.process_meta(rsp)
								#print avail
								#print cl							
								tagged=[]
								for x in cl:
									if x not in avail:
										tagged.append(x)
								for x in tagged:
									cl.remove(x)
								for e in range(len(cl)):
									if len(imgs)>0:
										ind=avail.index(cl[e])
										avail[ind]=imgs.pop(0)
										im = pygame.image.load(data_dir+"/"+avail[ind])
										x=50+ind*300
										background.blit(im,(x,10))
										screen.blit(background, (0, 0))
										pygame.display.flip()
																														
									
							except:
								print "Invalid input, please try again."
						else:
							print "Invalid input, please try again."			

				elif i == 14:
					writer("Boston Invite!!",(520,420))
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[0],(520,440),False)
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[1],(520,460),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[2],(520,480),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[3],(520,500),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[4],(520,520),False)		 
				elif i == 29:
					writer("Elite-Select Challenge!!",(520,420))
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[0],(520,440),False)
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[1],(520,460),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[2],(520,480),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[3],(520,500),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[4],(520,520),False)	 
				elif i == 44:
					writer("Top Select!!",(520,420))
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[0],(520,440),False)
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[1],(520,460),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[2],(520,480),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[3],(520,500),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[4],(520,520),False)	
				elif i == 49:
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[0],(520,440),False)
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[1],(520,460),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[2],(520,480),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[3],(520,500),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[4],(520,520),False)	
				else:
					writer("Practice!!",(520,420))
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[0],(520,440),False)
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[1],(520,460),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[2],(520,480),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[3],(520,500),False)	 
					writer(G.algorithm(G.w1,G.w2,G.w3,G.w4,G.G1,G.G2,G.G3,G.G4)[4],(520,520),False)		 
			break
		

							
	pygame.quit()

#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__':
	main()
else:
	print __name__
