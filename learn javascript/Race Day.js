let raceNumber = Math.floor(Math.random() * 1000);
let registerdEarly = false;
let runnerAge = 0;

if (registerdEarly && runnerAge > 15){
  raceNumber += 1000;
}

if (registerdEarly && runnerAge > 18){
  console.log(`${raceNumber} race starts at 9:30 `);
}
else if (!registerdEarly && runnerAge > 18){
  console.log(`${raceNumber} race starts at 11:00 `);
}
else if (runnerAge < 18){
    console.log(`${raceNumber} race starts at 12:30 `);
}
else{
    console.log(`Registration desk `);
}