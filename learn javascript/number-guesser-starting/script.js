let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
const generateTarget = () => Math.floor(Math.random() * 10) ;
const compareGuesses = (uG, cG, tG) =>  Math.abs(tG - uG) <= Math.abs(tG - cG) ? true : false ;
const updateScore = s => {
  if (s === 'human'){
    humanScore++;
  }
  else{
    computerScore++;
  }
}
const advanceRound = () => currentRoundNumber++;