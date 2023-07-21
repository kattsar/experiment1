/************************************* 
 * Repswitch1_Practice_Version2 Test *
 *************************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'REPSWITCH1_Practice_version2';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from codeSavePractice
count = 0;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(General_Instr_1RoutineBegin());
flowScheduler.add(General_Instr_1RoutineEachFrame());
flowScheduler.add(General_Instr_1RoutineEnd());
flowScheduler.add(General_Instr_2RoutineBegin());
flowScheduler.add(General_Instr_2RoutineEachFrame());
flowScheduler.add(General_Instr_2RoutineEnd());
flowScheduler.add(General_Instr_3RoutineBegin());
flowScheduler.add(General_Instr_3RoutineEachFrame());
flowScheduler.add(General_Instr_3RoutineEnd());
flowScheduler.add(InstructionsPracticeRoutineBegin());
flowScheduler.add(InstructionsPracticeRoutineEachFrame());
flowScheduler.add(InstructionsPracticeRoutineEnd());
flowScheduler.add(blank500RoutineBegin());
flowScheduler.add(blank500RoutineEachFrame());
flowScheduler.add(blank500RoutineEnd());
const trialsPracticeLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsPracticeLoopBegin(trialsPracticeLoopScheduler));
flowScheduler.add(trialsPracticeLoopScheduler);
flowScheduler.add(trialsPracticeLoopEnd);
flowScheduler.add(blank500RoutineBegin());
flowScheduler.add(blank500RoutineEachFrame());
flowScheduler.add(blank500RoutineEnd());
flowScheduler.add(EndPracticeRoutineBegin());
flowScheduler.add(EndPracticeRoutineEachFrame());
flowScheduler.add(EndPracticeRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'REPSWITCH1_Practice/PICTURE_614.png', 'path': 'REPSWITCH1_Practice/PICTURE_614.png'},
    {'name': 'REPSWITCH1_Practice/PICTURE_612.png', 'path': 'REPSWITCH1_Practice/PICTURE_612.png'},
    {'name': 'REPSWITCH1_Practice/PICTURE_570.png', 'path': 'REPSWITCH1_Practice/PICTURE_570.png'},
    {'name': 'repswitch_practice_version2.xlsx', 'path': 'repswitch_practice_version2.xlsx'},
    {'name': 'REPSWITCH1_Practice/PICTURE_733.png', 'path': 'REPSWITCH1_Practice/PICTURE_733.png'},
    {'name': 'REPSWITCH1_Practice/PICTURE_110.png', 'path': 'REPSWITCH1_Practice/PICTURE_110.png'},
    {'name': 'REPSWITCH1_Practice/PICTURE_599.png', 'path': 'REPSWITCH1_Practice/PICTURE_599.png'},
    {'name': 'REPSWITCH1_Practice/PICTURE_12.png', 'path': 'REPSWITCH1_Practice/PICTURE_12.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var General_Instr_1Clock;
var textboxInstr1;
var textboxInstr1_2;
var textboxInstr1_3;
var textboxInstr1_4;
var textboxInstr1_5;
var textboxInstr1_6;
var textboxInstr1_7;
var textboxInstr1_8;
var textboxInstr1_9;
var textboxInstr1_10;
var keyInstr1;
var General_Instr_2Clock;
var textboxInstr2;
var keyInstr2;
var General_Instr_3Clock;
var textboxInstr3;
var keyInstr3;
var InstructionsPracticeClock;
var textboxInstrPractice;
var textboxInstrPractice_2;
var textboxInstrPractice_3;
var textboxInstrPractice_4;
var textboxInstrPractice_5;
var textboxInstrPractice_6;
var textboxInstrPractice_7;
var textboxInstrPractice_8;
var textboxInstrPractice_9;
var textboxInstrPractice_10;
var textboxInstrPractice_11;
var textboxInstrPractice_12;
var textboxInstrPractice_13;
var textboxInstrPractice_14;
var textboxInstrPractice_15;
var textboxInstrPractice_16;
var textboxInstrPractice_17;
var keyInstrPractice;
var blank500Clock;
var textBlank500;
var ITIClock;
var fixationITI;
var practiceTrialClock;
var polygonCol;
var polygonWh;
var textCue;
var imagePractice;
var polygonText;
var textPractice;
var keyPractice;
var micPractice;
var EndPracticeClock;
var textboxEndPracrice;
var keyEndPractice;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "General_Instr_1"
  General_Instr_1Clock = new util.Clock();
  textboxInstr1 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstr1',
    text: 'En este experimento verás imágenes en la pantalla y tendrás que nombrarlas. \n\nTendrás que nombrar cada imagen diciendo su nombre en voz alta o escribiéndolo. \n\nUn rectángulo de color alrededor de cada imagen te indicará si tienes que decirla en voz alta o teclearla. ',
    font: 'Open Sans',
    pos: [0, 0.25], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  textboxInstr1_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstr1_2',
    text: 'Si el rectángulo es',
    font: 'Open Sans',
    pos: [0, 0.03], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  textboxInstr1_3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstr1_3',
    text: 'amarillo,',
    font: 'Open Sans',
    pos: [0.255, 0.03], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: [1.0, 0.6863, (- 1.0)], colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  textboxInstr1_4 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstr1_4',
    text: ' tendrás que  ',
    font: 'Open Sans',
    pos: [0.39, 0.03], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  textboxInstr1_5 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstr1_5',
    text: 'escribirlo con el teclado.',
    font: 'Open Sans',
    pos: [0.57, 0.03], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  textboxInstr1_6 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstr1_6',
    text: 'Si el rectángulo es ',
    font: 'Open Sans',
    pos: [0, (- 0.03)], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -5.0 
  });
  
  textboxInstr1_7 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstr1_7',
    text: 'azul,',
    font: 'Open Sans',
    pos: [0.255, (- 0.03)], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: [(- 1.0), (- 1.0), 0.0902], colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -6.0 
  });
  
  textboxInstr1_8 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstr1_8',
    text: ' tendrás que ',
    font: 'Open Sans',
    pos: [0.33, (- 0.03)], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -7.0 
  });
  
  textboxInstr1_9 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstr1_9',
    text: 'decirlo en voz alta. ',
    font: 'Open Sans',
    pos: [0.51, (- 0.03)], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -8.0 
  });
  
  textboxInstr1_10 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstr1_10',
    text: 'Deberás nombrar las imágenes lo más rápido y con la mayor precisión posible. \n\nLas imágenes solo permanecerán en la pantalla durante unos instantes. \n\n\nPulsa la BARRA ESPACIADORA para continuar.\n',
    font: 'Open Sans',
    pos: [0, (- 0.27)], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -9.0 
  });
  
  keyInstr1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "General_Instr_2"
  General_Instr_2Clock = new util.Clock();
  textboxInstr2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstr2',
    text: 'Algunas instrucciones más.\n\nCuando hables, asegúrate de decir una sola palabra, con voz clara.\n\nIntenta mantener las manos sobre el teclado durante toda la sesión.\n\nY, por favor, ¡no hables mientras escribes!\n\n\nPulsa la BARRA ESPACIADORA para continuar.\n',
    font: 'Open Sans',
    pos: [0, 0], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  keyInstr2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "General_Instr_3"
  General_Instr_3Clock = new util.Clock();
  textboxInstr3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstr3',
    text: 'Practiquemos antes de empezar.\n\nPulsa la BARRA ESPACIADORA para continuar.\n',
    font: 'Open Sans',
    pos: [0, 0], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  keyInstr3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "InstructionsPractice"
  InstructionsPracticeClock = new util.Clock();
  textboxInstrPractice = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice',
    text: 'Si el rectángulo es',
    font: 'Open Sans',
    pos: [0, 0.2], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  textboxInstrPractice_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice_2',
    text: 'amarillo,',
    font: 'Open Sans',
    pos: [0.255, 0.2], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: [1.0, 0.6863, (- 1.0)], colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  textboxInstrPractice_3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice_3',
    text: ' deberás ',
    font: 'Open Sans',
    pos: [0.39, 0.2], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  textboxInstrPractice_4 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice_4',
    text: 'teclear',
    font: 'Open Sans',
    pos: [0.52, 0.2], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  textboxInstrPractice_5 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice_5',
    text: 'el nombre de la imagen. ',
    font: 'Open Sans',
    pos: [0.635, 0.2], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  textboxInstrPractice_6 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice_6',
    text: 'La palabra',
    font: 'Open Sans',
    pos: [0, 0.15], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -5.0 
  });
  
  textboxInstrPractice_7 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice_7',
    text: 'HABLA',
    font: 'Open Sans',
    pos: [0.155, 0.15], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -6.0 
  });
  
  textboxInstrPractice_8 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice_8',
    text: 'aparecerá encima de la imagen.',
    font: 'Open Sans',
    pos: [0.265, 0.15], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -7.0 
  });
  
  textboxInstrPractice_9 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice_9',
    text: 'Si el rectángulo es ',
    font: 'Open Sans',
    pos: [0, 0.05], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -8.0 
  });
  
  textboxInstrPractice_10 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice_10',
    text: 'azul,',
    font: 'Open Sans',
    pos: [0.255, 0.05], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: [(- 1.0), (- 1.0), 0.0902], colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -9.0 
  });
  
  textboxInstrPractice_11 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice_11',
    text: ' tendrás que ',
    font: 'Open Sans',
    pos: [0.33, 0.05], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -10.0 
  });
  
  textboxInstrPractice_12 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice_12',
    text: 'decir en voz alta ',
    font: 'Open Sans',
    pos: [0.51, 0.05], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -11.0 
  });
  
  textboxInstrPractice_13 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice_13',
    text: 'el nombre de la imagen. ',
    font: 'Open Sans',
    pos: [0.76, 0.05], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -12.0 
  });
  
  textboxInstrPractice_14 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice_14',
    text: 'La palabra',
    font: 'Open Sans',
    pos: [0, 0], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -13.0 
  });
  
  textboxInstrPractice_15 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice_15',
    text: 'TECLEA',
    font: 'Open Sans',
    pos: [0.15, 0], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -14.0 
  });
  
  textboxInstrPractice_16 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice_16',
    text: 'aparecerá encima de la imagen. ',
    font: 'Open Sans',
    pos: [0.265, 0], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -15.0 
  });
  
  textboxInstrPractice_17 = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxInstrPractice_17',
    text: 'Pulsa la BARRA ESPACIADORA para empezar.',
    font: 'Open Sans',
    pos: [0, (- 0.1)], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -16.0 
  });
  
  keyInstrPractice = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "blank500"
  blank500Clock = new util.Clock();
  textBlank500 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank500',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ITI"
  ITIClock = new util.Clock();
  fixationITI = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixationITI', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "practiceTrial"
  practiceTrialClock = new util.Clock();
  polygonCol = new visual.Rect ({
    win: psychoJS.window, name: 'polygonCol', 
    width: [0.55, 0.55][0], height: [0.55, 0.55][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  polygonWh = new visual.Rect ({
    win: psychoJS.window, name: 'polygonWh', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  textCue = new visual.TextStim({
    win: psychoJS.window,
    name: 'textCue',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.35], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  imagePractice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imagePractice', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  polygonText = new visual.Rect ({
    win: psychoJS.window, name: 'polygonText', 
    width: [0.2, 0.1][0], height: [0.2, 0.1][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([0.9216, 0.9216, 0.9216]),
    fillColor: new util.Color([0.9216, 0.9216, 0.9216]),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  textPractice = new visual.TextStim({
    win: psychoJS.window,
    name: 'textPractice',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -5.0 
  });
  
  keyPractice = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  micPractice = new sound.Microphone({
    win : psychoJS.window, 
    name:'micPractice',
    sampleRateHz : 48000,
    channels : 'auto',
    maxRecordingSize : 24000.0,
    loopback : true,
    policyWhenFull : 'ignore',
  });
  // Initialize components for Routine "EndPractice"
  EndPracticeClock = new util.Clock();
  textboxEndPracrice = new visual.TextBox({
    win: psychoJS.window,
    name: 'textboxEndPracrice',
    text: '¡Genial! \n\n\nPulsa la BARRA ESPACIADORA para continuar.',
    font: 'Open Sans',
    pos: [0, 0], letterHeight: 0.03,
    size: [null, null],  units: undefined, 
    color: [1.0, 1.0, 1.0], colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  keyEndPractice = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _keyInstr1_allKeys;
var General_Instr_1Components;
function General_Instr_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'General_Instr_1' ---
    t = 0;
    General_Instr_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    keyInstr1.keys = undefined;
    keyInstr1.rt = undefined;
    _keyInstr1_allKeys = [];
    // keep track of which components have finished
    General_Instr_1Components = [];
    General_Instr_1Components.push(textboxInstr1);
    General_Instr_1Components.push(textboxInstr1_2);
    General_Instr_1Components.push(textboxInstr1_3);
    General_Instr_1Components.push(textboxInstr1_4);
    General_Instr_1Components.push(textboxInstr1_5);
    General_Instr_1Components.push(textboxInstr1_6);
    General_Instr_1Components.push(textboxInstr1_7);
    General_Instr_1Components.push(textboxInstr1_8);
    General_Instr_1Components.push(textboxInstr1_9);
    General_Instr_1Components.push(textboxInstr1_10);
    General_Instr_1Components.push(keyInstr1);
    
    for (const thisComponent of General_Instr_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function General_Instr_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'General_Instr_1' ---
    // get current time
    t = General_Instr_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textboxInstr1* updates
    if (t >= 0.0 && textboxInstr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstr1.tStart = t;  // (not accounting for frame time here)
      textboxInstr1.frameNStart = frameN;  // exact frame index
      
      textboxInstr1.setAutoDraw(true);
    }

    
    // *textboxInstr1_2* updates
    if (t >= 0.0 && textboxInstr1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstr1_2.tStart = t;  // (not accounting for frame time here)
      textboxInstr1_2.frameNStart = frameN;  // exact frame index
      
      textboxInstr1_2.setAutoDraw(true);
    }

    
    // *textboxInstr1_3* updates
    if (t >= 0.0 && textboxInstr1_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstr1_3.tStart = t;  // (not accounting for frame time here)
      textboxInstr1_3.frameNStart = frameN;  // exact frame index
      
      textboxInstr1_3.setAutoDraw(true);
    }

    
    // *textboxInstr1_4* updates
    if (t >= 0.0 && textboxInstr1_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstr1_4.tStart = t;  // (not accounting for frame time here)
      textboxInstr1_4.frameNStart = frameN;  // exact frame index
      
      textboxInstr1_4.setAutoDraw(true);
    }

    
    // *textboxInstr1_5* updates
    if (t >= 0.0 && textboxInstr1_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstr1_5.tStart = t;  // (not accounting for frame time here)
      textboxInstr1_5.frameNStart = frameN;  // exact frame index
      
      textboxInstr1_5.setAutoDraw(true);
    }

    
    // *textboxInstr1_6* updates
    if (t >= 0.0 && textboxInstr1_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstr1_6.tStart = t;  // (not accounting for frame time here)
      textboxInstr1_6.frameNStart = frameN;  // exact frame index
      
      textboxInstr1_6.setAutoDraw(true);
    }

    
    // *textboxInstr1_7* updates
    if (t >= 0.0 && textboxInstr1_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstr1_7.tStart = t;  // (not accounting for frame time here)
      textboxInstr1_7.frameNStart = frameN;  // exact frame index
      
      textboxInstr1_7.setAutoDraw(true);
    }

    
    // *textboxInstr1_8* updates
    if (t >= 0.0 && textboxInstr1_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstr1_8.tStart = t;  // (not accounting for frame time here)
      textboxInstr1_8.frameNStart = frameN;  // exact frame index
      
      textboxInstr1_8.setAutoDraw(true);
    }

    
    // *textboxInstr1_9* updates
    if (t >= 0.0 && textboxInstr1_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstr1_9.tStart = t;  // (not accounting for frame time here)
      textboxInstr1_9.frameNStart = frameN;  // exact frame index
      
      textboxInstr1_9.setAutoDraw(true);
    }

    
    // *textboxInstr1_10* updates
    if (t >= 0.0 && textboxInstr1_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstr1_10.tStart = t;  // (not accounting for frame time here)
      textboxInstr1_10.frameNStart = frameN;  // exact frame index
      
      textboxInstr1_10.setAutoDraw(true);
    }

    
    // *keyInstr1* updates
    if (t >= 0.0 && keyInstr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyInstr1.tStart = t;  // (not accounting for frame time here)
      keyInstr1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyInstr1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyInstr1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyInstr1.clearEvents(); });
    }

    if (keyInstr1.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyInstr1.getKeys({keyList: ['space'], waitRelease: false});
      _keyInstr1_allKeys = _keyInstr1_allKeys.concat(theseKeys);
      if (_keyInstr1_allKeys.length > 0) {
        keyInstr1.keys = _keyInstr1_allKeys[_keyInstr1_allKeys.length - 1].name;  // just the last key pressed
        keyInstr1.rt = _keyInstr1_allKeys[_keyInstr1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of General_Instr_1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function General_Instr_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'General_Instr_1' ---
    for (const thisComponent of General_Instr_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(keyInstr1.corr, level);
    }
    psychoJS.experiment.addData('keyInstr1.keys', keyInstr1.keys);
    if (typeof keyInstr1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyInstr1.rt', keyInstr1.rt);
        routineTimer.reset();
        }
    
    keyInstr1.stop();
    // the Routine "General_Instr_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _keyInstr2_allKeys;
var General_Instr_2Components;
function General_Instr_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'General_Instr_2' ---
    t = 0;
    General_Instr_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    keyInstr2.keys = undefined;
    keyInstr2.rt = undefined;
    _keyInstr2_allKeys = [];
    // keep track of which components have finished
    General_Instr_2Components = [];
    General_Instr_2Components.push(textboxInstr2);
    General_Instr_2Components.push(keyInstr2);
    
    for (const thisComponent of General_Instr_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function General_Instr_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'General_Instr_2' ---
    // get current time
    t = General_Instr_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textboxInstr2* updates
    if (t >= 0.0 && textboxInstr2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstr2.tStart = t;  // (not accounting for frame time here)
      textboxInstr2.frameNStart = frameN;  // exact frame index
      
      textboxInstr2.setAutoDraw(true);
    }

    
    // *keyInstr2* updates
    if (t >= 0.0 && keyInstr2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyInstr2.tStart = t;  // (not accounting for frame time here)
      keyInstr2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyInstr2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyInstr2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyInstr2.clearEvents(); });
    }

    if (keyInstr2.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyInstr2.getKeys({keyList: ['space'], waitRelease: false});
      _keyInstr2_allKeys = _keyInstr2_allKeys.concat(theseKeys);
      if (_keyInstr2_allKeys.length > 0) {
        keyInstr2.keys = _keyInstr2_allKeys[_keyInstr2_allKeys.length - 1].name;  // just the last key pressed
        keyInstr2.rt = _keyInstr2_allKeys[_keyInstr2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of General_Instr_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function General_Instr_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'General_Instr_2' ---
    for (const thisComponent of General_Instr_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(keyInstr2.corr, level);
    }
    psychoJS.experiment.addData('keyInstr2.keys', keyInstr2.keys);
    if (typeof keyInstr2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyInstr2.rt', keyInstr2.rt);
        routineTimer.reset();
        }
    
    keyInstr2.stop();
    // the Routine "General_Instr_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _keyInstr3_allKeys;
var General_Instr_3Components;
function General_Instr_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'General_Instr_3' ---
    t = 0;
    General_Instr_3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    keyInstr3.keys = undefined;
    keyInstr3.rt = undefined;
    _keyInstr3_allKeys = [];
    // keep track of which components have finished
    General_Instr_3Components = [];
    General_Instr_3Components.push(textboxInstr3);
    General_Instr_3Components.push(keyInstr3);
    
    for (const thisComponent of General_Instr_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function General_Instr_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'General_Instr_3' ---
    // get current time
    t = General_Instr_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textboxInstr3* updates
    if (t >= 0.0 && textboxInstr3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstr3.tStart = t;  // (not accounting for frame time here)
      textboxInstr3.frameNStart = frameN;  // exact frame index
      
      textboxInstr3.setAutoDraw(true);
    }

    
    // *keyInstr3* updates
    if (t >= 0.0 && keyInstr3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyInstr3.tStart = t;  // (not accounting for frame time here)
      keyInstr3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyInstr3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyInstr3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyInstr3.clearEvents(); });
    }

    if (keyInstr3.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyInstr3.getKeys({keyList: ['space'], waitRelease: false});
      _keyInstr3_allKeys = _keyInstr3_allKeys.concat(theseKeys);
      if (_keyInstr3_allKeys.length > 0) {
        keyInstr3.keys = _keyInstr3_allKeys[_keyInstr3_allKeys.length - 1].name;  // just the last key pressed
        keyInstr3.rt = _keyInstr3_allKeys[_keyInstr3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of General_Instr_3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function General_Instr_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'General_Instr_3' ---
    for (const thisComponent of General_Instr_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(keyInstr3.corr, level);
    }
    psychoJS.experiment.addData('keyInstr3.keys', keyInstr3.keys);
    if (typeof keyInstr3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyInstr3.rt', keyInstr3.rt);
        routineTimer.reset();
        }
    
    keyInstr3.stop();
    // the Routine "General_Instr_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _keyInstrPractice_allKeys;
var InstructionsPracticeComponents;
function InstructionsPracticeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'InstructionsPractice' ---
    t = 0;
    InstructionsPracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    keyInstrPractice.keys = undefined;
    keyInstrPractice.rt = undefined;
    _keyInstrPractice_allKeys = [];
    // keep track of which components have finished
    InstructionsPracticeComponents = [];
    InstructionsPracticeComponents.push(textboxInstrPractice);
    InstructionsPracticeComponents.push(textboxInstrPractice_2);
    InstructionsPracticeComponents.push(textboxInstrPractice_3);
    InstructionsPracticeComponents.push(textboxInstrPractice_4);
    InstructionsPracticeComponents.push(textboxInstrPractice_5);
    InstructionsPracticeComponents.push(textboxInstrPractice_6);
    InstructionsPracticeComponents.push(textboxInstrPractice_7);
    InstructionsPracticeComponents.push(textboxInstrPractice_8);
    InstructionsPracticeComponents.push(textboxInstrPractice_9);
    InstructionsPracticeComponents.push(textboxInstrPractice_10);
    InstructionsPracticeComponents.push(textboxInstrPractice_11);
    InstructionsPracticeComponents.push(textboxInstrPractice_12);
    InstructionsPracticeComponents.push(textboxInstrPractice_13);
    InstructionsPracticeComponents.push(textboxInstrPractice_14);
    InstructionsPracticeComponents.push(textboxInstrPractice_15);
    InstructionsPracticeComponents.push(textboxInstrPractice_16);
    InstructionsPracticeComponents.push(textboxInstrPractice_17);
    InstructionsPracticeComponents.push(keyInstrPractice);
    
    for (const thisComponent of InstructionsPracticeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructionsPracticeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'InstructionsPractice' ---
    // get current time
    t = InstructionsPracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textboxInstrPractice* updates
    if (t >= 0.0 && textboxInstrPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice.setAutoDraw(true);
    }

    
    // *textboxInstrPractice_2* updates
    if (t >= 0.0 && textboxInstrPractice_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice_2.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice_2.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice_2.setAutoDraw(true);
    }

    
    // *textboxInstrPractice_3* updates
    if (t >= 0.0 && textboxInstrPractice_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice_3.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice_3.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice_3.setAutoDraw(true);
    }

    
    // *textboxInstrPractice_4* updates
    if (t >= 0.0 && textboxInstrPractice_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice_4.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice_4.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice_4.setAutoDraw(true);
    }

    
    // *textboxInstrPractice_5* updates
    if (t >= 0.0 && textboxInstrPractice_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice_5.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice_5.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice_5.setAutoDraw(true);
    }

    
    // *textboxInstrPractice_6* updates
    if (t >= 0.0 && textboxInstrPractice_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice_6.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice_6.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice_6.setAutoDraw(true);
    }

    
    // *textboxInstrPractice_7* updates
    if (t >= 0.0 && textboxInstrPractice_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice_7.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice_7.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice_7.setAutoDraw(true);
    }

    
    // *textboxInstrPractice_8* updates
    if (t >= 0.0 && textboxInstrPractice_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice_8.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice_8.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice_8.setAutoDraw(true);
    }

    
    // *textboxInstrPractice_9* updates
    if (t >= 0.0 && textboxInstrPractice_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice_9.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice_9.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice_9.setAutoDraw(true);
    }

    
    // *textboxInstrPractice_10* updates
    if (t >= 0.0 && textboxInstrPractice_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice_10.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice_10.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice_10.setAutoDraw(true);
    }

    
    // *textboxInstrPractice_11* updates
    if (t >= 0.0 && textboxInstrPractice_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice_11.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice_11.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice_11.setAutoDraw(true);
    }

    
    // *textboxInstrPractice_12* updates
    if (t >= 0.0 && textboxInstrPractice_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice_12.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice_12.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice_12.setAutoDraw(true);
    }

    
    // *textboxInstrPractice_13* updates
    if (t >= 0.0 && textboxInstrPractice_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice_13.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice_13.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice_13.setAutoDraw(true);
    }

    
    // *textboxInstrPractice_14* updates
    if (t >= 0.0 && textboxInstrPractice_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice_14.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice_14.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice_14.setAutoDraw(true);
    }

    
    // *textboxInstrPractice_15* updates
    if (t >= 0.0 && textboxInstrPractice_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice_15.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice_15.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice_15.setAutoDraw(true);
    }

    
    // *textboxInstrPractice_16* updates
    if (t >= 0.0 && textboxInstrPractice_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice_16.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice_16.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice_16.setAutoDraw(true);
    }

    
    // *textboxInstrPractice_17* updates
    if (t >= 0.0 && textboxInstrPractice_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxInstrPractice_17.tStart = t;  // (not accounting for frame time here)
      textboxInstrPractice_17.frameNStart = frameN;  // exact frame index
      
      textboxInstrPractice_17.setAutoDraw(true);
    }

    
    // *keyInstrPractice* updates
    if (t >= 0.0 && keyInstrPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyInstrPractice.tStart = t;  // (not accounting for frame time here)
      keyInstrPractice.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyInstrPractice.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyInstrPractice.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyInstrPractice.clearEvents(); });
    }

    if (keyInstrPractice.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyInstrPractice.getKeys({keyList: ['space'], waitRelease: false});
      _keyInstrPractice_allKeys = _keyInstrPractice_allKeys.concat(theseKeys);
      if (_keyInstrPractice_allKeys.length > 0) {
        keyInstrPractice.keys = _keyInstrPractice_allKeys[_keyInstrPractice_allKeys.length - 1].name;  // just the last key pressed
        keyInstrPractice.rt = _keyInstrPractice_allKeys[_keyInstrPractice_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionsPracticeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsPracticeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'InstructionsPractice' ---
    for (const thisComponent of InstructionsPracticeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(keyInstrPractice.corr, level);
    }
    psychoJS.experiment.addData('keyInstrPractice.keys', keyInstrPractice.keys);
    if (typeof keyInstrPractice.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyInstrPractice.rt', keyInstrPractice.rt);
        routineTimer.reset();
        }
    
    keyInstrPractice.stop();
    // the Routine "InstructionsPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var blank500Components;
function blank500RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'blank500' ---
    t = 0;
    blank500Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    blank500Components = [];
    blank500Components.push(textBlank500);
    
    for (const thisComponent of blank500Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function blank500RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blank500' ---
    // get current time
    t = blank500Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textBlank500* updates
    if (t >= 0.0 && textBlank500.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textBlank500.tStart = t;  // (not accounting for frame time here)
      textBlank500.frameNStart = frameN;  // exact frame index
      
      textBlank500.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textBlank500.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textBlank500.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blank500Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blank500RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blank500' ---
    for (const thisComponent of blank500Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trialsPractice;
function trialsPracticeLoopBegin(trialsPracticeLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialsPractice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'repswitch_practice_version2.xlsx',
      seed: undefined, name: 'trialsPractice'
    });
    psychoJS.experiment.addLoop(trialsPractice); // add the loop to the experiment
    currentLoop = trialsPractice;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrialsPractice of trialsPractice) {
      snapshot = trialsPractice.getSnapshot();
      trialsPracticeLoopScheduler.add(importConditions(snapshot));
      trialsPracticeLoopScheduler.add(ITIRoutineBegin(snapshot));
      trialsPracticeLoopScheduler.add(ITIRoutineEachFrame());
      trialsPracticeLoopScheduler.add(ITIRoutineEnd(snapshot));
      trialsPracticeLoopScheduler.add(practiceTrialRoutineBegin(snapshot));
      trialsPracticeLoopScheduler.add(practiceTrialRoutineEachFrame());
      trialsPracticeLoopScheduler.add(practiceTrialRoutineEnd(snapshot));
      trialsPracticeLoopScheduler.add(blank500RoutineBegin(snapshot));
      trialsPracticeLoopScheduler.add(blank500RoutineEachFrame());
      trialsPracticeLoopScheduler.add(blank500RoutineEnd(snapshot));
      trialsPracticeLoopScheduler.add(trialsPracticeLoopEndIteration(trialsPracticeLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsPracticeLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trialsPractice);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsPracticeLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var ITIComponents;
function ITIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ITI' ---
    t = 0;
    ITIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    ITIComponents = [];
    ITIComponents.push(fixationITI);
    
    for (const thisComponent of ITIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ITIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ITI' ---
    // get current time
    t = ITIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixationITI* updates
    if (t >= 0.0 && fixationITI.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationITI.tStart = t;  // (not accounting for frame time here)
      fixationITI.frameNStart = frameN;  // exact frame index
      
      fixationITI.setAutoDraw(true);
    }

    frameRemains = 0.0 + (Math.random() + 1) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixationITI.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixationITI.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ITIComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ITIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ITI' ---
    for (const thisComponent of ITIComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _keyPractice_allKeys;
var practiceTrialComponents;
function practiceTrialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practiceTrial' ---
    t = 0;
    practiceTrialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    polygonCol.setFillColor(new util.Color(frameColor));
    polygonCol.setLineColor(new util.Color(frameColor));
    textCue.setColor(new util.Color(frameColor));
    imagePractice.setImage(image);
    keyPractice.keys = undefined;
    keyPractice.rt = undefined;
    _keyPractice_allKeys = [];
    // keep track of which components have finished
    practiceTrialComponents = [];
    practiceTrialComponents.push(polygonCol);
    practiceTrialComponents.push(polygonWh);
    practiceTrialComponents.push(textCue);
    practiceTrialComponents.push(imagePractice);
    practiceTrialComponents.push(polygonText);
    practiceTrialComponents.push(textPractice);
    practiceTrialComponents.push(keyPractice);
    practiceTrialComponents.push(micPractice);
    
    for (const thisComponent of practiceTrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practiceTrialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practiceTrial' ---
    // get current time
    t = practiceTrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygonCol* updates
    if (t >= 0.0 && polygonCol.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygonCol.tStart = t;  // (not accounting for frame time here)
      polygonCol.frameNStart = frameN;  // exact frame index
      
      polygonCol.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (polygonCol.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygonCol.setAutoDraw(false);
    }
    
    // *polygonWh* updates
    if (t >= 0.0 && polygonWh.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygonWh.tStart = t;  // (not accounting for frame time here)
      polygonWh.frameNStart = frameN;  // exact frame index
      
      polygonWh.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (polygonWh.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygonWh.setAutoDraw(false);
    }
    
    // *textCue* updates
    if (t >= 0.0 && textCue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textCue.tStart = t;  // (not accounting for frame time here)
      textCue.frameNStart = frameN;  // exact frame index
      
      textCue.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textCue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textCue.setAutoDraw(false);
    }
    
    if (textCue.status === PsychoJS.Status.STARTED){ // only update if being drawn
      textCue.setText(respModal, false);
    }
    
    // *imagePractice* updates
    if (t >= 0.0 && imagePractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imagePractice.tStart = t;  // (not accounting for frame time here)
      imagePractice.frameNStart = frameN;  // exact frame index
      
      imagePractice.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imagePractice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imagePractice.setAutoDraw(false);
    }
    
    // *polygonText* updates
    if (t >= 0.0 && polygonText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygonText.tStart = t;  // (not accounting for frame time here)
      polygonText.frameNStart = frameN;  // exact frame index
      
      polygonText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (polygonText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygonText.setAutoDraw(false);
    }
    
    // *textPractice* updates
    if (t >= 0.0 && textPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textPractice.tStart = t;  // (not accounting for frame time here)
      textPractice.frameNStart = frameN;  // exact frame index
      
      textPractice.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textPractice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textPractice.setAutoDraw(false);
    }
    
    if (textPractice.status === PsychoJS.Status.STARTED){ // only update if being drawn
      textPractice.setText(respDisplay, false);
    }
    
    // *keyPractice* updates
    if (t >= 0.0 && keyPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyPractice.tStart = t;  // (not accounting for frame time here)
      keyPractice.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyPractice.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyPractice.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyPractice.clearEvents(); });
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (keyPractice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      keyPractice.status = PsychoJS.Status.FINISHED;
  }

    if (keyPractice.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyPractice.getKeys({keyList: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'backspace'], waitRelease: false});
      _keyPractice_allKeys = _keyPractice_allKeys.concat(theseKeys);
      if (_keyPractice_allKeys.length > 0) {
        keyPractice.keys = _keyPractice_allKeys.map((key) => key.name);  // storing all keys
        keyPractice.rt = _keyPractice_allKeys.map((key) => key.rt);
        // was this correct?
        if (keyPractice.keys == correctAns) {
            keyPractice.corr = 1;
        } else {
            keyPractice.corr = 0;
        }
      }
    }
    
    if (t >= 0.0 && micPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      micPractice.tStart = t;  // (not accounting for frame time here)
      micPractice.frameNStart = frameN;  // exact frame index
      
      await micPractice.start();
    }
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (micPractice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      micPractice.pause();
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practiceTrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var thisFilename;
function practiceTrialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practiceTrial' ---
    for (const thisComponent of practiceTrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (keyPractice.keys === undefined) {
      if (['None','none',undefined].includes(correctAns)) {
         keyPractice.corr = 1;  // correct non-response
      } else {
         keyPractice.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(keyPractice.corr, level);
    }
    psychoJS.experiment.addData('keyPractice.keys', keyPractice.keys);
    psychoJS.experiment.addData('keyPractice.corr', keyPractice.corr);
    if (typeof keyPractice.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyPractice.rt', keyPractice.rt);
        }
    
    keyPractice.stop();
    // stop the microphone (make the audio data ready for upload)
    await micPractice.stop();
    // construct a filename for this recording
    thisFilename = 'recording_micPractice_' + currentLoop.name + '_' + currentLoop.thisN
    // get the recording
    micPractice.lastClip = await micPractice.getRecording({
      tag: thisFilename + '_' + util.MonotonicClock.getDateStr(),
      flush: false
    });
    psychoJS.experiment.addData('micPractice.clip', thisFilename);
    // start the asynchronous upload to the server
    micPractice.lastClip.upload();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _keyEndPractice_allKeys;
var EndPracticeComponents;
function EndPracticeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EndPractice' ---
    t = 0;
    EndPracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    keyEndPractice.keys = undefined;
    keyEndPractice.rt = undefined;
    _keyEndPractice_allKeys = [];
    // keep track of which components have finished
    EndPracticeComponents = [];
    EndPracticeComponents.push(textboxEndPracrice);
    EndPracticeComponents.push(keyEndPractice);
    
    for (const thisComponent of EndPracticeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndPracticeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EndPractice' ---
    // get current time
    t = EndPracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textboxEndPracrice* updates
    if (t >= 0.0 && textboxEndPracrice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textboxEndPracrice.tStart = t;  // (not accounting for frame time here)
      textboxEndPracrice.frameNStart = frameN;  // exact frame index
      
      textboxEndPracrice.setAutoDraw(true);
    }

    
    // *keyEndPractice* updates
    if (t >= 0.0 && keyEndPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyEndPractice.tStart = t;  // (not accounting for frame time here)
      keyEndPractice.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyEndPractice.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyEndPractice.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyEndPractice.clearEvents(); });
    }

    if (keyEndPractice.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyEndPractice.getKeys({keyList: ['space'], waitRelease: false});
      _keyEndPractice_allKeys = _keyEndPractice_allKeys.concat(theseKeys);
      if (_keyEndPractice_allKeys.length > 0) {
        keyEndPractice.keys = _keyEndPractice_allKeys[_keyEndPractice_allKeys.length - 1].name;  // just the last key pressed
        keyEndPractice.rt = _keyEndPractice_allKeys[_keyEndPractice_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndPracticeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndPracticeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EndPractice' ---
    for (const thisComponent of EndPracticeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(keyEndPractice.corr, level);
    }
    psychoJS.experiment.addData('keyEndPractice.keys', keyEndPractice.keys);
    if (typeof keyEndPractice.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyEndPractice.rt', keyEndPractice.rt);
        routineTimer.reset();
        }
    
    keyEndPractice.stop();
    // the Routine "EndPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
