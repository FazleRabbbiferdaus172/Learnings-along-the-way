const Calculate = {
    factorial(input){
      let fact = 1;
      for (let i = 2; i <= input ; i++){
        fact *= i;
      }
      return fact;
    }
  }
  
  module.exports = Calculate;
  
  
  