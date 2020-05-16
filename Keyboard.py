from tkinter import *
import pyaudio
import numpy as np
import pygame
from pydub import AudioSegment
from scipy.io.wavfile import write

master = Tk()

# Setup
master.title('Piano')
master.resizable(width=False, height=False)

# Photos
whiteKeyU = PhotoImage(file="whiteKeyU.png")
whiteKeyU = whiteKeyU.zoom(5)
whiteKeyU = whiteKeyU.subsample(25)

whiteKeyP = PhotoImage(file="whiteKeyP.png")

blackKeyU = PhotoImage(file="blackKeyU.png")
blackKeyU = blackKeyU.zoom(6)
blackKeyU = blackKeyU.subsample(28)

blackKeyP = PhotoImage(file="blackKeyP.png")

# frame
frame = Frame(master)
frame.pack(fill="both", expand=True, padx=20, pady=20)

# octave 1
C0 = Button(frame, text='C', image=whiteKeyU, command=lambda: audioGeneration(130.82))
C0.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
D0 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(146.83))
D0.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
E0 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(164.81))
E0.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
F0 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(174.61))
F0.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
G0 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(196))
G0.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
A0 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(220))
A0.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
B0 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(246.94))
B0.pack(fill=NONE, expand=False, ipady=3, side=LEFT)

Dflat0 = Button(frame, text='Dflat', image=blackKeyU, command=lambda: audioGeneration(138.59))
Dflat0.place(relx=0.035, rely=0.365, anchor=CENTER)
Eflat0 = Button(frame, text='Eflat', image=blackKeyU, command=lambda: audioGeneration(155.56))
Eflat0.place(relx=0.07, rely=0.365, anchor=CENTER)
Gflat0 = Button(frame, text='Gflat', image=blackKeyU, command=lambda: audioGeneration(185))
Gflat0.place(relx=0.1425, rely=0.365, anchor=CENTER)
Aflat0 = Button(frame, text='Aflat', image=blackKeyU, command=lambda: audioGeneration(207.65))
Aflat0.place(relx=0.1785, rely=0.365, anchor=CENTER)
Bflat0 = Button(frame, text='Bflat', image=blackKeyU, command=lambda: audioGeneration(233.08))
Bflat0.place(relx=0.2125, rely=0.365, anchor=CENTER)

# octave 2
C1 = Button(frame, text='D', image=whiteKeyU, command=lambda: [audioGeneration(261.63)])
C1.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
D1 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(293.66))
D1.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
E1 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(329.63))
E1.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
F1 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(349.23))
F1.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
G1 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(392))
G1.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
A1 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(440))
A1.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
B1 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(493.88))
B1.pack(fill=NONE, expand=False, ipady=3, side=LEFT)

Dflat1 = Button(frame, text='Dflat', image=blackKeyU, command=lambda: audioGeneration(277.18))
Dflat1.place(relx=0.285, rely=0.365, anchor=CENTER)
Eflat1 = Button(frame, text='Eflat', image=blackKeyU, command=lambda: audioGeneration(311.13))
Eflat1.place(relx=0.32, rely=0.365, anchor=CENTER)
Gflat1 = Button(frame, text='Gflat', image=blackKeyU, command=lambda: audioGeneration(369.99))
Gflat1.place(relx=0.3925, rely=0.365, anchor=CENTER)
Aflat1 = Button(frame, text='Aflat', image=blackKeyU, command=lambda: audioGeneration(415.3))
Aflat1.place(relx=0.4275, rely=0.365, anchor=CENTER)
Bflat1 = Button(frame, text='Bflat', image=blackKeyU, command=lambda: audioGeneration(466.16))
Bflat1.place(relx=0.463, rely=0.365, anchor=CENTER)

# octave 3
C2 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(523.25))
C2.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
D2 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(587.33))
D2.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
E2 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(659.26))
E2.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
F2 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(698.46))
F2.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
G2 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(783.99))
G2.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
A2 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(880))
A2.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
B2 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(987.77))
B2.pack(fill=NONE, expand=False, ipady=3, side=LEFT)

Dflat2 = Button(frame, text='Dflat', image=blackKeyU, command=lambda: audioGeneration(554.37))
Dflat2.place(relx=0.5335, rely=0.365, anchor=CENTER)
Eflat2 = Button(frame, text='Eflat', image=blackKeyU, command=lambda: audioGeneration(622.25))
Eflat2.place(relx=0.57, rely=0.365, anchor=CENTER)
Gflat2 = Button(frame, text='Gflat', image=blackKeyU, command=lambda: audioGeneration(739.99))
Gflat2.place(relx=0.6425, rely=0.365, anchor=CENTER)
Aflat2 = Button(frame, text='Aflat', image=blackKeyU, command=lambda: audioGeneration(830.61))
Aflat2.place(relx=0.6775, rely=0.365, anchor=CENTER)
Bflat2 = Button(frame, text='Bflat', image=blackKeyU, command=lambda: audioGeneration(932.33))
Bflat2.place(relx=0.713, rely=0.365, anchor=CENTER)

# octave 4
C3 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(1046.5))
C3.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
D3 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(1174.66))
D3.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
E3 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(1318.51))
E3.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
F3 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(1396.91))
F3.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
G3 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(1567.98))
G3.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
A3 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(1760))
A3.pack(fill=NONE, expand=False, ipady=3, side=LEFT)
B3 = Button(frame, text='D', image=whiteKeyU, command=lambda: audioGeneration(1975.53))
B3.pack(fill=NONE, expand=False, ipady=3, side=LEFT)

Dflat3 = Button(frame, text='Dflat', image=blackKeyU, command=lambda: audioGeneration(1108.73))
Dflat3.place(relx=0.7835, rely=0.365, anchor=CENTER)
Eflat3 = Button(frame, text='Eflat', image=blackKeyU, command=lambda: audioGeneration(1244.51))
Eflat3.place(relx=0.82, rely=0.365, anchor=CENTER)
Gflat3 = Button(frame, text='Gflat', image=blackKeyU, command=lambda: audioGeneration(1479.98))
Gflat3.place(relx=0.8925, rely=0.365, anchor=CENTER)
Aflat3 = Button(frame, text='Aflat', image=blackKeyU, command=lambda: audioGeneration(1661.22))
Aflat3.place(relx=0.9275, rely=0.365, anchor=CENTER)
Bflat3 = Button(frame, text='Bflat', image=blackKeyU, command=lambda: audioGeneration(1864.66))
Bflat3.place(relx=0.963, rely=0.365, anchor=CENTER)


# generates sounds
def audioGeneration(x):
    p = pyaudio.PyAudio()

    volume = 0.2  # range [0.0, 1.0]
    fs = 44100  # sampling rate, Hz, must be integer
    duration = 1  # in seconds, may be float
    f = x  # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)
    # scales numpy array
    scaled = np.int16(samples/ np.max(np.abs(samples)) * 32767)
    # writes array into test.wav file
    write('test.wav', 44100, scaled)

    # adds the fadeout effect to reduce popping noise
    keysound = AudioSegment.from_wav('test.wav')
    keysound2 = keysound * 2
    keysound2 = keysound2.low_pass_filter(1000)
    length = len(keysound2)
    fade_time = int(length * 0.5)
    faded = keysound.fade_out(fade_time)
    faded.export('test1.wav', format='wav')

    # plays the sound by using channels
    pygame.mixer.init()
    sound = pygame.mixer.Sound('test1.wav')
    pygame.mixer.set_num_channels(20) # 20 concurrent sounds
    pygame.mixer.find_channel().play(sound)


# key binds
master.bind('<s>', lambda a: audioGeneration(261.63))
master.bind('<f>', lambda a: audioGeneration(329.63))
master.bind('<h>', lambda a: audioGeneration(392))

master.mainloop()