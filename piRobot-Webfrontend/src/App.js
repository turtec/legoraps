import React from 'react';
import ButtonLeft from './uicomponents/ButtonLeft'
import ButtonRight from './uicomponents/ButtonRight'
import ButtonForward from './uicomponents/ButtonForward'
import {moveRight, moveLeft, moveForward} from './api'

import './App.css';

function triggerLeft(){
  console.log('triggerLeft')
  moveLeft()
}

function triggerRight(){
  console.log('triggerRight')
  moveRight()
}

function triggerForward(){
  console.log('triggerForward')
  moveForward()
}


function App() {
  return (
    <div className="App">
      <ButtonLeft onclick={triggerLeft}/>
      <ButtonRight onclick={triggerRight}/>
      <ButtonForward onclick={triggerForward}/>
    </div>
  );
}

export default App;
