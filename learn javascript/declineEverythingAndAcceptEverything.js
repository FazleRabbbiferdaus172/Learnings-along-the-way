const veggies = ['broccoli', 'spinach', 'cauliflower', 'broccoflower'];

const politelyDecline = (veg) => {
      console.log('No ' + veg + ' please. I will have pizza with extra cheese.');
}

// Write your code here:
const declineEverything = a => a.forEach(politelyDecline);
const acceptEverything = a => a.forEach( i => console.log("Ok, I guess I will eat some "+i+"."));
declineEverything(veggies);
acceptEverything(veggies);