#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Ιούλιος 04, 2023, at 12:25
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.4')


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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'REPSWITCH1_v2022.2.4'  # from the Builder filename that created this script
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
    originPath='D:\\GitHub\\experiment1\\REPSWITCH1_v2022.2.4 - Copy.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation
# Make folder to store recordings from micResp
micRespRecFolder = filename + '_micResp_recorded'
if not os.path.isdir(micRespRecFolder):
    os.mkdir(micRespRecFolder)

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

# --- Initialize components for Routine "Welcome" ---
textWelcome = visual.TextStim(win=win, name='textWelcome',
    text='We are going to start the experiment!',
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

# --- Initialize components for Routine "InstructionsMain1" ---
textboxInstrMain1 = visual.TextBox2(
     win, text='A few reminders before we start: \n\nYou should name the images ', font='Open Sans',
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
     name='textboxInstrMain1',
     autoLog=True,
)
textboxInstrMain1_2 = visual.TextBox2(
     win, text='as fast and accurately as possible.\n', font='Open Sans',
     pos=(0.4, 0.2358),     letterHeight=0.03,
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
     name='textboxInstrMain1_2',
     autoLog=True,
)
textboxInstrMain1_3 = visual.TextBox2(
     win, text='\nWhen you speak, make sure you say only one word, in a clear voice.\n\nTry to keep your hands above the keyboard during the whole session. \n\nAnd please, don’t speak while typing!\n\n\nYou will be able to take a short break every N minutes.\n\n\nPress SPACE to continue\n\n', font='Open Sans',
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
     name='textboxInstrMain1_3',
     autoLog=True,
)
keyInstrMain = keyboard.Keyboard()

# --- Initialize components for Routine "InstructionsMain2" ---
textboxInstrMain2 = visual.TextBox2(
     win, text='Remember: ', font='Open Sans',
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
     name='textboxInstrMain2',
     autoLog=True,
)
textboxInstrMain2_2 = visual.TextBox2(
     win, text='If the rectangle is ', font='Open Sans',
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
     name='textboxInstrMain2_2',
     autoLog=True,
)
textboxInstrMain2_3 = visual.TextBox2(
     win, text='blue,', font='Open Sans',
     pos=(0.245, 0.2),     letterHeight=0.03,
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
     name='textboxInstrMain2_3',
     autoLog=True,
)
textboxInstrMain2_4 = visual.TextBox2(
     win, text=' you will need to ', font='Open Sans',
     pos=(0.32, 0.2),     letterHeight=0.03,
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
     name='textboxInstrMain2_4',
     autoLog=True,
)
textboxInstrMain2_5 = visual.TextBox2(
     win, text='type', font='Open Sans',
     pos=(0.55, 0.2),     letterHeight=0.03,
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
     name='textboxInstrMain2_5',
     autoLog=True,
)
textboxInstrMain2_6 = visual.TextBox2(
     win, text='the name of the picture.', font='Open Sans',
     pos=(0.625, 0.2),     letterHeight=0.03,
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
     name='textboxInstrMain2_6',
     autoLog=True,
)
textboxInstrMain2_7 = visual.TextBox2(
     win, text='If the rectangle is ', font='Open Sans',
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
     name='textboxInstrMain2_7',
     autoLog=True,
)
textboxInstrMain2_8 = visual.TextBox2(
     win, text='yellow,', font='Open Sans',
     pos=(0.245, 0.1),     letterHeight=0.03,
     size=(None, None), borderWidth=2.0,
     color=[1.0000, 1.0000, -1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='textboxInstrMain2_8',
     autoLog=True,
)
textboxInstrMain2_9 = visual.TextBox2(
     win, text='you will have to ', font='Open Sans',
     pos=(0.365, 0.1),     letterHeight=0.03,
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
     name='textboxInstrMain2_9',
     autoLog=True,
)
textboxInstrMain2_10 = visual.TextBox2(
     win, text='say out loud', font='Open Sans',
     pos=(0.59, 0.1),     letterHeight=0.03,
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
     name='textboxInstrMain2_10',
     autoLog=True,
)
textboxInstrMain2_11 = visual.TextBox2(
     win, text='the name of the picture.', font='Open Sans',
     pos=(0.78, 0.1),     letterHeight=0.03,
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
     name='textboxInstrMain2_11',
     autoLog=True,
)
textboxInstrMain2_12 = visual.TextBox2(
     win, text='Press SPACE to begin!', font='Open Sans',
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
     name='textboxInstrMain2_12',
     autoLog=True,
)
keyInstrMain2 = keyboard.Keyboard()

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

# --- Initialize components for Routine "trial" ---
polygonColour = visual.Rect(
    win=win, name='polygonColour',
    width=(0.55, 0.55)[0], height=(0.55, 0.55)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
polygonWhite = visual.Rect(
    win=win, name='polygonWhite',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
imageObject = visual.ImageStim(
    win=win,
    name='imageObject', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
polygonType = visual.Rect(
    win=win, name='polygonType',
    width=(0.3, 0.1)[0], height=(0.3, 0.1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.9216, 0.9216, 0.9216], fillColor=[0.9216, 0.9216, 0.9216],
    opacity=None, depth=-3.0, interpolate=True)
textInput = visual.TextStim(win=win, name='textInput',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
keyResp = keyboard.Keyboard()
micResp = sound.microphone.Microphone(
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

# --- Initialize components for Routine "pause" ---
textboxPause = visual.TextBox2(
     win, text='Short break!\n\nPress SPACE to continue.', font='Open Sans',
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
     name='textboxPause',
     autoLog=True,
)
keyPause = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
textBlank500 = visual.TextStim(win=win, name='textBlank500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Goodbye" ---
textboxGoodbye = visual.TextBox2(
     win, text='This is the end of the experiment!\n\nThank you for participating!', font='Open Sans',
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
     name='textboxGoodbye',
     autoLog=True,
)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
WelcomeComponents = [textWelcome]
for thisComponent in WelcomeComponents:
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

# --- Run Routine "Welcome" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcome* updates
    if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcome.frameNStart = frameN  # exact frame index
        textWelcome.tStart = t  # local t and not account for scr refresh
        textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textWelcome.started')
        textWelcome.setAutoDraw(True)
    if textWelcome.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textWelcome.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            textWelcome.tStop = t  # not accounting for scr refresh
            textWelcome.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textWelcome.stopped')
            textWelcome.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

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

# --- Prepare to start Routine "InstructionsMain1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textboxInstrMain1.reset()
textboxInstrMain1_2.reset()
textboxInstrMain1_3.reset()
keyInstrMain.keys = []
keyInstrMain.rt = []
_keyInstrMain_allKeys = []
# keep track of which components have finished
InstructionsMain1Components = [textboxInstrMain1, textboxInstrMain1_2, textboxInstrMain1_3, keyInstrMain]
for thisComponent in InstructionsMain1Components:
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

# --- Run Routine "InstructionsMain1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textboxInstrMain1* updates
    if textboxInstrMain1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrMain1.frameNStart = frameN  # exact frame index
        textboxInstrMain1.tStart = t  # local t and not account for scr refresh
        textboxInstrMain1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrMain1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrMain1.started')
        textboxInstrMain1.setAutoDraw(True)
    
    # *textboxInstrMain1_2* updates
    if textboxInstrMain1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrMain1_2.frameNStart = frameN  # exact frame index
        textboxInstrMain1_2.tStart = t  # local t and not account for scr refresh
        textboxInstrMain1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrMain1_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrMain1_2.started')
        textboxInstrMain1_2.setAutoDraw(True)
    
    # *textboxInstrMain1_3* updates
    if textboxInstrMain1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrMain1_3.frameNStart = frameN  # exact frame index
        textboxInstrMain1_3.tStart = t  # local t and not account for scr refresh
        textboxInstrMain1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrMain1_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrMain1_3.started')
        textboxInstrMain1_3.setAutoDraw(True)
    
    # *keyInstrMain* updates
    waitOnFlip = False
    if keyInstrMain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyInstrMain.frameNStart = frameN  # exact frame index
        keyInstrMain.tStart = t  # local t and not account for scr refresh
        keyInstrMain.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyInstrMain, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'keyInstrMain.started')
        keyInstrMain.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyInstrMain.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyInstrMain.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyInstrMain.status == STARTED and not waitOnFlip:
        theseKeys = keyInstrMain.getKeys(keyList=['space'], waitRelease=False)
        _keyInstrMain_allKeys.extend(theseKeys)
        if len(_keyInstrMain_allKeys):
            keyInstrMain.keys = _keyInstrMain_allKeys[-1].name  # just the last key pressed
            keyInstrMain.rt = _keyInstrMain_allKeys[-1].rt
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
    for thisComponent in InstructionsMain1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "InstructionsMain1" ---
for thisComponent in InstructionsMain1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyInstrMain.keys in ['', [], None]:  # No response was made
    keyInstrMain.keys = None
thisExp.addData('keyInstrMain.keys',keyInstrMain.keys)
if keyInstrMain.keys != None:  # we had a response
    thisExp.addData('keyInstrMain.rt', keyInstrMain.rt)
thisExp.nextEntry()
# the Routine "InstructionsMain1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "InstructionsMain2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textboxInstrMain2.reset()
textboxInstrMain2_2.reset()
textboxInstrMain2_3.reset()
textboxInstrMain2_4.reset()
textboxInstrMain2_5.reset()
textboxInstrMain2_6.reset()
textboxInstrMain2_7.reset()
textboxInstrMain2_8.reset()
textboxInstrMain2_9.reset()
textboxInstrMain2_10.reset()
textboxInstrMain2_11.reset()
textboxInstrMain2_12.reset()
keyInstrMain2.keys = []
keyInstrMain2.rt = []
_keyInstrMain2_allKeys = []
# keep track of which components have finished
InstructionsMain2Components = [textboxInstrMain2, textboxInstrMain2_2, textboxInstrMain2_3, textboxInstrMain2_4, textboxInstrMain2_5, textboxInstrMain2_6, textboxInstrMain2_7, textboxInstrMain2_8, textboxInstrMain2_9, textboxInstrMain2_10, textboxInstrMain2_11, textboxInstrMain2_12, keyInstrMain2]
for thisComponent in InstructionsMain2Components:
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

# --- Run Routine "InstructionsMain2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textboxInstrMain2* updates
    if textboxInstrMain2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrMain2.frameNStart = frameN  # exact frame index
        textboxInstrMain2.tStart = t  # local t and not account for scr refresh
        textboxInstrMain2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrMain2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrMain2.started')
        textboxInstrMain2.setAutoDraw(True)
    
    # *textboxInstrMain2_2* updates
    if textboxInstrMain2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrMain2_2.frameNStart = frameN  # exact frame index
        textboxInstrMain2_2.tStart = t  # local t and not account for scr refresh
        textboxInstrMain2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrMain2_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrMain2_2.started')
        textboxInstrMain2_2.setAutoDraw(True)
    
    # *textboxInstrMain2_3* updates
    if textboxInstrMain2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrMain2_3.frameNStart = frameN  # exact frame index
        textboxInstrMain2_3.tStart = t  # local t and not account for scr refresh
        textboxInstrMain2_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrMain2_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrMain2_3.started')
        textboxInstrMain2_3.setAutoDraw(True)
    
    # *textboxInstrMain2_4* updates
    if textboxInstrMain2_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrMain2_4.frameNStart = frameN  # exact frame index
        textboxInstrMain2_4.tStart = t  # local t and not account for scr refresh
        textboxInstrMain2_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrMain2_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrMain2_4.started')
        textboxInstrMain2_4.setAutoDraw(True)
    
    # *textboxInstrMain2_5* updates
    if textboxInstrMain2_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrMain2_5.frameNStart = frameN  # exact frame index
        textboxInstrMain2_5.tStart = t  # local t and not account for scr refresh
        textboxInstrMain2_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrMain2_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrMain2_5.started')
        textboxInstrMain2_5.setAutoDraw(True)
    
    # *textboxInstrMain2_6* updates
    if textboxInstrMain2_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrMain2_6.frameNStart = frameN  # exact frame index
        textboxInstrMain2_6.tStart = t  # local t and not account for scr refresh
        textboxInstrMain2_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrMain2_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrMain2_6.started')
        textboxInstrMain2_6.setAutoDraw(True)
    
    # *textboxInstrMain2_7* updates
    if textboxInstrMain2_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrMain2_7.frameNStart = frameN  # exact frame index
        textboxInstrMain2_7.tStart = t  # local t and not account for scr refresh
        textboxInstrMain2_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrMain2_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrMain2_7.started')
        textboxInstrMain2_7.setAutoDraw(True)
    
    # *textboxInstrMain2_8* updates
    if textboxInstrMain2_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrMain2_8.frameNStart = frameN  # exact frame index
        textboxInstrMain2_8.tStart = t  # local t and not account for scr refresh
        textboxInstrMain2_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrMain2_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrMain2_8.started')
        textboxInstrMain2_8.setAutoDraw(True)
    
    # *textboxInstrMain2_9* updates
    if textboxInstrMain2_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrMain2_9.frameNStart = frameN  # exact frame index
        textboxInstrMain2_9.tStart = t  # local t and not account for scr refresh
        textboxInstrMain2_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrMain2_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrMain2_9.started')
        textboxInstrMain2_9.setAutoDraw(True)
    
    # *textboxInstrMain2_10* updates
    if textboxInstrMain2_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrMain2_10.frameNStart = frameN  # exact frame index
        textboxInstrMain2_10.tStart = t  # local t and not account for scr refresh
        textboxInstrMain2_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrMain2_10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrMain2_10.started')
        textboxInstrMain2_10.setAutoDraw(True)
    
    # *textboxInstrMain2_11* updates
    if textboxInstrMain2_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrMain2_11.frameNStart = frameN  # exact frame index
        textboxInstrMain2_11.tStart = t  # local t and not account for scr refresh
        textboxInstrMain2_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrMain2_11, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrMain2_11.started')
        textboxInstrMain2_11.setAutoDraw(True)
    
    # *textboxInstrMain2_12* updates
    if textboxInstrMain2_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxInstrMain2_12.frameNStart = frameN  # exact frame index
        textboxInstrMain2_12.tStart = t  # local t and not account for scr refresh
        textboxInstrMain2_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxInstrMain2_12, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxInstrMain2_12.started')
        textboxInstrMain2_12.setAutoDraw(True)
    
    # *keyInstrMain2* updates
    waitOnFlip = False
    if keyInstrMain2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyInstrMain2.frameNStart = frameN  # exact frame index
        keyInstrMain2.tStart = t  # local t and not account for scr refresh
        keyInstrMain2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyInstrMain2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'keyInstrMain2.started')
        keyInstrMain2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyInstrMain2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyInstrMain2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyInstrMain2.status == STARTED and not waitOnFlip:
        theseKeys = keyInstrMain2.getKeys(keyList=['space'], waitRelease=False)
        _keyInstrMain2_allKeys.extend(theseKeys)
        if len(_keyInstrMain2_allKeys):
            keyInstrMain2.keys = _keyInstrMain2_allKeys[-1].name  # just the last key pressed
            keyInstrMain2.rt = _keyInstrMain2_allKeys[-1].rt
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
    for thisComponent in InstructionsMain2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "InstructionsMain2" ---
for thisComponent in InstructionsMain2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyInstrMain2.keys in ['', [], None]:  # No response was made
    keyInstrMain2.keys = None
thisExp.addData('keyInstrMain2.keys',keyInstrMain2.keys)
if keyInstrMain2.keys != None:  # we had a response
    thisExp.addData('keyInstrMain2.rt', keyInstrMain2.rt)
thisExp.nextEntry()
# the Routine "InstructionsMain2" was not non-slip safe, so reset the non-slip timer
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
trialsREPSWITCH = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('repswitch.xlsx'),
    seed=None, name='trialsREPSWITCH')
thisExp.addLoop(trialsREPSWITCH)  # add the loop to the experiment
thisTrialsREPSWITCH = trialsREPSWITCH.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsREPSWITCH.rgb)
if thisTrialsREPSWITCH != None:
    for paramName in thisTrialsREPSWITCH:
        exec('{} = thisTrialsREPSWITCH[paramName]'.format(paramName))

for thisTrialsREPSWITCH in trialsREPSWITCH:
    currentLoop = trialsREPSWITCH
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsREPSWITCH.rgb)
    if thisTrialsREPSWITCH != None:
        for paramName in thisTrialsREPSWITCH:
            exec('{} = thisTrialsREPSWITCH[paramName]'.format(paramName))
    
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
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    polygonColour.setFillColor(frameColor)
    polygonColour.setLineColor(frameColor)
    imageObject.setImage(image)
    keyResp.keys = []
    keyResp.rt = []
    _keyResp_allKeys = []
    # Run 'Begin Routine' code from codeResp
    respDisplay = ""
    
    
    #key logger defaults
    last_len = 0
    key_list = []
    
    polygonType.opacity = 0  
    
    # keep track of which components have finished
    trialComponents = [polygonColour, polygonWhite, imageObject, polygonType, textInput, keyResp, micResp]
    for thisComponent in trialComponents:
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
    
    # --- Run Routine "trial" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygonColour* updates
        if polygonColour.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygonColour.frameNStart = frameN  # exact frame index
            polygonColour.tStart = t  # local t and not account for scr refresh
            polygonColour.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygonColour, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygonColour.started')
            polygonColour.setAutoDraw(True)
        if polygonColour.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygonColour.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygonColour.tStop = t  # not accounting for scr refresh
                polygonColour.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygonColour.stopped')
                polygonColour.setAutoDraw(False)
        
        # *polygonWhite* updates
        if polygonWhite.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygonWhite.frameNStart = frameN  # exact frame index
            polygonWhite.tStart = t  # local t and not account for scr refresh
            polygonWhite.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygonWhite, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygonWhite.started')
            polygonWhite.setAutoDraw(True)
        if polygonWhite.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygonWhite.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygonWhite.tStop = t  # not accounting for scr refresh
                polygonWhite.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygonWhite.stopped')
                polygonWhite.setAutoDraw(False)
        
        # *imageObject* updates
        if imageObject.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageObject.frameNStart = frameN  # exact frame index
            imageObject.tStart = t  # local t and not account for scr refresh
            imageObject.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageObject, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageObject.started')
            imageObject.setAutoDraw(True)
        if imageObject.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageObject.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                imageObject.tStop = t  # not accounting for scr refresh
                imageObject.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageObject.stopped')
                imageObject.setAutoDraw(False)
        
        # *polygonType* updates
        if polygonType.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygonType.frameNStart = frameN  # exact frame index
            polygonType.tStart = t  # local t and not account for scr refresh
            polygonType.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygonType, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygonType.started')
            polygonType.setAutoDraw(True)
        if polygonType.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygonType.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygonType.tStop = t  # not accounting for scr refresh
                polygonType.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygonType.stopped')
                polygonType.setAutoDraw(False)
        
        # *textInput* updates
        if textInput.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textInput.frameNStart = frameN  # exact frame index
            textInput.tStart = t  # local t and not account for scr refresh
            textInput.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInput, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInput.started')
            textInput.setAutoDraw(True)
        if textInput.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textInput.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                textInput.tStop = t  # not accounting for scr refresh
                textInput.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textInput.stopped')
                textInput.setAutoDraw(False)
        if textInput.status == STARTED:  # only update if drawing
            textInput.setText(respDisplay, log=False)
        
        # *keyResp* updates
        waitOnFlip = False
        if keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyResp.frameNStart = frameN  # exact frame index
            keyResp.tStart = t  # local t and not account for scr refresh
            keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyResp.started')
            keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keyResp.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                keyResp.tStop = t  # not accounting for scr refresh
                keyResp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keyResp.stopped')
                keyResp.status = FINISHED
        if keyResp.status == STARTED and not waitOnFlip:
            theseKeys = keyResp.getKeys(keyList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','backspace'], waitRelease=False)
            _keyResp_allKeys.extend(theseKeys)
            if len(_keyResp_allKeys):
                keyResp.keys = [key.name for key in _keyResp_allKeys]  # storing all keys
                keyResp.rt = [key.rt for key in _keyResp_allKeys]
                # was this correct?
                if (keyResp.keys == str(correctAns)) or (keyResp.keys == correctAns):
                    keyResp.corr = 1
                else:
                    keyResp.corr = 0
        # Run 'Each Frame' code from codeResp
        #if a new key has been pressed since last time
        if(len(keyResp.keys) > last_len):
            #increment the key logger length
            last_len = len(keyResp.keys)
            
            #grab the last key added to the keys list
            key_list.append(keyResp.keys.pop())
        
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
            polygonType.opacity = 1
        
        # micResp updates
        if micResp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            micResp.frameNStart = frameN  # exact frame index
            micResp.tStart = t  # local t and not account for scr refresh
            micResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(micResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('micResp.started', t)
            # start recording with micResp
            micResp.start()
            micResp.status = STARTED
        if micResp.status == STARTED:
            # update recorded clip for micResp
            micResp.poll()
        if micResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > micResp.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                micResp.tStop = t  # not accounting for scr refresh
                micResp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('micResp.stopped', t)
                # save micResp recordings
                for tag in micResp.clips:
                    for i, clip in enumerate(micResp.clips[tag]):
                        clipFilename = 'recording_micResp_%s.wav' % tag
                        # if there's more than 1 clip with this tag, append a counter for all beyond the first
                        if i > 0:
                            clipFilename += '_%s' % i
                        clip.save(os.path.join(micRespRecFolder, clipFilename))
                # stop recording with micResp
                micResp.stop()
                micResp.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyResp.keys in ['', [], None]:  # No response was made
        keyResp.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           keyResp.corr = 1;  # correct non-response
        else:
           keyResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trialsREPSWITCH (TrialHandler)
    trialsREPSWITCH.addData('keyResp.keys',keyResp.keys)
    trialsREPSWITCH.addData('keyResp.corr', keyResp.corr)
    if keyResp.keys != None:  # we had a response
        trialsREPSWITCH.addData('keyResp.rt', keyResp.rt)
    # Run 'End Routine' code from codeResp
    thisExp.addData('subjResponse', respDisplay)
    # tell mic to keep hold of current recording in micResp.clips and transcript (if applicable) in micResp.scripts
    # this will also update micResp.lastClip and micResp.lastScript
    #micResp.stop()
    tag = data.utils.getDateStr()
    micRespClip = micResp.bank(
        tag=tag, transcribe='None',
        config=None
    )
    trialsREPSWITCH.addData('micResp.clip', os.path.join(micRespRecFolder, 'recording_micResp_%s.wav' % tag))
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
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
    
    # --- Prepare to start Routine "pause" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    textboxPause.reset()
    keyPause.keys = []
    keyPause.rt = []
    _keyPause_allKeys = []
    # Run 'Begin Routine' code from codePause
    if trialsREPSWITCH.thisN == 0 or trialsREPSWITCH.thisN % 95 != 0:
        continueRoutine = False
        
        #checks if the value of trialsREPSWITCH.thisN is either 0 or not divisible evenly by 95
        #If either of these conditions is true, the continueRoutine variable is set to False, 
        #indicating that some loop or routine should be skipped or terminated.
    # keep track of which components have finished
    pauseComponents = [textboxPause, keyPause]
    for thisComponent in pauseComponents:
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
    
    # --- Run Routine "pause" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textboxPause* updates
        if textboxPause.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textboxPause.frameNStart = frameN  # exact frame index
            textboxPause.tStart = t  # local t and not account for scr refresh
            textboxPause.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textboxPause, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textboxPause.started')
            textboxPause.setAutoDraw(True)
        
        # *keyPause* updates
        waitOnFlip = False
        if keyPause.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyPause.frameNStart = frameN  # exact frame index
            keyPause.tStart = t  # local t and not account for scr refresh
            keyPause.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyPause, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyPause.started')
            keyPause.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyPause.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyPause.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyPause.status == STARTED and not waitOnFlip:
            theseKeys = keyPause.getKeys(keyList=['space'], waitRelease=False)
            _keyPause_allKeys.extend(theseKeys)
            if len(_keyPause_allKeys):
                keyPause.keys = _keyPause_allKeys[-1].name  # just the last key pressed
                keyPause.rt = _keyPause_allKeys[-1].rt
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
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pause" ---
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyPause.keys in ['', [], None]:  # No response was made
        keyPause.keys = None
    trialsREPSWITCH.addData('keyPause.keys',keyPause.keys)
    if keyPause.keys != None:  # we had a response
        trialsREPSWITCH.addData('keyPause.rt', keyPause.rt)
    # the Routine "pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsREPSWITCH'


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

# --- Prepare to start Routine "Goodbye" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textboxGoodbye.reset()
# keep track of which components have finished
GoodbyeComponents = [textboxGoodbye]
for thisComponent in GoodbyeComponents:
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

# --- Run Routine "Goodbye" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textboxGoodbye* updates
    if textboxGoodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textboxGoodbye.frameNStart = frameN  # exact frame index
        textboxGoodbye.tStart = t  # local t and not account for scr refresh
        textboxGoodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textboxGoodbye, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textboxGoodbye.started')
        textboxGoodbye.setAutoDraw(True)
    if textboxGoodbye.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textboxGoodbye.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            textboxGoodbye.tStop = t  # not accounting for scr refresh
            textboxGoodbye.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textboxGoodbye.stopped')
            textboxGoodbye.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Goodbye" ---
for thisComponent in GoodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)


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
