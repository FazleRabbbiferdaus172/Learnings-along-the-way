// Write your code here:
function dogFactory(name,breed,weight){
    return {
      _name: name,
      _breed: breed,
      _weight: weight,
      get name(){
       return this._name;
      },
      set name(n){
       this._name = n;
      },
      get breed(){
        return this._breed;
      },
      set breed(b){
       this._breed = b;
      },
      get weight(){
       return this._weight;
      },
      set weight(w){
       this._weight = w;
      },
      bark(){
        return 'ruff! ruff!';
      },
      eatTooManyTreats(){
        this._weight++;
      }
    }
  }