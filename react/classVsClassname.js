import React from 'react';
import ReactDOM from 'react-dom';

// Write code here:
// syntax in jsx is same as html only difference is class and className
const myDiv = (
    <div className="big">
        I AM A BIG DIV
    </div>
);

ReactDOM.render(myDiv, document.getElementById('app'));