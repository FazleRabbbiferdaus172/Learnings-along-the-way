function finalGrade (a,b,c){
    if (a > 100 || a < 0 ||  b > 100 || b < 0 || c > 100 || c < 0){
      return 'You have entered an invalid grade.';
    }
  
    let avg = (a+b+c)/3;
  
    if (avg >= 0 && avg <= 59){
      return 'F';
    }
    else if (avg >= 60 && avg <= 69){
      return 'D';
    }
    else if (avg >= 70 && avg <= 79){
      return 'C';
    }
    else if (avg >= 80 && avg <= 89){
      return 'B';
    }
    else if (avg >= 90 && avg <= 100){
      return 'A';
    }
  }
  
  