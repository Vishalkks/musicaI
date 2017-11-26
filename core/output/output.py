import pygame.midi
import time
import SharedArray as sa
def sendOutput():
	#puts the output to the keyboard, gives the midi output back after reading from shared memory
	#poll shared mem
	#notesToPlay = [[48,100],[48,100],[48,100],[48,100]]
	while(notesToPlay[0] == 0.0):
		continue
	print(notesToPlay)
	while(not(notesToPlay[0] == -1.0)):
		for i in range(4):
			print(notesToPlay[i])
			out.note_on(int(notesToPlay[i]),velocity = 100)
			time.sleep((60/tempo))
			print("OUT")
			out.note_off(int(notesToPlay[i]),velocity = 0)
		
if __name__ == "__main__":
	tempo = 150.0
	pygame.midi.init()
	notesToPlay = sa.attach("shm://notes")
	for i in range(0,len(notesToPlay)):
		notesToPlay[i] = 0.0
	out = pygame.midi.Output(2)
	sendOutput()	
