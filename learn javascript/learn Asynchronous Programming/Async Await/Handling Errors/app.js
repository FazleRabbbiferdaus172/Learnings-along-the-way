const cookBeanSouffle = require('./library.js');

// Write your code below:

async function hostDinnerParty() {
  try {
    let x = await cookBeanSouffle();
    console.log(`${x} is served!`);
  }
  catch (error) {
    console.log(error);
    console.log('Ordering a pizza!');
  }
}
hostDinnerParty();


