import pygame
import pygame.midi
from pygame.locals import *


#no idea what these do

pygame.init()
pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post



pygame.midi.init()


#hard coded
input_id = 3

i = pygame.midi.Input( input_id )
print pygame.midi.get_device_info(3)


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
                print midi_events


del i
pygame.midi.quit()
pygame.quit()
exit()
