import numpy as np
from pygame import sndarray as snd
from pygame import mixer
import time

S_RATE = 44100
mixer.init(frequency=S_RATE, channels=1)

LENGTH = 5
A = 220
B = 246
C = 261
D = 293
E = 329
F = 349
FS = 369
G = 392

leng = 0.3

def note_f(freq, length=leng):
    note_wave = ((np.sin(
                    (2*np.pi*np.arange(0, length*S_RATE, 1))/(freq)
            )) * 128).astype(np.int8)
    harm_wave = note_wave + note_wave/2 + note_wave/3 + note_wave/6 + note_wave/12 + note_wave/36
    return note_wave
    #return harm_wave


a = note_f(A)
b = note_f(B)
c = note_f(C)
cl = note_f(C, leng*2)
d = note_f(D)
e = note_f(E)
f = note_f(F)
fs = note_f(FS)
g = note_f(G)
gl = note_f(G, leng*2)


snd.make_sound(c).play()
time.sleep(leng)
snd.make_sound(c).play()
time.sleep(leng)
snd.make_sound(g).play()
time.sleep(leng)
snd.make_sound(g).play()
time.sleep(leng)
snd.make_sound(a).play()
time.sleep(leng)
snd.make_sound(a).play()
time.sleep(leng)
snd.make_sound(gl).play()
time.sleep(leng*2)
snd.make_sound(f).play()
time.sleep(leng)
snd.make_sound(f).play()
time.sleep(leng)
snd.make_sound(e).play()
time.sleep(leng)
snd.make_sound(e).play()
time.sleep(leng)
snd.make_sound(d).play()
time.sleep(leng)
snd.make_sound(d).play()
time.sleep(leng)
snd.make_sound(cl).play()
time.sleep(leng*2)
















