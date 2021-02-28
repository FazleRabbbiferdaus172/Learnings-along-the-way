// TODO: Create setup() function
function setup(){
  // Inside the setup() function:
  // TODO: Create canvas 500px wide and 500px high
  createCanvas(500,500);
  // TODO: Draw horizontal and vertical guidelines
  line(width/2,0,width/2,height);
  line(0,height/2,width,height/2);
}
function draw() {
// TODO: Create wall drawing inside draw() function
  // Inside the draw() function:
  // Draw parallel lines:
  // TODO: Set stroke color and weight
   stroke(127);
   strokeWeight(10);

  // TODO: Use a for loop to draw 10 vertical lines

    for (let posX = 0 ; posX < 10 ; posX++ ){
    line(posX*25, 0 , posX*25 , height/2);
  }

  // Draw polka dots:
  // TODO: Set no stroke and fill color
  fill('#ffd700');
  noStroke();

  // TODO: Use nested for loops to draw a grid of circles
  // TODO: Offset y positions of every other column by 10 pixels
  for (let x = 0 ; x < 10 ; x++){
    for (let y = 0; y < 10 ; y++){
      if (x % 2 === 0){
      circle(x*25+width/2, y*25+10, 10);}
    else {
      circle(x*25+width/2, y*25, 10);
    }
    }
  }


  // Draw checkered squares:
  // TODO: Set fill color
  fill('red');

  // TODO: Use nested for loops to draw rows of squares
  // TODO: Offset y positions of every other column by 25 pixels
  for (let x = 0 ; x < 10 ; x++){
    for (let y = 0; y < 5 ; y++){
      if (x % 2 === 0){
      square(x*25, y*50+height/2+25, 25);}
      else{
      square(x*25, y*50+height/2, 25);
      }
    }
  }

  
  // Draw parallel diagonal lines:
  // TODO: Set stroke color and weight
  strokeWeight(10);
  stroke(0,0,255);

  // TODO: Use a for loop to draw diagonal lines
  for ( let i = 0; i < 10; i++){
    line(width/2,height-i*25,width/2+i*25,height);
  }

  for ( let i = 0; i < 10; i++){
    line(width/2+i*25,height/2,width,height-i*25);
  }

  // Draw borders:
  // TODO: Set stroke color
  stroke(0);

  // TODO: Draw horizontal and vertical guidelines
    line(width/2,0,width/2,height);
    line(0,height/2,width,height/2);
    noFill()
    square(0,0,500);
  // TODO: Draw borders around canvas

}
