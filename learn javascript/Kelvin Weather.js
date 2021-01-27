// kelvin is a constant
const kelvin = 0;
// celsius is 273 less than kelvin
const celsius = kelvin - 273;
let fahrenheit = celsius*(9/5) + 32;
fahrenheit = Math.floor(fahrenheit);
console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);