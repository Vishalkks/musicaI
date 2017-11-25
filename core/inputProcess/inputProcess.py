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
	tempo = int(raw_input("Enter desired tempo: "))
	time_interval = float(1000*4*60/tempo)


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
	prev_bar_start = None

	pygame.midi.init()
    input_id = 3
    i = pygame.midi.Input( input_id )
    print pygame.midi.get_device_info(3)
	first = False

	while !first:
        if i.poll():
			midi_events = i.read(1)
			print(midi_events)
			if midi_events[0][0][2] != 0: 			#velocity!=0 [keyPressed]
				first = True
				prev_bar_start = midi_events[1]
				note = NOTES[midi_events[0][0][1]%12]		#noteNum % 12
			    vel = midi_events[0][0][2]
				try:
			        chords = rules['C'][note]
			        if len(chords)>1:
			            chords.pop(random.randint(0,100)%2)
			        random.shuffle(chords[0])
			    except KeyError:
			        chords = None
		        print ("Note: "+note+" Vel:"+str(vel)+" chords found:"+str(chords))

	going = True
    while going:
        if i.poll():
			midi_events = i.read(1)
			print(midi_events)

			interStart = start_time + bar_count*(time_interval/2)
			interEnd = start_time + bar_count*(time_interval*3/2)

			if midi_events[0][0][2] != 0 and (midi_events[1]>interStart or midi_events[1]>interEnd): 			   #velocity!=0 [keyPressed]
				note = NOTES[midi_events[0][0][1]%12]		       #noteNum % 12
			    vel = midi_events[0][0][2]
			    try:
			        chords = rules['C'][note]
			        if len(chords)>1:
			            chords.pop(random.randint(0,100)%2)
			        random.shuffle(chords[0])
			    except KeyError:
			        chords = None
		        print ("Note: "+note+" Vel:"+str(vel)+" chords found:"+str(chords))
	pygame.midi.quit()

#------------------OUTPUT--------------------
# output = pygame.midi.Output(2)
# for chordNote in chords[0]:
#     output.note_on(note2num[chordNote], velocity=100)
#     time.sleep(0.17)
#     output.note_off(note2num[chordNote], velocity=0)

initTempo()
populateRules()
getInput()
