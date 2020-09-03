import React from 'react';
import ButtonLeft from './uicomponents/ButtonLeft'
import ButtonRight from './uicomponents/ButtonRight'
import ButtonForward from './uicomponents/ButtonForward'
import ButtonBackward from './uicomponents/ButtonBackward'
import ButtonStop from './uicomponents/ButtonStop'
import {moveRight, moveLeft, moveForward, moveBackward, moveStop} from './api'

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

function App() {
  return (
    <div className="App">
      <ButtonLeft onclick={triggerLeft}/>
      <ButtonRight onclick={triggerRight}/>
      <ButtonForward onclick={triggerForward}/>
      <ButtonBackward onclick={triggerBackward}/>
      <ButtonStop onclick={triggerStop}/>
    </div>
  );
}

export default App;
