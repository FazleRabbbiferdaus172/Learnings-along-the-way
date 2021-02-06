const fruits = ['mango', 'papaya', 'pineapple', 'apple'];

// Iterate over fruits below
fruits.forEach(a => console.log('I want to eat a ' + a ));


const animals = ['Hen', 'elephant', 'llama', 'leopard', 'ostrich', 'Whale', 'octopus', 'rabbit', 'lion', 'dog'];

// Create the secretMessage array below
const secretMessage = animals.map(i => i[0]);
console.log(secretMessage.join(''));

const bigNumbers = [100, 200, 300, 400, 500];
const smallNumbers = bigNumbers.map(i => i/100);

const randomNumbers = [375, 200, 3.14, 7, 13, 852];

// Call .filter() on randomNumbers below
const smallNumbers = randomNumbers.filter(i => i < 250);

const favoriteWords = ['nostalgia', 'hyperbole', 'fervent', 'esoteric', 'serene'];

const longFavoriteWords = favoriteWords.filter(i => i.length > 7);
console.log(longFavoriteWords);
// Call .filter() on favoriteWords below

const animals = ['hippo', 'tiger', 'lion', 'seal', 'cheetah', 'monkey', 'salamander', 'elephant'];

const foundAnimal = animals.findIndex(i => i === 'elephant');

const startsWithS = animals.findIndex(i => i[0] === 's');

const newNumbers = [1, 3, 5, 7];
const newSum = newNumbers.reduce((accumulator,currentValue) => {
  console.log('The value of accumulator: ', accumulator);
  console.log('The value of currentValue: ', currentValue);
  return accumulator + currentValue;
}, 10)

console.log(newSum);