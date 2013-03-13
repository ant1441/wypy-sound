import numpy as np
from pygame import sndarray as snd
from pygame import mixer
import time
import math

S_RATE = 44100

################################################################################
# Note Frequencies
# 
# Equation of nth key on keyboard
# f(n) = (2^(1/12))^(n-49) * 440 Hz
# High A is 440 Hz. Middle C is f(40)
################################################################################

def note(number):
    if number is None:
        return
    twelfth_root_two = 1.0594630943592952645618252949463417007792043174941856
    power = number - 49
    exponent = math.pow(twelfth_root_two, power)
    frequency = exponent * 440
    
    return frequency

################################################################################
# Defining notes
################################################################################
# Frequencies

A = map(note, [0, 13, 25, 37, 49, 61, 73, 85])
B = map(note, [3, 15, 27, 39, 51, 63, 75, 87])
C = map(note, [None, 4, 16, 28, 40, 52, 64, 76, 88]) # Middle C is C[4]
D = map(note, [None, 6, 18, 30, 42, 54, 66, 78])
E = map(note, [None, 8, 20, 32, 44, 56, 68, 80])
F = map(note, [None, 9, 21, 33, 45, 57, 69, 81])
G = map(note, [None, 11, 23, 35, 47, 59, 71, 83])

# Note Lengths
SEMI = 1.0
MINIM = SEMI/2
CROTCHET = SEMI/4
QUAVER = SEMI/8
SEMIQUAVER = SEMI/16
DEMISEMIQUAVER = SEMI/32
HEMIDEMISEMIQUAVER = SEMI/64

BEAT_LENGTH = 1
def calc_wave(freq, duration=BEAT_LENGTH):
#    print 'duration: ' + str(duration)
    note_wave = ((np.sin(
                    (2*np.pi*np.arange(0, duration*S_RATE, 1))/(freq)
            )) * 128).astype(np.int8)
    
    harm_wave = note_wave + note_wave/2 + note_wave/3 + note_wave/6 + note_wave/12 + note_wave/36
    return note_wave
    #return harm_wave

LENGTH = 5

# Start building the music
mixer.init(frequency=S_RATE, channels=1)

music = [(C[4], CROTCHET), (C[4], CROTCHET), (G[4], CROTCHET), (G[4], CROTCHET),
        (A[4], CROTCHET), (A[4], CROTCHET), (G[4], MINIM), (F[4], CROTCHET), (F[4], CROTCHET),
        (E[4], CROTCHET), (E[4], CROTCHET), (D[4], CROTCHET), (D[4], CROTCHET), (C[4],MINIM)]

def build_beat(beat):
    beat_wave = 0
    if type(beat) is tuple:
        beat = [beat]
    for note in beat:
        name, duration = note
        if type(name) is list:
            print '[ERROR] Ensure music is given octave level. Defaulting to C = C4'
            name = name[4]
#        print 'Duration: ' + str(duration)
        beat_wave = beat_wave + calc_wave(name, duration)
    return beat_wave
        
        
def play(music):
    for beat in music:
        beat_wave = build_beat(beat)
        snd.make_sound(beat_wave).play()
        time.sleep(BEAT_LENGTH*0.9)
