#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Ιούλιος 21, 2023, at 10:21
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

# Run 'Before Experiment' code from codeSavePractice2
import pandas as pd

count = 0


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'REPSWITCH1_Practice_2_version2'  # from the Builder filename that created this script
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
    originPath='D:\\GitHub\\experiment1\\REPSWITCH1_Practice_2_version2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation
# Make folder to store recordings from micPractice2v2
micPractice2v2RecFolder = filename + '_micPractice2v2_recorded'
if not os.path.isdir(micPractice2v2RecFolder):
    os.mkdir(micPractice2v2RecFolder)

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

# --- Initialize components for Routine "InstructionsPractice_2" ---
textboxInstrPractice_2 = visual.TextBox2(
     win, text='¡Vamos a practicar un poco más ante de empezar!\n\nRecuerda:', font='Open Sans',
     pos=(0, 0.3),     letterHeight=0.03,
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
     name='textboxInstrPractice_2',
     autoLog=True,
)
textboxInstrPractice_2_2 = visual.TextBox2(
     win, text='Si el rectángulo es ', font='Open Sans',
     pos=(0, 0.18),     letterHeight=0.03,
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
     name='textboxInstrPractice_2_2',
     autoLog=True,
)
textboxInstrPractice_2_3 = visual.TextBox2(
     win, text='amarillo,', font='Open Sans',
     pos=(0.255, 0.18),     letterHeight=0.03,
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
     name='textboxInstrPractice_2_3',
     autoLog=True,
)
textboxInstrPractice_2_4 = visual.TextBox2(
     win, text='deberás ', font='Open Sans',
     pos=(0.39, 0.18),     letterHeight=0.03,
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
     name='textboxInstrPractice_2_4',
     autoLog=True,
)
textboxInstrPractice_2_5 = visual.TextBox2(
     win, text='teclear', font='Open Sans',
     pos=(0.51, 0.18),     letterHeight=0.03,
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
     name='textboxInstrPractice_2_5',
     autoLog=True,
)
textboxInstrPractice_2_6 = visual.TextBox2(
     win, text='el nombre de la imagen.  ', font='Open Sans',
     pos=(0.62, 0.18),     letterHeight=0.03,
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
     name='textboxInstrPractice_2_6',
     autoLog=True,
)
textboxInstrPractice_2_7 = visual.TextBox2(
     win, text='Si el rectángulo es ', font='Open Sans',
     pos=(0, 0.1),     letterHeight=0.03,
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
     name='textboxInstrPractice_2_7',
     autoLog=True,
)
textboxInstrPractice_2_8 = visual.TextBox2(
     win, text='azul,', font='Open Sans',
     pos=(0.255, 0.1),     letterHeight=0.03,
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
     name='textboxInstrPractice_2_8',
     autoLog=True,
)
textboxInstrPractice_2_9 = visual.TextBox2(
     win, text='deberás ', font='Open Sans',
     pos=(0.33, 0.1),     letterHeight=0.03,
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
     name='textboxInstrPractice_2_9',
     autoLog=True,
)
textboxInstrPractice_2_10 = visual.TextBox2(
     win, text='repetir en voz alta ', font='Open Sans',
     pos=(0.45, 0.1),     letterHeight=0.03,
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
     name='textboxInstrPractice_2_10',
     autoLog=True,
)
textboxInstrPractice_2_11 = visual.TextBox2(
     win, text='el nombre de la imagen.  ', font='Open Sans',
     pos=(0.73, 0.1),     letterHeight=0.03,
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
     name='textboxInstrPractice_2_11',
     autoLog=True,
)
textboxInstrPractice_2_12 = visual.TextBox2(
     win, text='En esta ocasión, no verás las palabras TECLEA o HABLA y solo deberás utilizar los colores. \n\n\nPulsa la BARRA ESPACIADORA para continuar.', font='Open Sans',
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
     name='textboxInstrPractice_2_12',
     autoLog=True,
)
keyInstrPractice_2 = keyboard.Keyboard()

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

# --- Initialize components for Routine "practiceTrial_2" ---
polygonCol_2 = visual.Rect(
    win=win, name='polygonCol_2',
    width=(0.55, 0.55)[0], height=(0.55, 0.55)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
polygonWh_2 = visual.Rect(
    win=win, name='polygonWh_2',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
imagePractice_2 = visual.ImageStim(
    win=win,
    name='imagePractice_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
polygonText_2 = visual.Rect(
    win=win, name='polygonText_2',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.9216, 0.9216, 0.9216], fillColor=[0.9216, 0.9216, 0.9216],
    opacity=None, depth=-3.0, interpolate=True)
textPractice_2 = visual.TextStim(win=win, name='textPractice_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
keyPractice_2 = keyboard.Keyboard()
micPractice2v2 = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=48000, maxRecordingSize=24000.0
)
# Run 'Begin Experiment' code from codeSavePractice2
# Read the excel file and store it in a pandas DataFrame
data_file = "repswitch_practice_2_version2.xlsx"  
df = pd.read_excel(data_file)

# Get the participant number from the experiment info dialog
participant_number = expInfo['participant']

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

# --- Initialize components for Routine "EndPractice_2" ---
textboxEndPractice_2 = visual.TextBox2(
     win, text='¡Genial! \n\n\nPulsa la BARRA ESPACIADORA para continuar.', font='Open Sans',
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
     name='textboxEndPractice_2',
     autoLog=True,
)
keyEndPractice_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "InstructionsPractice_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textboxInstrPractice_2.reset()
textboxInstrPractice_2_2.reset()
textboxInstrPractice_2_3.reset()
textboxInstrPractice_2_4.reset()
textboxInstrPractice_2_5.reset()
textboxInstrPractice_2_6.reset()
textboxInstrPractice_2_7.reset()
textboxInstrPractice_2_8.reset()
textboxInstrPractice_2_9.reset()
textboxInstrPractice_2_10.reset()
textboxInstrPractice_2_11.reset()
textboxInstrPractice_2_12.reset()
keyInstrPractice_2.keys = []
keyInstrPractice_2.rt = []
_keyInstrPractice_2_allKeys = []
# keep track of which components have finished
InstructionsPractice_2Components = [textboxInstrPractice_2, textboxInstrPractice_2_2, textboxInstrPractice_2_3, textboxInstrPractice_2_4, textboxInstrPractice_2_5, textboxInstrPractice_2_6, textboxInstrPractice_2_7, textboxInstrPractice_2_8, textboxInstrPractice_2_9, textboxInstrPractice_2_10, textboxInstrPractice_2_11, textboxInstrPractice_2_12, keyInstrPractice_2]
for thisComponent in InstructionsPractice_2Components:
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

# --- Run Routine "InstructionsPractice_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
    
    # *textboxInstrPractice_2_2* updates
    if textboxInstrPractice_2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_2_2.frameNStart = frameN  # exact frame index
        textboxInstrPractice_2_2.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_2_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_2_2.started')
        textboxInstrPractice_2_2.setAutoDraw(True)
    
    # *textboxInstrPractice_2_3* updates
    if textboxInstrPractice_2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_2_3.frameNStart = frameN  # exact frame index
        textboxInstrPractice_2_3.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_2_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_2_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_2_3.started')
        textboxInstrPractice_2_3.setAutoDraw(True)
    
    # *textboxInstrPractice_2_4* updates
    if textboxInstrPractice_2_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_2_4.frameNStart = frameN  # exact frame index
        textboxInstrPractice_2_4.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_2_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_2_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_2_4.started')
        textboxInstrPractice_2_4.setAutoDraw(True)
    
    # *textboxInstrPractice_2_5* updates
    if textboxInstrPractice_2_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_2_5.frameNStart = frameN  # exact frame index
        textboxInstrPractice_2_5.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_2_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_2_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_2_5.started')
        textboxInstrPractice_2_5.setAutoDraw(True)
    
    # *textboxInstrPractice_2_6* updates
    if textboxInstrPractice_2_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_2_6.frameNStart = frameN  # exact frame index
        textboxInstrPractice_2_6.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_2_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_2_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_2_6.started')
        textboxInstrPractice_2_6.setAutoDraw(True)
    
    # *textboxInstrPractice_2_7* updates
    if textboxInstrPractice_2_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_2_7.frameNStart = frameN  # exact frame index
        textboxInstrPractice_2_7.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_2_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_2_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_2_7.started')
        textboxInstrPractice_2_7.setAutoDraw(True)
    
    # *textboxInstrPractice_2_8* updates
    if textboxInstrPractice_2_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_2_8.frameNStart = frameN  # exact frame index
        textboxInstrPractice_2_8.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_2_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_2_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_2_8.started')
        textboxInstrPractice_2_8.setAutoDraw(True)
    
    # *textboxInstrPractice_2_9* updates
    if textboxInstrPractice_2_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_2_9.frameNStart = frameN  # exact frame index
        textboxInstrPractice_2_9.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_2_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_2_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_2_9.started')
        textboxInstrPractice_2_9.setAutoDraw(True)
    
    # *textboxInstrPractice_2_10* updates
    if textboxInstrPractice_2_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_2_10.frameNStart = frameN  # exact frame index
        textboxInstrPractice_2_10.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_2_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_2_10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_2_10.started')
        textboxInstrPractice_2_10.setAutoDraw(True)
    
    # *textboxInstrPractice_2_11* updates
    if textboxInstrPractice_2_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_2_11.frameNStart = frameN  # exact frame index
        textboxInstrPractice_2_11.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_2_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_2_11, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_2_11.started')
        textboxInstrPractice_2_11.setAutoDraw(True)
    
    # *textboxInstrPractice_2_12* updates
    if textboxInstrPractice_2_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrPractice_2_12.frameNStart = frameN  # exact frame index
        textboxInstrPractice_2_12.tStart = t  # local t and not account for scr refresh
        textboxInstrPractice_2_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrPractice_2_12, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrPractice_2_12.started')
        textboxInstrPractice_2_12.setAutoDraw(True)
    
    # *keyInstrPractice_2* updates
    waitOnFlip = False
    if keyInstrPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyInstrPractice_2.frameNStart = frameN  # exact frame index
        keyInstrPractice_2.tStart = t  # local t and not account for scr refresh
        keyInstrPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyInstrPractice_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'keyInstrPractice_2.started')
        keyInstrPractice_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyInstrPractice_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyInstrPractice_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyInstrPractice_2.status == STARTED and not waitOnFlip:
        theseKeys = keyInstrPractice_2.getKeys(keyList=['space'], waitRelease=False)
        _keyInstrPractice_2_allKeys.extend(theseKeys)
        if len(_keyInstrPractice_2_allKeys):
            keyInstrPractice_2.keys = _keyInstrPractice_2_allKeys[-1].name  # just the last key pressed
            keyInstrPractice_2.rt = _keyInstrPractice_2_allKeys[-1].rt
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
    for thisComponent in InstructionsPractice_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "InstructionsPractice_2" ---
for thisComponent in InstructionsPractice_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyInstrPractice_2.keys in ['', [], None]:  # No response was made
    keyInstrPractice_2.keys = None
thisExp.addData('keyInstrPractice_2.keys',keyInstrPractice_2.keys)
if keyInstrPractice_2.keys != None:  # we had a response
    thisExp.addData('keyInstrPractice_2.rt', keyInstrPractice_2.rt)
thisExp.nextEntry()
# the Routine "InstructionsPractice_2" was not non-slip safe, so reset the non-slip timer
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
trialsPractice_2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('repswitch_practice_2_version2.xlsx'),
    seed=None, name='trialsPractice_2')
thisExp.addLoop(trialsPractice_2)  # add the loop to the experiment
thisTrialsPractice_2 = trialsPractice_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsPractice_2.rgb)
if thisTrialsPractice_2 != None:
    for paramName in thisTrialsPractice_2:
        exec('{} = thisTrialsPractice_2[paramName]'.format(paramName))

for thisTrialsPractice_2 in trialsPractice_2:
    currentLoop = trialsPractice_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsPractice_2.rgb)
    if thisTrialsPractice_2 != None:
        for paramName in thisTrialsPractice_2:
            exec('{} = thisTrialsPractice_2[paramName]'.format(paramName))
    
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
    
    # --- Prepare to start Routine "practiceTrial_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    polygonCol_2.setFillColor(frameColor)
    polygonCol_2.setLineColor(frameColor)
    imagePractice_2.setImage(image)
    keyPractice_2.keys = []
    keyPractice_2.rt = []
    _keyPractice_2_allKeys = []
    # Run 'Begin Routine' code from codePractice_2
    respDisplay = ""
    
    
    #key logger defaults
    last_len = 0
    key_list = []
    
    polygonText_2.opacity = 0  
    # Run 'Begin Routine' code from codeSavePractice2
    count = count + 1
    
    #Retrieve the value of 'correctAns' for the current trial
    correctAns = df.loc[count - 1, 'correctAns']
    # keep track of which components have finished
    practiceTrial_2Components = [polygonCol_2, polygonWh_2, imagePractice_2, polygonText_2, textPractice_2, keyPractice_2, micPractice2v2]
    for thisComponent in practiceTrial_2Components:
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
    
    # --- Run Routine "practiceTrial_2" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygonCol_2* updates
        if polygonCol_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygonCol_2.frameNStart = frameN  # exact frame index
            polygonCol_2.tStart = t  # local t and not account for scr refresh
            polygonCol_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygonCol_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygonCol_2.started')
            polygonCol_2.setAutoDraw(True)
        if polygonCol_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygonCol_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygonCol_2.tStop = t  # not accounting for scr refresh
                polygonCol_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygonCol_2.stopped')
                polygonCol_2.setAutoDraw(False)
        
        # *polygonWh_2* updates
        if polygonWh_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygonWh_2.frameNStart = frameN  # exact frame index
            polygonWh_2.tStart = t  # local t and not account for scr refresh
            polygonWh_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygonWh_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygonWh_2.started')
            polygonWh_2.setAutoDraw(True)
        if polygonWh_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygonWh_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygonWh_2.tStop = t  # not accounting for scr refresh
                polygonWh_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygonWh_2.stopped')
                polygonWh_2.setAutoDraw(False)
        
        # *imagePractice_2* updates
        if imagePractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imagePractice_2.frameNStart = frameN  # exact frame index
            imagePractice_2.tStart = t  # local t and not account for scr refresh
            imagePractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imagePractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imagePractice_2.started')
            imagePractice_2.setAutoDraw(True)
        if imagePractice_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imagePractice_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                imagePractice_2.tStop = t  # not accounting for scr refresh
                imagePractice_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imagePractice_2.stopped')
                imagePractice_2.setAutoDraw(False)
        
        # *polygonText_2* updates
        if polygonText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygonText_2.frameNStart = frameN  # exact frame index
            polygonText_2.tStart = t  # local t and not account for scr refresh
            polygonText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygonText_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygonText_2.started')
            polygonText_2.setAutoDraw(True)
        if polygonText_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygonText_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygonText_2.tStop = t  # not accounting for scr refresh
                polygonText_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygonText_2.stopped')
                polygonText_2.setAutoDraw(False)
        
        # *textPractice_2* updates
        if textPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textPractice_2.frameNStart = frameN  # exact frame index
            textPractice_2.tStart = t  # local t and not account for scr refresh
            textPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textPractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textPractice_2.started')
            textPractice_2.setAutoDraw(True)
        if textPractice_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textPractice_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                textPractice_2.tStop = t  # not accounting for scr refresh
                textPractice_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textPractice_2.stopped')
                textPractice_2.setAutoDraw(False)
        if textPractice_2.status == STARTED:  # only update if drawing
            textPractice_2.setText(respDisplay, log=False)
        
        # *keyPractice_2* updates
        waitOnFlip = False
        if keyPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyPractice_2.frameNStart = frameN  # exact frame index
            keyPractice_2.tStart = t  # local t and not account for scr refresh
            keyPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyPractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyPractice_2.started')
            keyPractice_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyPractice_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyPractice_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyPractice_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keyPractice_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                keyPractice_2.tStop = t  # not accounting for scr refresh
                keyPractice_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keyPractice_2.stopped')
                keyPractice_2.status = FINISHED
        if keyPractice_2.status == STARTED and not waitOnFlip:
            theseKeys = keyPractice_2.getKeys(keyList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','backspace'], waitRelease=False)
            _keyPractice_2_allKeys.extend(theseKeys)
            if len(_keyPractice_2_allKeys):
                keyPractice_2.keys = [key.name for key in _keyPractice_2_allKeys]  # storing all keys
                keyPractice_2.rt = [key.rt for key in _keyPractice_2_allKeys]
                # was this correct?
                if (keyPractice_2.keys == str(correctAns)) or (keyPractice_2.keys == correctAns):
                    keyPractice_2.corr = 1
                else:
                    keyPractice_2.corr = 0
        # Run 'Each Frame' code from codePractice_2
        #if a new key has been pressed since last time
        if(len(keyPractice_2.keys) > last_len):
            #increment the key logger length
            last_len = len(keyPractice_2.keys)
            
            #grab the last key added to the keys list
            key_list.append(keyPractice_2.keys.pop())
        
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
            polygonText_2.opacity = 1
        
        # micPractice2v2 updates
        if micPractice2v2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            micPractice2v2.frameNStart = frameN  # exact frame index
            micPractice2v2.tStart = t  # local t and not account for scr refresh
            micPractice2v2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(micPractice2v2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('micPractice2v2.started', t)
            # start recording with micPractice2v2
            micPractice2v2.start()
            micPractice2v2.status = STARTED
        if micPractice2v2.status == STARTED:
            # update recorded clip for micPractice2v2
            micPractice2v2.poll()
        if micPractice2v2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > micPractice2v2.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                micPractice2v2.tStop = t  # not accounting for scr refresh
                micPractice2v2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('micPractice2v2.stopped', t)
                # stop recording with micPractice2v2
                micPractice2v2.stop()
                micPractice2v2.status = FINISHED
        # Run 'Each Frame' code from codeMicPractice2
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
        for thisComponent in practiceTrial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practiceTrial_2" ---
    for thisComponent in practiceTrial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyPractice_2.keys in ['', [], None]:  # No response was made
        keyPractice_2.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           keyPractice_2.corr = 1;  # correct non-response
        else:
           keyPractice_2.corr = 0;  # failed to respond (incorrectly)
    # store data for trialsPractice_2 (TrialHandler)
    trialsPractice_2.addData('keyPractice_2.keys',keyPractice_2.keys)
    trialsPractice_2.addData('keyPractice_2.corr', keyPractice_2.corr)
    if keyPractice_2.keys != None:  # we had a response
        trialsPractice_2.addData('keyPractice_2.rt', keyPractice_2.rt)
    # Run 'End Routine' code from codePractice_2
    thisExp.addData('subjResponse', respDisplay)
    # tell mic to keep hold of current recording in micPractice2v2.clips and transcript (if applicable) in micPractice2v2.scripts
    # this will also update micPractice2v2.lastClip and micPractice2v2.lastScript
    micPractice2v2.stop()
    tag = data.utils.getDateStr()
    micPractice2v2Clip = micPractice2v2.bank(
        tag=tag, transcribe='None',
        config=None
    )
    trialsPractice_2.addData('micPractice2v2.clip', os.path.join(micPractice2v2RecFolder, 'recording_micPractice2v2_%s.wav' % tag))
    # Run 'End Routine' code from codeSavePractice2
    clipFilename = f"recording_Practice2v2_p{participant_number}_trial{str(count)}_{correctAns}_%s.wav" % tag
    #"recording_" + str(count) + ".wav"
    micPractice2v2.lastClip.save(os.path.join(micPractice2v2RecFolder, clipFilename))
    
    
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
    
# completed 1.0 repeats of 'trialsPractice_2'


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

# --- Prepare to start Routine "EndPractice_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textboxEndPractice_2.reset()
keyEndPractice_2.keys = []
keyEndPractice_2.rt = []
_keyEndPractice_2_allKeys = []
# keep track of which components have finished
EndPractice_2Components = [textboxEndPractice_2, keyEndPractice_2]
for thisComponent in EndPractice_2Components:
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

# --- Run Routine "EndPractice_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textboxEndPractice_2* updates
    if textboxEndPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxEndPractice_2.frameNStart = frameN  # exact frame index
        textboxEndPractice_2.tStart = t  # local t and not account for scr refresh
        textboxEndPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxEndPractice_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxEndPractice_2.started')
        textboxEndPractice_2.setAutoDraw(True)
    
    # *keyEndPractice_2* updates
    waitOnFlip = False
    if keyEndPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyEndPractice_2.frameNStart = frameN  # exact frame index
        keyEndPractice_2.tStart = t  # local t and not account for scr refresh
        keyEndPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyEndPractice_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'keyEndPractice_2.started')
        keyEndPractice_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyEndPractice_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyEndPractice_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyEndPractice_2.status == STARTED and not waitOnFlip:
        theseKeys = keyEndPractice_2.getKeys(keyList=['space'], waitRelease=False)
        _keyEndPractice_2_allKeys.extend(theseKeys)
        if len(_keyEndPractice_2_allKeys):
            keyEndPractice_2.keys = _keyEndPractice_2_allKeys[-1].name  # just the last key pressed
            keyEndPractice_2.rt = _keyEndPractice_2_allKeys[-1].rt
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
    for thisComponent in EndPractice_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EndPractice_2" ---
for thisComponent in EndPractice_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyEndPractice_2.keys in ['', [], None]:  # No response was made
    keyEndPractice_2.keys = None
thisExp.addData('keyEndPractice_2.keys',keyEndPractice_2.keys)
if keyEndPractice_2.keys != None:  # we had a response
    thisExp.addData('keyEndPractice_2.rt', keyEndPractice_2.rt)
thisExp.nextEntry()
# the Routine "EndPractice_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# save micPractice2v2 recordings
for tag in micPractice2v2.clips:
    for i, clip in enumerate(micPractice2v2.clips[tag]):
        clipFilename = 'recording_micPractice2v2_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micPractice2v2RecFolder, clipFilename))

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
