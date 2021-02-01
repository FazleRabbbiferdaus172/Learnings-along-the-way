const howOld = (age,year) => {
    let yDiff = year - 2021
    let aY = Math.abs(yDiff + age)
    let nAge = age + yDiff;
    if (year > 2021){
      return `You will be ${nAge} in the year ${year}`
    }
    else if (year < 2021 - age) {
      return `'The year ${year} was ${aY} years before you were born'`
    }
    else if (year > 2021 - age && year < 2021){
      return `You were ${nAge} in the year ${year}`
    }
  }