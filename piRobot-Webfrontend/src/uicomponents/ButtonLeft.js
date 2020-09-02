import React from 'react';

function ButtonLeft(props) {
  return (
    <div >
     <p onClick={props.onclick}>
       left
      </p>
    </div>
  );
}

export default ButtonLeft;