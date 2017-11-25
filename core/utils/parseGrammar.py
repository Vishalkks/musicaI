from os import listdir
from pprint import pprint
import pygame
import pygame.midi
from pygame.locals import *

rules = {}

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

def getInput():
    input_id = 3
    i = pygame.midi.Input( input_id )
    print pygame.midi.get_device_info(3)

    NOTES = ['C','C#','D','D#','E', 'F', 'F#', 'G', 'G#', 'A', 'A#','B']
    going = True
    while going:
            events = event_get()
            for e in events:
                    if e.type in [QUIT]:
                            going = False
                    if e.type in [KEYDOWN]:
                            going = False

            if i.poll():
                    midi_events = i.read(1)
                    if midi_events[0][1] not 0:
                        note = NOTES.index(midi_events[0][1]%12)
                        vel = midi_events[0][2]
                        chords = rules['C'][note]
                        print ("Note: "+note+" Vel:"+vel+" chords found:"+str(chords))
    del is

populateRules()

pygame.midi.init()
getInput()
pygame.midi.quit()
