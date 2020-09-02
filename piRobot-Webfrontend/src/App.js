import React from 'react';
import ButtonLeft from './uicomponents/ButtonLeft'
import ButtonRight from './uicomponents/ButtonRight'
import {moveRight, moveLeft} from './api'

import './App.css';

function triggerLeft(){
  console.log('triggerLeft')
  moveLeft()
}

function triggerRight(){
  console.log('triggerRight')
  moveRight()
}


function App() {
  return (
    <div className="App">
      <ButtonLeft onclick={triggerLeft}/>
      <ButtonRight onclick={triggerRight}/>
    </div>
  );
}

export default App;
