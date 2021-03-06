var assert = require("assert");
var Calculate =  require('../index.js')

describe('Calculate', () => {
  describe('.factorial', () => {
    it('result is 120 if the input is 5',() =>{
      const expectedResult = 120;
      const input = 5;
      const result = Calculate.factorial(input);
      assert.equal(result,expectedResult);
    });

      it('result is 6 if the input is 3',() =>{
      const expectedResult = 6;
      const input = 3;
      const result = Calculate.factorial(input);
      assert.equal(result,expectedResult);
    });

          it('result is 1 if the input is 0',() =>{
      const expectedResult = 1;
      const input = 0;
      const result = Calculate.factorial(input);
      assert.equal(result,expectedResult);
    });

  });
});