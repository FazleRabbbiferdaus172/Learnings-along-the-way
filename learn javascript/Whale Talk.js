let input = 'turpentine and turtles';
let v = ['a','e','i','o','u'];
let rA = [];
for (let i = 0 ; i < input.length ; i++){
  for (let j = 0 ; j < v.length ; j++){
    if (input[i] === v[j]){
      rA.push(input[i]);
      if (v[j] === 'u' || v[j] === 'e'){
        rA.push(input[i]);
      }
      break;
    }
  }
} 

console.log(rA.join('').toUpperCase());
