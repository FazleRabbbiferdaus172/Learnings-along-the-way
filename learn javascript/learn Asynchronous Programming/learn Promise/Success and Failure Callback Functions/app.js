const {checkInventory} = require('./library.js');

const order = [['sunglasses', 1], ['bags', 2]];

// Write your code below:
const handleSuccess = (resolvedVale) => {
  console.log(resolvedVale);
}

const handleFailure = (rejectedValue) => {
  console.log(rejectedValue);
}

checkInventory(order).then(handleSuccess, handleFailure);
