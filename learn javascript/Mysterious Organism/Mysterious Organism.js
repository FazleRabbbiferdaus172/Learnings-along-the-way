// Returns a random DNA base
const returnRandBase = () => {
    const dnaBases = ['A', 'T', 'C', 'G']
    return dnaBases[Math.floor(Math.random() * 4)] 
  }
  
  // Returns a random single stand of DNA containing 15 bases
  const mockUpStrand = () => {
    const newStrand = []
    for (let i = 0; i < 15; i++) {
      newStrand.push(returnRandBase())
    }
    return newStrand
  }
  
  
  function pAequorFactory(num,arr){
    return {
      specimenNum : num,
      dna : arr,
      mutate(){
        let x = ['A','T','C','G'];
        i = Math.floor(Math.random()*16);
        j = Math.floor(Math.random()*4);
        while (this.dna[i] === x[j]){
            j = Math.floor(Math.random()*4);
        }
        this.dna[i] = x[j];
        return this.dna;
      },
      compareDNA(obj){
      let s = 0;
      for (let i = 0; i < 15; i++){
        if (this.dna[i] === obj.dna[i]){
          s++;
        }
      }
      let ans = (s/15)*100;
      console.log("common in ",this.specimenNum," and ",obj.specimenNum, " is : ",ans);
    },
    willLikelySurvive(){
      let s = 0;
      for (let i = 0; i < 15; i++){
        if (this.dna[i] === 'G' || this.dna[i] === 'C'){
          s++;
        }
      }
      let ans = (s/15)*100;
      return ans >= 60;
    },
    }
  }
  
  //let x = pAequorFactory(1,mockUpStrand());
  //let y = pAequorFactory(2,mockUpStrand());
  //console.log(x.willLikelySurvive());
  
  let ans = [];
  let i = 0;
  
  while (ans.length < 30){
    let x = pAequorFactory(i,mockUpStrand());
    if (x.willLikelySurvive()){
      ans.push(x);
      i++;
    }
  }
  
  console.log(ans.length);
  
  
  
  
  
  
  
  