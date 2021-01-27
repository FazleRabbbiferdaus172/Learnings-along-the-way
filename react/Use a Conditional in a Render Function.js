import React from 'react';
import ReactDOM from 'react-dom';

const fiftyFifty = Math.random() < 0.5;

// New component class starts here:
class TonightsPlan extends React.Component {
    render() {
        let ele = "";
        if (fiftyFifty) {
            ele = "out WOOO";
        }
        else {
            ele = "to bed WOOO";
        }
        return <h1>Tonight I'm going {ele}</h1>;
    }
};

ReactDOM.render(<TonightsPlan />, document.getElementById('app'));