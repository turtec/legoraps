import React from 'react';
import ButtonLeft from './uicomponents/ButtonLeft'
import ButtonRight from './uicomponents/ButtonRight'
import ButtonForward from './uicomponents/ButtonForward'
import ButtonBackward from './uicomponents/ButtonBackward'
import ButtonStop from './uicomponents/ButtonStop'
import ButtonDecreaseSpeed from './uicomponents/ButtonDecreaseSpeed'
import ButtonIncreaseSpeed from './uicomponents/ButtonIncreaseSpeed'
import {moveRight, moveLeft, moveForward, moveBackward, 
  moveStop, moveIncreaseSpeed, moveDecreaseSpeed} from './api'

import './App.css';

function triggerLeft(){
  moveLeft()
}

function triggerRight(){
  moveRight()
}

function triggerForward(){
  moveForward()
}

function triggerBackward(){
  moveBackward()
}

function triggerStop(){
  moveStop()
}

function triggerIncreaseSpeed(){
  moveIncreaseSpeed()
}

function triggerDecreaseSpeed(){
  moveDecreaseSpeed()
}

function App() {
  return (
    <div className="App">
      <ButtonLeft onclick={triggerLeft}/>
      <ButtonRight onclick={triggerRight}/>
      <ButtonForward onclick={triggerForward}/>
      <ButtonBackward onclick={triggerBackward}/>
      <ButtonStop onclick={triggerStop}/>
      <ButtonDecreaseSpeed onclick={triggerDecreaseSpeed}/>
      <ButtonIncreaseSpeed onclick={triggerIncreaseSpeed}/>
    </div>
  );
}

export default App;
