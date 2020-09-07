import React from 'react';

function ButtonIncreaseSpeed(props) {
  return (
    <div >
     <p onClick={props.onclick}>
       increase Speed
      </p>
    </div>
  );
}

export default ButtonIncreaseSpeed;