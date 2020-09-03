import React from 'react';

function ButtonBackward(props) {
  return (
    <div >
     <p onClick={props.onclick}>
       backward
      </p>
    </div>
  );
}

export default ButtonBackward;