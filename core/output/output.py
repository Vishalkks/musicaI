import time
import SharedArray as sa
def sendOutput():
	#puts the output to the keyboard, gives the midi output back after reading from shared memory
	#poll shared mem
	noteToPlay = sa.attach("shm://notes")
	#notesToPlay = [[48,100],[48,100],[48,100],[48,100]]
	for note,velo in notesToPlay:
		out.note_on(note,velocity = velo)
		time.sleep((60/tempo) * 1000)
		out.note_off(note,velocity = 0)
		
if __name__ == "main":
	tempo = 120
	pygame.midi.init()
	out = pygame.midi.Output(2)
	sendOutput()	
