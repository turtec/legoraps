import React from 'react';

function ButtonForward(props) {
  return (
    <div >
     <p onClick={props.onclick}>
       forward
      </p>
    </div>
  );
}

export default ButtonForward;