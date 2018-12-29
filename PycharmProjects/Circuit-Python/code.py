from math import ceil
from time import sleep

from adafruit_circuitplayground.express import cpx

song = '99 Bottles of Beer on the Wall'
songs = {
    'Twinkle Twinkle Little Star': ['ccggaag ffeeddc ggffeed ggffeed ccggaag ffeeddc ', [1, 1, 1, 1, 1, 1, 2, .1]],
    'ABCs': ['ccggaagffeeddddcggfeedgggfeedccggaagffeeddc', [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, .5, .5, .5, .5, 2, 1, 1, 2, 1, 1, 2, .5, .5, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2]],
    '99 Bottles of Beer on the Wall': ['fffdddffffeeecccegggggggccccdeffff', [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 4, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]],
    'London Bridge is Falling Down': ['abagfgaefgfgaabagfgaeagb', [.75, .25, .5, .5, .5, .5, 1, .5, .5, 1, .5, .5, 1, .75, .25, .5, .5, .5, .5, 1, 1, 1, .5, 1.5]]
}
song_data = songs[song]
lengths = list(map(len, song_data))

if lengths[0] < lengths[1]:
    song_data[0] = song_data[0] * ceil(lengths[1] / lengths[0])
elif lengths[0] > lengths[1]:
    song_data[1] = song_data[1] * ceil(lengths[0] / lengths[1])

notes = list(zip(*songs[song]))
note_tones = {
    'c': 261,
    'd': 294,
    'e': 329,
    'f': 349,
    'g': 392,
    'a': 440,
    'b': 493,
}

for note, time in notes:
    speed = 1 / (2 if cpx.button_a else 1) / (5 if cpx.button_b else 1) / (10 if cpx.switch else 1)
    
    if note == ' ':
        sleep(time * speed)
    else:
        cpx.play_tone(note_tones[note], time * speed)
