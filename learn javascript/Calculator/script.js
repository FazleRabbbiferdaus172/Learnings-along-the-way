
const add = () => {
    let inp1 = document.getElementById("inp1").value;
    let inp2 = document.getElementById("inp2").value;
    let ans = Number(inp1) + Number(inp2);
    if (Number(inp2) < 0){
        inp2 = "("+inp2+")";
    }
    let result = inp1 + " + " + inp2 + " = " + ans;
    let res = document.getElementById("Result"); 
    res.innerHTML = res.innerHTML + result + "<br>";
} 

const sub = () => {
    let inp1 = document.getElementById("inp1").value;
    let inp2 = document.getElementById("inp2").value;
    let ans = Number(inp1) - Number(inp2);
    if (Number(inp2) < 0){
        inp2 = "("+inp2+")";
    }
    let result = inp1 + " - " + inp2 + " = " + ans;
    let res = document.getElementById("Result"); 
    res.innerHTML = res.innerHTML + result + "<br>";
} 

const mul = () => {
    let inp1 = document.getElementById("inp1").value;
    let inp2 = document.getElementById("inp2").value;
    let ans = Number(inp1) * Number(inp2);
    if (Number(inp2) < 0){
        inp2 = "("+inp2+")";
    }
    let result = inp1 + " * " + inp2 + " = " + ans;
    let res = document.getElementById("Result"); 
    res.innerHTML = res.innerHTML + result + "<br>";
} 

const div = () => {
    let inp1 = document.getElementById("inp1").value;
    let inp2 = document.getElementById("inp2").value;
    if (Number(inp2) < 0){
        inp2 = "("+inp2+")";
    }
    if (Number(inp2) === 0){
        alert("Math Error");
    }
    else{
    let ans = Number(inp1) / Number(inp2);

    let result = inp1 + " / " + inp2 + " = " + ans;
    let res = document.getElementById("Result"); 
    res.innerHTML = res.innerHTML + result + "<br>";}
} 

const check = () => {
    console.log("i clicked");
    let res = document.getElementById("Result"); 
    res.innerHTML = "";
}