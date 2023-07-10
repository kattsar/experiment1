#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Ιούλιος 10, 2023, at 11:06
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from codeSavePractice
count = 0


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'REPSWITCH1_Practice_v2022.2.4'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\GitHub\\experiment1\\REPSWITCH1_Practice_v2022.2.4_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation
# Make folder to store recordings from micPractice
micPracticeRecFolder = filename + '_micPractice_recorded'
if not os.path.isdir(micPracticeRecFolder):
    os.mkdir(micPracticeRecFolder)

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "General_Instr_1" ---
textboxInstr1 = visual.TextBox2(
     win, text='En este experimento verás imágenes en la pantalla y tendrás que nombrarlas. \n\nTendrás que nombrar cada imagen diciendo su nombre en voz alta o escribiéndolo. \n\nUn rectángulo de color alrededor de cada imagen te indicará si tienes que decirla en voz alta o teclearla. ', font='Open Sans',
     pos=(0, 0.25),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstr1',
     autoLog=True,
)
textboxInstr1_2 = visual.TextBox2(
     win, text='Si el rectángulo es', font='Open Sans',
     pos=(0, 0.03),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstr1_2',
     autoLog=True,
)
textboxInstr1_3 = visual.TextBox2(
     win, text='azul,', font='Open Sans',
     pos=(0.255, 0.03),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 0.0902], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstr1_3',
     autoLog=True,
)
textboxInstr1_4 = visual.TextBox2(
     win, text=' tendrás que  ', font='Open Sans',
     pos=(0.33, 0.03),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstr1_4',
     autoLog=True,
)
textboxInstr1_5 = visual.TextBox2(
     win, text='escribirlo con el teclado.', font='Open Sans',
     pos=(0.51, 0.03),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstr1_5',
     autoLog=True,
)
textboxInstr1_6 = visual.TextBox2(
     win, text='Si el rectángulo es ', font='Open Sans',
     pos=(0,-0.03),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstr1_6',
     autoLog=True,
)
textboxInstr1_7 = visual.TextBox2(
     win, text='amarillo,', font='Open Sans',
     pos=(0.255, -0.03),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color=[1.0000, 0.6863, -1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstr1_7',
     autoLog=True,
)
textboxInstr1_8 = visual.TextBox2(
     win, text=' tendrás que ', font='Open Sans',
     pos=(0.39, -0.03),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstr1_8',
     autoLog=True,
)
textboxInstr1_9 = visual.TextBox2(
     win, text='decirlo en voz alta. ', font='Open Sans',
     pos=(0.57, -0.03),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstr1_9',
     autoLog=True,
)
textboxInstr1_10 = visual.TextBox2(
     win, text='Deberás nombrar las imágenes lo más rápido y con la mayor precisión posible. \n\nLas imágenes solo permanecerán en la pantalla durante unos instantes. \n\n\nPulsa la BARRA ESPACIADORA para continuar.\n', font='Open Sans',
     pos=(0, -0.27),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstr1_10',
     autoLog=True,
)
keyInstr1 = keyboard.Keyboard()

# --- Initialize components for Routine "General_Instr_2" ---
textboxInstr2 = visual.TextBox2(
     win, text='Algunas instrucciones más.\n\nCuando hables, asegúrate de decir una sola palabra, con voz clara.\n\nIntenta mantener las manos sobre el teclado durante toda la sesión.\n\nY, por favor, ¡no hables mientras escribes!\n\n\nPulsa la BARRA ESPACIADORA para continuar.\n', font='Open Sans',
     pos=(0, 0),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstr2',
     autoLog=True,
)
keyInstr2 = keyboard.Keyboard()

# --- Initialize components for Routine "General_Instr_3" ---
textboxInstr3 = visual.TextBox2(
     win, text='Practiquemos antes de empezar.\n\nPulsa la BARRA ESPACIADORA para continuar.\n', font='Open Sans',
     pos=(0, 0),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstr3',
     autoLog=True,
)
keyInstr3 = keyboard.Keyboard()

# --- Initialize components for Routine "InstructionsPractice" ---
textboxInstrPractice = visual.TextBox2(
     win, text='Si el rectángulo es', font='Open Sans',
     pos=(0, 0.2),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice',
     autoLog=True,
)
textboxInstrPractice_2 = visual.TextBox2(
     win, text='azul,', font='Open Sans',
     pos=(0.255, 0.2),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 0.0902], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice_2',
     autoLog=True,
)
textboxInstrPractice_3 = visual.TextBox2(
     win, text=' deberás ', font='Open Sans',
     pos=(0.33, 0.2),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice_3',
     autoLog=True,
)
textboxInstrPractice_4 = visual.TextBox2(
     win, text='teclear', font='Open Sans',
     pos=(0.46, 0.2),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice_4',
     autoLog=True,
)
textboxInstrPractice_5 = visual.TextBox2(
     win, text='el nombre de la imagen. ', font='Open Sans',
     pos=(0.575, 0.2),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice_5',
     autoLog=True,
)
textboxInstrPractice_6 = visual.TextBox2(
     win, text='La palabra', font='Open Sans',
     pos=(0, 0.15),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice_6',
     autoLog=True,
)
textboxInstrPractice_7 = visual.TextBox2(
     win, text='TECLEA', font='Open Sans',
     pos=(0.155, 0.15),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice_7',
     autoLog=True,
)
textboxInstrPractice_8 = visual.TextBox2(
     win, text='aparecerá encima de la imagen.', font='Open Sans',
     pos=(0.27, 0.15),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice_8',
     autoLog=True,
)
textboxInstrPractice_9 = visual.TextBox2(
     win, text='Si el rectángulo es ', font='Open Sans',
     pos=(0, 0.05),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice_9',
     autoLog=True,
)
textboxInstrPractice_10 = visual.TextBox2(
     win, text='amarillo,', font='Open Sans',
     pos=(0.255, 0.05),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color=[1.0000, 0.6863, -1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice_10',
     autoLog=True,
)
textboxInstrPractice_11 = visual.TextBox2(
     win, text=' tendrás que ', font='Open Sans',
     pos=(0.39, 0.05),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice_11',
     autoLog=True,
)
textboxInstrPractice_12 = visual.TextBox2(
     win, text='decir en voz alta ', font='Open Sans',
     pos=(0.57, 0.05),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice_12',
     autoLog=True,
)
textboxInstrPractice_13 = visual.TextBox2(
     win, text='el nombre de la imagen. ', font='Open Sans',
     pos=(0.82, 0.05),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice_13',
     autoLog=True,
)
textboxInstrPractice_14 = visual.TextBox2(
     win, text='La palabra', font='Open Sans',
     pos=(0, 0),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice_14',
     autoLog=True,
)
textboxInstrPractice_15 = visual.TextBox2(
     win, text='HABLA', font='Open Sans',
     pos=(0.15, 0),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice_15',
     autoLog=True,
)
textboxInstrPractice_16 = visual.TextBox2(
     win, text='aparecerá encima de la imagen. ', font='Open Sans',
     pos=(0.26, 0),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice_16',
     autoLog=True,
)
textboxInstrPractice_17 = visual.TextBox2(
     win, text='Pulsa la BARRA ESPACIADORA para empezar.', font='Open Sans',
     pos=(0, -0.1),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrPractice_17',
     autoLog=True,
)
keyInstrPractice = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
textBlank500 = visual.TextStim(win=win, name='textBlank500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "ITI" ---
fixationITI = visual.ShapeStim(
    win=win, name='fixationITI', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "practiceTrial" ---
polygonCol = visual.Rect(
    win=win, name='polygonCol',
    width=(0.55, 0.55)[0], height=(0.55, 0.55)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
polygonWh = visual.Rect(
    win=win, name='polygonWh',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
textCue = visual.TextStim(win=win, name='textCue',
    text='',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
imagePractice = visual.ImageStim(
    win=win,
    name='imagePractice', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
polygonText = visual.Rect(
    win=win, name='polygonText',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.9216, 0.9216, 0.9216], fillColor=[0.9216, 0.9216, 0.9216],
    opacity=None, depth=-4.0, interpolate=True)
textPractice = visual.TextStim(win=win, name='textPractice',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
keyPractice = keyboard.Keyboard()
micPractice = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=48000, maxRecordingSize=24000.0
)

# --- Initialize components for Routine "blank500" ---
textBlank500 = visual.TextStim(win=win, name='textBlank500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "blank500" ---
textBlank500 = visual.TextStim(win=win, name='textBlank500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "EndPractice" ---
textboxEndPracrice = visual.TextBox2(
     win, text='¡Genial! \n\n\nPulsa la BARRA ESPACIADORA para continuar.', font='Open Sans',
     pos=(0, 0),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxEndPracrice',
     autoLog=True,
)
keyEndPractice = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "General_Instr_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textboxInstr1.reset()
textboxInstr1_2.reset()
textboxInstr1_3.reset()
textboxInstr1_4.reset()
textboxInstr1_5.reset()
textboxInstr1_6.reset()
textboxInstr1_7.reset()
textboxInstr1_8.reset()
textboxInstr1_9.reset()
textboxInstr1_10.reset()
keyInstr1.keys = []
keyInstr1.rt = []
_keyInstr1_allKeys = []
# keep track of which components have finished
General_Instr_1Components = [textboxInstr1, textboxInstr1_2, textboxInstr1_3, textboxInstr1_4, textboxInstr1_5, textboxInstr1_6, textboxInstr1_7, textboxInstr1_8, textboxInstr1_9, textboxInstr1_10, keyInstr1]
for thisComponent in General_Instr_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "General_Instr_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textboxInstr1* updates
    if textboxInstr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstr1.frameNStart = frameN  # exact frame index
        textboxInstr1.tStart = t  # local t and not account for scr refresh
        textboxInstr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstr1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstr1.started')
        textboxInstr1.setAutoDraw(True)
    
    # *textboxInstr1_2* updates
    if textboxInstr1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstr1_2.frameNStart = frameN  # exact frame index
        textboxInstr1_2.tStart = t  # local t and not account for scr refresh
        textboxInstr1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstr1_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstr1_2.started')
        textboxInstr1_2.setAutoDraw(True)
    
    # *textboxInstr1_3* updates
    if textboxInstr1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstr1_3.frameNStart = frameN  # exact frame index
        textboxInstr1_3.tStart = t  # local t and not account for scr refresh
        textboxInstr1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstr1_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstr1_3.started')
        textboxInstr1_3.setAutoDraw(True)
    
    # *textboxInstr1_4* updates
    if textboxInstr1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstr1_4.frameNStart = frameN  # exact frame index
        textboxInstr1_4.tStart = t  # local t and not account for scr refresh
        textboxInstr1_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstr1_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstr1_4.started')
        textboxInstr1_4.setAutoDraw(True)
    
    # *textboxInstr1_5* updates
    if textboxInstr1_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstr1_5.frameNStart = frameN  # exact frame index
        textboxInstr1_5.tStart = t  # local t and not account for scr refresh
        textboxInstr1_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstr1_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstr1_5.started')
        textboxInstr1_5.setAutoDraw(True)
    
    # *textboxInstr1_6* updates
    if textboxInstr1_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstr1_6.frameNStart = frameN  # exact frame index
        textboxInstr1_6.tStart = t  # local t and not account for scr refresh
        textboxInstr1_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstr1_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstr1_6.started')
        textboxInstr1_6.setAutoDraw(True)
    
    # *textboxInstr1_7* updates
    if textboxInstr1_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstr1_7.frameNStart = frameN  # exact frame index
        textboxInstr1_7.tStart = t  # local t and not account for scr refresh
        textboxInstr1_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstr1_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstr1_7.started')
        textboxInstr1_7.setAutoDraw(True)
    
    # *textboxInstr1_8* updates
    if textboxInstr1_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstr1_8.frameNStart = frameN  # exact frame index
        textboxInstr1_8.tStart = t  # local t and not account for scr refresh
        textboxInstr1_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstr1_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstr1_8.started')
        textboxInstr1_8.setAutoDraw(True)
    
    # *textboxInstr1_9* updates
    if textboxInstr1_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstr1_9.frameNStart = frameN  # exact frame index
        textboxInstr1_9.tStart = t  # local t and not account for scr refresh
        textboxInstr1_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstr1_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstr1_9.started')
        textboxInstr1_9.setAutoDraw(True)
    
    # *textboxInstr1_10* updates
    if textboxInstr1_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstr1_10.frameNStart = frameN  # exact frame index
        textboxInstr1_10.tStart = t  # local t and not account for scr refresh
        textboxInstr1_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstr1_10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstr1_10.started')
        textboxInstr1_10.setAutoDraw(True)
    
    # *keyInstr1* updates
    waitOnFlip = False
    if keyInstr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyInstr1.frameNStart = frameN  # exact frame index
        keyInstr1.tStart = t  # local t and not account for scr refresh
        keyInstr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyInstr1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'keyInstr1.started')
        keyInstr1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyInstr1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyInstr1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyInstr1.status == STARTED and not waitOnFlip:
        theseKeys = keyInstr1.getKeys(keyList=['space'], waitRelease=False)
        _keyInstr1_allKeys.extend(theseKeys)
        if len(_keyInstr1_allKeys):
            keyInstr1.keys = _keyInstr1_allKeys[-1].name  # just the last key pressed
            keyInstr1.rt = _keyInstr1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in General_Instr_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "General_Instr_1" ---
for thisComponent in General_Instr_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyInstr1.keys in ['', [], None]:  # No response was made
    keyInstr1.keys = None
thisExp.addData('keyInstr1.keys',keyInstr1.keys)
if keyInstr1.keys != None:  # we had a response
    thisExp.addData('keyInstr1.rt', keyInstr1.rt)
thisExp.nextEntry()
# the Routine "General_Instr_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "General_Instr_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textboxInstr2.reset()
keyInstr2.keys = []
keyInstr2.rt = []
_keyInstr2_allKeys = []
# keep track of which components have finished
General_Instr_2Components = [textboxInstr2, keyInstr2]
for thisComponent in General_Instr_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "General_Instr_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textboxInstr2* updates
    if textboxInstr2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstr2.frameNStart = frameN  # exact frame index
        textboxInstr2.tStart = t  # local t and not account for scr refresh
        textboxInstr2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstr2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstr2.started')
        textboxInstr2.setAutoDraw(True)
    
    # *keyInstr2* updates
    waitOnFlip = False
    if keyInstr2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyInstr2.frameNStart = frameN  # exact frame index
        keyInstr2.tStart = t  # local t and not account for scr refresh
        keyInstr2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyInstr2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'keyInstr2.started')
        keyInstr2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyInstr2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyInstr2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyInstr2.status == STARTED and not waitOnFlip:
        theseKeys = keyInstr2.getKeys(keyList=['space'], waitRelease=False)
        _keyInstr2_allKeys.extend(theseKeys)
        if len(_keyInstr2_allKeys):
            keyInstr2.keys = _keyInstr2_allKeys[-1].name  # just the last key pressed
            keyInstr2.rt = _keyInstr2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in General_Instr_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "General_Instr_2" ---
for thisComponent in General_Instr_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyInstr2.keys in ['', [], None]:  # No response was made
    keyInstr2.keys = None
thisExp.addData('keyInstr2.keys',keyInstr2.keys)
if keyInstr2.keys != None:  # we had a response
    thisExp.addData('keyInstr2.rt', keyInstr2.rt)
thisExp.nextEntry()
# the Routine "General_Instr_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "General_Instr_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textboxInstr3.reset()
keyInstr3.keys = []
keyInstr3.rt = []
_keyInstr3_allKeys = []
# keep track of which components have finished
General_Instr_3Components = [textboxInstr3, keyInstr3]
for thisComponent in General_Instr_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "General_Instr_3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textboxInstr3* updates
    if textboxInstr3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstr3.frameNStart = frameN  # exact frame index
        textboxInstr3.tStart = t  # local t and not account for scr refresh
        textboxInstr3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstr3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstr3.started')
        textboxInstr3.setAutoDraw(True)
    
    # *keyInstr3* updates
    waitOnFlip = False
    if keyInstr3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyInstr3.frameNStart = frameN  # exact frame index
        keyInstr3.tStart = t  # local t and not account for scr refresh
        keyInstr3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyInstr3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'keyInstr3.started')
        keyInstr3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyInstr3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyInstr3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyInstr3.status == STARTED and not waitOnFlip:
        theseKeys = keyInstr3.getKeys(keyList=['space'], waitRelease=False)
        _keyInstr3_allKeys.extend(theseKeys)
        if len(_keyInstr3_allKeys):
            keyInstr3.keys = _keyInstr3_allKeys[-1].name  # just the last key pressed
            keyInstr3.rt = _keyInstr3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in General_Instr_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "General_Instr_3" ---
for thisComponent in General_Instr_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyInstr3.keys in ['', [], None]:  # No response was made
    keyInstr3.keys = None
thisExp.addData('keyInstr3.keys',keyInstr3.keys)
if keyInstr3.keys != None:  # we had a response
    thisExp.addData('keyInstr3.rt', keyInstr3.rt)
thisExp.nextEntry()
# the Routine "General_Instr_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "InstructionsPractice" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textboxInstrPractice.reset()
textboxInstrPractice_2.reset()
textboxInstrPractice_3.reset()
textboxInstrPractice_4.reset()
textboxInstrPractice_5.reset()
textboxInstrPractice_6.reset()
textboxInstrPractice_7.reset()
textboxInstrPractice_8.reset()
textboxInstrPractice_9.reset()
textboxInstrPractice_10.reset()
textboxInstrPractice_11.reset()
textboxInstrPractice_12.reset()
textboxInstrPractice_13.reset()
textboxInstrPractice_14.reset()
textboxInstrPractice_15.reset()
textboxInstrPractice_16.reset()
textboxInstrPractice_17.reset()
keyInstrPractice.keys = []
keyInstrPractice.rt = []
_keyInstrPractice_allKeys = []
# keep track of which components have finished
InstructionsPracticeComponents = [textboxInstrPractice, textboxInstrPractice_2, textboxInstrPractice_3, textboxInstrPractice_4, textboxInstrPractice_5, textboxInstrPractice_6, textboxInstrPractice_7, textboxInstrPractice_8, textboxInstrPractice_9, textboxInstrPractice_10, textboxInstrPractice_11, textboxInstrPractice_12, textboxInstrPractice_13, textboxInstrPractice_14, textboxInstrPractice_15, textboxInstrPractice_16, textboxInstrPractice_17, keyInstrPractice]
for thisComponent in InstructionsPracticeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "InstructionsPractice" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textboxInstrPractice* updates
    if textboxInstrPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice.frameNStart = frameN  # exact frame index
        textboxInstrPractice.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice.started')
        textboxInstrPractice.setAutoDraw(True)
    
    # *textboxInstrPractice_2* updates
    if textboxInstrPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_2.frameNStart = frameN  # exact frame index
        textboxInstrPractice_2.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_2.started')
        textboxInstrPractice_2.setAutoDraw(True)
    
    # *textboxInstrPractice_3* updates
    if textboxInstrPractice_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_3.frameNStart = frameN  # exact frame index
        textboxInstrPractice_3.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_3.started')
        textboxInstrPractice_3.setAutoDraw(True)
    
    # *textboxInstrPractice_4* updates
    if textboxInstrPractice_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_4.frameNStart = frameN  # exact frame index
        textboxInstrPractice_4.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_4.started')
        textboxInstrPractice_4.setAutoDraw(True)
    
    # *textboxInstrPractice_5* updates
    if textboxInstrPractice_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_5.frameNStart = frameN  # exact frame index
        textboxInstrPractice_5.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_5.started')
        textboxInstrPractice_5.setAutoDraw(True)
    
    # *textboxInstrPractice_6* updates
    if textboxInstrPractice_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_6.frameNStart = frameN  # exact frame index
        textboxInstrPractice_6.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_6.started')
        textboxInstrPractice_6.setAutoDraw(True)
    
    # *textboxInstrPractice_7* updates
    if textboxInstrPractice_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_7.frameNStart = frameN  # exact frame index
        textboxInstrPractice_7.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_7.started')
        textboxInstrPractice_7.setAutoDraw(True)
    
    # *textboxInstrPractice_8* updates
    if textboxInstrPractice_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_8.frameNStart = frameN  # exact frame index
        textboxInstrPractice_8.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_8.started')
        textboxInstrPractice_8.setAutoDraw(True)
    
    # *textboxInstrPractice_9* updates
    if textboxInstrPractice_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_9.frameNStart = frameN  # exact frame index
        textboxInstrPractice_9.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_9.started')
        textboxInstrPractice_9.setAutoDraw(True)
    
    # *textboxInstrPractice_10* updates
    if textboxInstrPractice_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_10.frameNStart = frameN  # exact frame index
        textboxInstrPractice_10.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_10.started')
        textboxInstrPractice_10.setAutoDraw(True)
    
    # *textboxInstrPractice_11* updates
    if textboxInstrPractice_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_11.frameNStart = frameN  # exact frame index
        textboxInstrPractice_11.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_11, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_11.started')
        textboxInstrPractice_11.setAutoDraw(True)
    
    # *textboxInstrPractice_12* updates
    if textboxInstrPractice_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_12.frameNStart = frameN  # exact frame index
        textboxInstrPractice_12.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_12, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_12.started')
        textboxInstrPractice_12.setAutoDraw(True)
    
    # *textboxInstrPractice_13* updates
    if textboxInstrPractice_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_13.frameNStart = frameN  # exact frame index
        textboxInstrPractice_13.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_13, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_13.started')
        textboxInstrPractice_13.setAutoDraw(True)
    
    # *textboxInstrPractice_14* updates
    if textboxInstrPractice_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_14.frameNStart = frameN  # exact frame index
        textboxInstrPractice_14.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_14, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_14.started')
        textboxInstrPractice_14.setAutoDraw(True)
    
    # *textboxInstrPractice_15* updates
    if textboxInstrPractice_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_15.frameNStart = frameN  # exact frame index
        textboxInstrPractice_15.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_15, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_15.started')
        textboxInstrPractice_15.setAutoDraw(True)
    
    # *textboxInstrPractice_16* updates
    if textboxInstrPractice_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_16.frameNStart = frameN  # exact frame index
        textboxInstrPractice_16.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_16, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_16.started')
        textboxInstrPractice_16.setAutoDraw(True)
    
    # *textboxInstrPractice_17* updates
    if textboxInstrPractice_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_17.frameNStart = frameN  # exact frame index
        textboxInstrPractice_17.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_17, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_17.started')
        textboxInstrPractice_17.setAutoDraw(True)
    
    # *keyInstrPractice* updates
    waitOnFlip = False
    if keyInstrPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyInstrPractice.frameNStart = frameN  # exact frame index
        keyInstrPractice.tStart = t  # local t and not account for scr refresh
        keyInstrPractice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyInstrPractice, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'keyInstrPractice.started')
        keyInstrPractice.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyInstrPractice.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyInstrPractice.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyInstrPractice.status == STARTED and not waitOnFlip:
        theseKeys = keyInstrPractice.getKeys(keyList=['space'], waitRelease=False)
        _keyInstrPractice_allKeys.extend(theseKeys)
        if len(_keyInstrPractice_allKeys):
            keyInstrPractice.keys = _keyInstrPractice_allKeys[-1].name  # just the last key pressed
            keyInstrPractice.rt = _keyInstrPractice_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsPracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "InstructionsPractice" ---
for thisComponent in InstructionsPracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyInstrPractice.keys in ['', [], None]:  # No response was made
    keyInstrPractice.keys = None
thisExp.addData('keyInstrPractice.keys',keyInstrPractice.keys)
if keyInstrPractice.keys != None:  # we had a response
    thisExp.addData('keyInstrPractice.rt', keyInstrPractice.rt)
thisExp.nextEntry()
# the Routine "InstructionsPractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "blank500" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blank500Components = [textBlank500]
for thisComponent in blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank500" ---
while continueRoutine and routineTimer.getTime() < 0.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank500* updates
    if textBlank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank500.frameNStart = frameN  # exact frame index
        textBlank500.tStart = t  # local t and not account for scr refresh
        textBlank500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank500, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textBlank500.started')
        textBlank500.setAutoDraw(True)
    if textBlank500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank500.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank500.tStop = t  # not accounting for scr refresh
            textBlank500.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textBlank500.stopped')
            textBlank500.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank500" ---
for thisComponent in blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.500000)

# set up handler to look after randomisation of conditions etc
trialsPractice = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('repswitch_practice.xlsx'),
    seed=None, name='trialsPractice')
thisExp.addLoop(trialsPractice)  # add the loop to the experiment
thisTrialsPractice = trialsPractice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsPractice.rgb)
if thisTrialsPractice != None:
    for paramName in thisTrialsPractice:
        exec('{} = thisTrialsPractice[paramName]'.format(paramName))

for thisTrialsPractice in trialsPractice:
    currentLoop = trialsPractice
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsPractice.rgb)
    if thisTrialsPractice != None:
        for paramName in thisTrialsPractice:
            exec('{} = thisTrialsPractice[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [fixationITI]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixationITI* updates
        if fixationITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixationITI.frameNStart = frameN  # exact frame index
            fixationITI.tStart = t  # local t and not account for scr refresh
            fixationITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixationITI, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixationITI.started')
            fixationITI.setAutoDraw(True)
        if fixationITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixationITI.tStartRefresh + random()+1-frameTolerance:
                # keep track of stop time/frame for later
                fixationITI.tStop = t  # not accounting for scr refresh
                fixationITI.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixationITI.stopped')
                fixationITI.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practiceTrial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    polygonCol.setFillColor(frameColor)
    polygonCol.setLineColor(frameColor)
    textCue.setColor(frameColor, colorSpace='rgb')
    imagePractice.setImage(image)
    keyPractice.keys = []
    keyPractice.rt = []
    _keyPractice_allKeys = []
    # Run 'Begin Routine' code from codePractice
    respDisplay = ""
    
    
    #key logger defaults
    last_len = 0
    key_list = []
    
    polygonText.opacity = 0  
    # Run 'Begin Routine' code from codeSavePractice
    count = count + 1
    # keep track of which components have finished
    practiceTrialComponents = [polygonCol, polygonWh, textCue, imagePractice, polygonText, textPractice, keyPractice, micPractice]
    for thisComponent in practiceTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practiceTrial" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygonCol* updates
        if polygonCol.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygonCol.frameNStart = frameN  # exact frame index
            polygonCol.tStart = t  # local t and not account for scr refresh
            polygonCol.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygonCol, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygonCol.started')
            polygonCol.setAutoDraw(True)
        if polygonCol.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygonCol.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygonCol.tStop = t  # not accounting for scr refresh
                polygonCol.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygonCol.stopped')
                polygonCol.setAutoDraw(False)
        
        # *polygonWh* updates
        if polygonWh.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygonWh.frameNStart = frameN  # exact frame index
            polygonWh.tStart = t  # local t and not account for scr refresh
            polygonWh.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygonWh, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygonWh.started')
            polygonWh.setAutoDraw(True)
        if polygonWh.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygonWh.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygonWh.tStop = t  # not accounting for scr refresh
                polygonWh.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygonWh.stopped')
                polygonWh.setAutoDraw(False)
        
        # *textCue* updates
        if textCue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textCue.frameNStart = frameN  # exact frame index
            textCue.tStart = t  # local t and not account for scr refresh
            textCue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textCue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textCue.started')
            textCue.setAutoDraw(True)
        if textCue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textCue.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                textCue.tStop = t  # not accounting for scr refresh
                textCue.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textCue.stopped')
                textCue.setAutoDraw(False)
        if textCue.status == STARTED:  # only update if drawing
            textCue.setText(respModal, log=False)
        
        # *imagePractice* updates
        if imagePractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imagePractice.frameNStart = frameN  # exact frame index
            imagePractice.tStart = t  # local t and not account for scr refresh
            imagePractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imagePractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imagePractice.started')
            imagePractice.setAutoDraw(True)
        if imagePractice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imagePractice.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                imagePractice.tStop = t  # not accounting for scr refresh
                imagePractice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imagePractice.stopped')
                imagePractice.setAutoDraw(False)
        
        # *polygonText* updates
        if polygonText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygonText.frameNStart = frameN  # exact frame index
            polygonText.tStart = t  # local t and not account for scr refresh
            polygonText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygonText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygonText.started')
            polygonText.setAutoDraw(True)
        if polygonText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygonText.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygonText.tStop = t  # not accounting for scr refresh
                polygonText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygonText.stopped')
                polygonText.setAutoDraw(False)
        
        # *textPractice* updates
        if textPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textPractice.frameNStart = frameN  # exact frame index
            textPractice.tStart = t  # local t and not account for scr refresh
            textPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textPractice.started')
            textPractice.setAutoDraw(True)
        if textPractice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textPractice.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                textPractice.tStop = t  # not accounting for scr refresh
                textPractice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textPractice.stopped')
                textPractice.setAutoDraw(False)
        if textPractice.status == STARTED:  # only update if drawing
            textPractice.setText(respDisplay, log=False)
        
        # *keyPractice* updates
        waitOnFlip = False
        if keyPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyPractice.frameNStart = frameN  # exact frame index
            keyPractice.tStart = t  # local t and not account for scr refresh
            keyPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyPractice.started')
            keyPractice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyPractice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyPractice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyPractice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keyPractice.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                keyPractice.tStop = t  # not accounting for scr refresh
                keyPractice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keyPractice.stopped')
                keyPractice.status = FINISHED
        if keyPractice.status == STARTED and not waitOnFlip:
            theseKeys = keyPractice.getKeys(keyList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','backspace'], waitRelease=False)
            _keyPractice_allKeys.extend(theseKeys)
            if len(_keyPractice_allKeys):
                keyPractice.keys = [key.name for key in _keyPractice_allKeys]  # storing all keys
                keyPractice.rt = [key.rt for key in _keyPractice_allKeys]
                # was this correct?
                if (keyPractice.keys == str(correctAns)) or (keyPractice.keys == correctAns):
                    keyPractice.corr = 1
                else:
                    keyPractice.corr = 0
        # Run 'Each Frame' code from codePractice
        #if a new key has been pressed since last time
        if(len(keyPractice.keys) > last_len):
            #increment the key logger length
            last_len = len(keyPractice.keys)
            
            #grab the last key added to the keys list
            key_list.append(keyPractice.keys.pop())
        
            #check for backspace
            if("backspace" in key_list):
                key_list.remove("backspace")
        
                #if we have at least 1 character, remove it
                if(len(key_list) > 0):
                    key_list.pop()
        
            #if enter is pressed then...
            #elif("return" in key_list):
                #remove the enter key
                #key_list.pop()
        
                #and end the trial if we have at least 2 digits
                #if(len(key_list) >= 2):
                    #continueRoutine = False
        
        
            #now loop through and remove any extra characters that may exist
            #while(len(key_list) > maxDigits):
                #key_list.pop()
            
            #create a variable to display
            respDisplay = ''.join(key_list)
           
        # check if the participant has started typing for the box to appear behind the sentence
        if len(key_list) > 0:
            polygonText.opacity = 1
        
        # micPractice updates
        if micPractice.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            micPractice.frameNStart = frameN  # exact frame index
            micPractice.tStart = t  # local t and not account for scr refresh
            micPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(micPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('micPractice.started', t)
            # start recording with micPractice
            micPractice.start()
            micPractice.status = STARTED
        if micPractice.status == STARTED:
            # update recorded clip for micPractice
            micPractice.poll()
        if micPractice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > micPractice.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                micPractice.tStop = t  # not accounting for scr refresh
                micPractice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('micPractice.stopped', t)
                # stop recording with micPractice
                micPractice.stop()
                micPractice.status = FINISHED
        # Run 'Each Frame' code from codeMicPractice
        if t > 3:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practiceTrial" ---
    for thisComponent in practiceTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyPractice.keys in ['', [], None]:  # No response was made
        keyPractice.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           keyPractice.corr = 1;  # correct non-response
        else:
           keyPractice.corr = 0;  # failed to respond (incorrectly)
    # store data for trialsPractice (TrialHandler)
    trialsPractice.addData('keyPractice.keys',keyPractice.keys)
    trialsPractice.addData('keyPractice.corr', keyPractice.corr)
    if keyPractice.keys != None:  # we had a response
        trialsPractice.addData('keyPractice.rt', keyPractice.rt)
    # Run 'End Routine' code from codePractice
    thisExp.addData('subjResponse', respDisplay)
    # tell mic to keep hold of current recording in micPractice.clips and transcript (if applicable) in micPractice.scripts
    # this will also update micPractice.lastClip and micPractice.lastScript
    micPractice.stop()
    tag = data.utils.getDateStr()
    micPracticeClip = micPractice.bank(
        tag=tag, transcribe='None',
        config=None
    )
    trialsPractice.addData('micPractice.clip', os.path.join(micPracticeRecFolder, 'recording_micPractice_%s.wav' % tag))
    # Run 'End Routine' code from codeSavePractice
    clipFilename = clipFilename = 'recording_mic_%s.wav' % tag
    #"recording_" + str(count) + ".wav"
    micPractice.lastClip.save(os.path.join(micPracticeRecFolder, clipFilename))
    
    '''
    # save mic recordings
    for tag in mic.clips:
        for i, clip in enumerate(mic.clips[tag]):
            clipFilename = 'recording_mic_%s.wav' % tag
            # if there's more than 1 clip with this tag, append a counter for all beyond the first
            if i > 0:
                clipFilename += '_%s' % i
            clip.save(os.path.join(micRecFolder, clipFilename))
            
    '''
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "blank500" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [textBlank500]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank500" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textBlank500* updates
        if textBlank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBlank500.frameNStart = frameN  # exact frame index
            textBlank500.tStart = t  # local t and not account for scr refresh
            textBlank500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBlank500, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textBlank500.started')
            textBlank500.setAutoDraw(True)
        if textBlank500.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textBlank500.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                textBlank500.tStop = t  # not accounting for scr refresh
                textBlank500.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textBlank500.stopped')
                textBlank500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank500" ---
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsPractice'


# --- Prepare to start Routine "blank500" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blank500Components = [textBlank500]
for thisComponent in blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank500" ---
while continueRoutine and routineTimer.getTime() < 0.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank500* updates
    if textBlank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank500.frameNStart = frameN  # exact frame index
        textBlank500.tStart = t  # local t and not account for scr refresh
        textBlank500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank500, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textBlank500.started')
        textBlank500.setAutoDraw(True)
    if textBlank500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank500.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank500.tStop = t  # not accounting for scr refresh
            textBlank500.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textBlank500.stopped')
            textBlank500.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank500" ---
for thisComponent in blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.500000)

# --- Prepare to start Routine "EndPractice" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textboxEndPracrice.reset()
keyEndPractice.keys = []
keyEndPractice.rt = []
_keyEndPractice_allKeys = []
# keep track of which components have finished
EndPracticeComponents = [textboxEndPracrice, keyEndPractice]
for thisComponent in EndPracticeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EndPractice" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textboxEndPracrice* updates
    if textboxEndPracrice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxEndPracrice.frameNStart = frameN  # exact frame index
        textboxEndPracrice.tStart = t  # local t and not account for scr refresh
        textboxEndPracrice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxEndPracrice, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxEndPracrice.started')
        textboxEndPracrice.setAutoDraw(True)
    
    # *keyEndPractice* updates
    waitOnFlip = False
    if keyEndPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyEndPractice.frameNStart = frameN  # exact frame index
        keyEndPractice.tStart = t  # local t and not account for scr refresh
        keyEndPractice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyEndPractice, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'keyEndPractice.started')
        keyEndPractice.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyEndPractice.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyEndPractice.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyEndPractice.status == STARTED and not waitOnFlip:
        theseKeys = keyEndPractice.getKeys(keyList=['space'], waitRelease=False)
        _keyEndPractice_allKeys.extend(theseKeys)
        if len(_keyEndPractice_allKeys):
            keyEndPractice.keys = _keyEndPractice_allKeys[-1].name  # just the last key pressed
            keyEndPractice.rt = _keyEndPractice_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndPracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EndPractice" ---
for thisComponent in EndPracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyEndPractice.keys in ['', [], None]:  # No response was made
    keyEndPractice.keys = None
thisExp.addData('keyEndPractice.keys',keyEndPractice.keys)
if keyEndPractice.keys != None:  # we had a response
    thisExp.addData('keyEndPractice.rt', keyEndPractice.rt)
thisExp.nextEntry()
# the Routine "EndPractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# save micPractice recordings
for tag in micPractice.clips:
    for i, clip in enumerate(micPractice.clips[tag]):
        clipFilename = 'recording_micPractice_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micPracticeRecFolder, clipFilename))

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
