const _ = {
    clamp(n,l,u){
        return Math.min(Math.max(n,l),u);
    },
    inRange(n,start,end){
      if (end === undefined){
        end = start;
        start = 0;
      }
      if (start > end){
        let t = start;
        start = end;
        end = t;
      }
      return (n >= start && n < end);
    },
    words(s){
      return s.split(" ");
    },
    pad(s,l){
      if (l <= s.length){
        return s
      }
      let spl = Math.floor((l - s.length)/2); 
      let epl = l - s.length - spl;
      let pS = " ";
      return pS.repeat(spl) + s + pS.repeat(epl);
  
    },
    has(o,k){
      return o[k] != undefined;
    },
    invert(o){
      let iO = {};
      for(let i in o){
        const oV = o[i];
        iO[oV] =  i ;
        }
      return iO;
  },
    findKey(o,predicate){
      for(let i in o){
        v = o[i];
        let prv = predicate(v);
        if (prv){
          return i;
        }
      }
      return undefined;
    },
    drop(arr,n){
      if (n === undefined){
        n = 1;
      }
      return arr.slice(n,arr.lenght)
    },
    dropWhile(arr,predicate){
      let dN = arr.findIndex((e,i) => !predicate(e,i,arr));
      return this.drop(arr,dN);
    },
    chunk(arr,s){
      if (s === undefined){
        s = 1;
      }
      let acs = [];
      for (let i = 0 ; i < arr.length; i += s){
        let ac = arr.slice(i,i+s);
        acs.push(ac);
      }
      return acs;
    }
  };
  
  
  
  
  // Do not write or modify code below this line.
  module.exports = _;