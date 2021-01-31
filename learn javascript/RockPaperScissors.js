const getUserChoice = userInput => {
    userInput = userInput.toLowerCase();
    if (userInput === 'rock' || userInput === 'paper' || userInput == 'scissors' || userInput ==='bomb')
    {
      return userInput;
    }
    else{
      console.log('Error');
    }
  };
  const getComputerChoice = () => {
    let rand = Math.floor(Math.random() * 3);
    switch (rand)
    {
      case 0:
      return 'rock';
      break;
      case 1:
      return 'paper';
      break;
      case 2:
      return 'scissors';
      break;
    }
  }
  const determineWinner = (userChoice, computerChoice) => {
    if (userChoice === 'bomb'){
      return 'User Won';
    }
    if (userChoice === computerChoice){
      return 'Tie';
    }
    if (userChoice === 'rock'){
      if (computerChoice === 'paper'){
        return 'Computer won';
      } else{
        return 'User won';
      }
    }
     if (userChoice === 'paper'){
      if (computerChoice === 'scissors'){
        return 'Computer won';
      } else{
        return 'User won';
      }
    }
     if (userChoice === 'scissors'){
      if (computerChoice === 'rock'){
        return 'Computer won';
      } else{
        return 'User won';
      }
    }
  }
  function playGame() {
    let userChoice = getUserChoice('bomb');
    let computerChoice = getComputerChoice();
    console.log(determineWinner(userChoice,computerChoice));
  
  }
  
  playGame()