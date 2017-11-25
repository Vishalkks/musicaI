import pygame
import pygame.midi
from pygame.locals import *
import time

#no idea what these do

pygame.init()
pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post



pygame.midi.init()


#hard coded
'''
input_id = 3
i = pygame.midi.Input( input_id )
port =  pygame.midi.get_device_info(4)
'''

'''
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
                print(midi_events)


del i
pygame.midi.quit()
pygame.quit()
f.close()
exit()
'''

output = pygame.midi.Output(2)
'''output.write([[[248, 0, 0, 0], 3699],[[248, 0, 0, 0], 3726], [[248, 0, 0, 0], 3753],
[[248, 0, 0, 0], 3780],
[[248, 0, 0, 0], 3807],
[[248, 0, 0, 0], 3834],
[[248, 0, 0, 0], 3861],
[[248, 0, 0, 0], 3887],
[[248, 0, 0, 0], 3916],
[[248, 0, 0, 0], 3943],
[[248, 0, 0, 0], 3970],
[[248, 0, 0, 0], 3997],
[[248, 0, 0, 0], 4024],
[[248, 0, 0, 0], 4051],
[[248, 0, 0, 0], 4079],
[[248, 0, 0, 0], 4106],
[[248, 0, 0, 0], 4133],
[[248, 0, 0, 0], 4161],
[[144, 96, 81, 0], 4187],
[[248, 0, 0, 0], 4187],
[[248, 0, 0, 0], 4215],
[[248, 0, 0, 0], 4242],
[[248, 0, 0, 0], 4269],
[[144, 96, 0, 0], 4296],
[[248, 0, 0, 0], 4297],
[[248, 0, 0, 0], 4323],
[[248, 0, 0, 0], 4351],
[[248, 0, 0, 0], 4379],
[[248, 0, 0, 0], 4405],
[[248, 0, 0, 0], 4432],
[[144, 38, 81, 0], 4187]])'''

for i in range(36,96):
        output.note_on(i,velocity=100)
        time.sleep(0.1)
        output.note_off(i,velocity=0)