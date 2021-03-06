from os import listdir
from pprint import pprint
import pygame, random
import pygame.midi
from pygame.locals import *
import time

rules = {}
NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
note2num = {'C':48,'D':50,'E':52,'F':53,'G':55,'A':57,'B':59,'C1':60,'D1':62,'E1':64,'F1':65,'G1':67,'A1':69,'B1':71}
tempo = None
time_interval = None

def initTempo():
	global tempo, time_interval
	tempo = 120.0#int(raw_input("Enter desired tempo: "))
	time_interval = float(1000*60/tempo)


def populateRules():
    global rules
    files = [x for x in listdir("../rules") if '~' not in x]
    for fileName in files:
        with open ("../rules/"+fileName) as f:
            if fileName not in rules:
                rules[fileName] = {}
            for line in f.readlines():
                line = line.strip("\n")
                rightNote = line.split(":")[0]
                leftChord = line.split(":")[1].split(" ")
                if rightNote not in rules[fileName]:
                    rules[fileName][rightNote] = []
                rules[fileName][rightNote].append(leftChord)


def getMidiInput():						#gets midi input, and converts to note
	note = None
	vel = None
	chords = None
	bar_start = None
	next_bar = None
	next_bar_count = None
	hasStarted = False
	prevChord = None
	barUpdated = False
	pygame.midi.init()
	input_id = 3
	i = pygame.midi.Input( input_id )
	#    print pygame.midi.get_device_info(3)
	while not hasStarted:
		if(i.poll()):
			midi_events = i.read(1)
			if midi_events[0][0][0] == 144 :
				hasStarted = True
				bar_start = midi_events[0][1] - time_interval/2
				next_bar = bar_start + (4*time_interval)
				next_bar_count = next_bar + (time_interval/2)
				note = NOTES[midi_events[0][0][1]%12]
				chords = rules['C'][note]
				prevChord = chords[0]
				chords = list(map(lambda c : [float(note2num[c]),float(midi_events[0][0][2])],chords[0])) #ideally probabilistic
				for k in range(4):	#number of notes in chord
					queue[k],queue[k+4] = chords[k]
	
	going = True
	endCount = 0
	while going:
		if i.poll():
			midi_events = i.read(1)
			if midi_events[0][0][0] == 144:
				endCount = 0
			if(midi_events[0][0][0] == 248):
				#print(".")
				endCount+=1
				if(endCount>400):
					queue[0] = -1
				barUpdated = False
			else:
				print(midi_events)
			if midi_events[0][1] < next_bar:
				#print("less than "+str(next_bar))
				pass
			
			elif midi_events[0][1] > next_bar and midi_events[0][1] < next_bar_count and midi_events[0][0][0] == 144:
				endCount = 0
				print("ELIF ")
				note = NOTES[midi_events[0][0][1]%12]		       #noteNum % 12
				vel = midi_events[0][0][2]
				try:
					chords = rules['C'][note]
					if len(chords)>1:
					    chords.pop(random.randint(0,100)%2)
					random.shuffle(chords[0])
					print(chords[0])
					prevChord = chords[0]
				except KeyError:
					chords = []
					#sa
				chords = list(map(lambda c : [float(note2num[c]),float(midi_events[0][0][2])],chords[0]))
				for k in range(4):	#number of notes in chord
					queue[k],queue[k+4] = chords[k]
				print ("Note: "+note+" Vel:"+str(vel)+" chords found:"+str(chords))
				if(not(barUpdated)):
					next_bar = next_bar + (time_interval*4)
					next_bar_count = next_bar + (time_interval/2)
					barUpdated = True
			else:
				print("DID NOT FIND")
				print(prevChord)
				if midi_events[0][0][0] == 144:
					endCount = 0
				
				chords = list(map(lambda c : [float(note2num[c]),float(midi_events[0][0][2])],prevChord))
				for k in range(4):	#number of notes in chord
					queue[k],queue[k+4] = chords[k]
				next_bar = next_bar + (time_interval*4)
				next_bar_count = next_bar + (time_interval/2)


			print(endCount)
	pygame.midi.quit()

#------------------OUTPUT--------------------
# output = pygame.midi.Output(2)
# for chordNote in chords[0]:
#     output.note_on(note2num[chordNote], velocity=100)
#     time.sleep(0.17)
#     output.note_off(note2num[chordNote], velocity=0)
if __name__ == "__main__":
	import SharedArray as sa
	if sa.list():
		sa.delete("shm://notes")	
	queue = sa.create("shm://notes",8)
	initTempo()
	populateRules()
	getMidiInput()

