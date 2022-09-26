// https://www.fantasyfootballdatapros.com/our_api clutchest mf on the internet

// Fix the math: do average for entire group (find projected stats for season)

// https://stackoverflow.com/a/4033310
function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}





var json = [];

var a = "";
var b = "";
var c = "";
var d = "";
var e = "";
var f = "";

function myCallback(text){
  json = JSON.parse(text);  
}

function correct(){
  a = document.getElementById('given1').value;
  a = a.toLowerCase()
    .split(' ')
    .map((s) => s.charAt(0).toUpperCase() + s.substring(1))
    .join(' ');

  b = document.getElementById('given2').value;
  b = b.toLowerCase()
    .split(' ')
    .map((s) => s.charAt(0).toUpperCase() + s.substring(1))
    .join(' ');

  c = document.getElementById('given3').value;
  c = c.toLowerCase()
    .split(' ')
    .map((s) => s.charAt(0).toUpperCase() + s.substring(1))
    .join(' ');

  d = document.getElementById('received1').value;
  d = d.toLowerCase()
    .split(' ')
    .map((s) => s.charAt(0).toUpperCase() + s.substring(1))
    .join(' ');

  e = document.getElementById('received2').value;
  e = e.toLowerCase()
    .split(' ')
    .map((s) => s.charAt(0).toUpperCase() + s.substring(1))
    .join(' ');

  f = document.getElementById('received3').value;
  f = f.toLowerCase()
    .split(' ')
    .map((s) => s.charAt(0).toUpperCase() + s.substring(1))
    .join(' ');


}

function calculate(){
  var givenIndex = [];
  var receivedIndex = [];
  var html = "";


  for(var i = 0; i < json.length; i++){
    if(json[i].player_name == a){
      console.log(a);
      givenIndex.push(i);
      var gTeam = json[i].team;
      console.log(gTeam) //0
    }
    if(json[i].player_name == b){
      givenIndex.push(i); //1
      var gTeam = json[i].team;
      console.log(gTeam)
    }
    if(json[i].player_name == c){
      givenIndex.push(i); //2
      var gTeam = json[i].team;
      console.log(gTeam)
    } 
}
  for(var i = 0; i < json.length; i++){
    if(json[i].player_name == d){
      receivedIndex.push(i);
      var rTeam = json[i].team;
      console.log(rTeam)
    }
    if(json[i].player_name == e){
      receivedIndex.push(i);
      var rTeam = json[i].team;
      console.log(rTeam)
    }
    if(json[i].player_name == f){
      receivedIndex.push(i);
      var rTeam = json[i].team;
      console.log(rTeam)
    }
  }



var gValue = 0;
var gValue1 = 0;
var gValue2 = 0;
//Given Calculations
if(givenIndex[0] != undefined){  
var gScore = json[givenIndex[0]].projection

if(json[givenIndex[0]].pos == "QB"){
  gValue = gScore / 116.; //116
}
if(json[givenIndex[0]].pos == "RB"){
  gValue = gScore / 85; //85
}
if(json[givenIndex[0]].pos == "WR"){
  gValue = gScore / 86.7; // 86.7
}
if(json[givenIndex[0]].pos == "TE"){
  gValue = gScore / 65; //60
}
}
else if((givenIndex[1] != undefined)){
  var gScore1 = json[givenIndex[1]].projection
if(json[givenIndex[1]].pos == "QB"){
  gValue1 = gScore1 / 116;
}
if(json[givenIndex[1]].pos == "RB"){
  gValue1 = gScore1 / 85;
}
if(json[givenIndex[1]].pos == "WR"){
  gValue1 = gScore1 / 86.7;
}
if(json[givenIndex[1]].pos == "TE"){
  gValue1 = gScore1 / 65;
} 
}

else if(givenIndex[2] != undefined){
  var gScore2 = json[givenIndex[2]].projection
if(json[givenIndex[2]].pos == "QB"){
  gValue2 = gScore2 / 116;
}
if(json[givenIndex[2]].pos == "RB"){
  gValue2 = gScore2 / 85;
}
if(json[givenIndex[2]].pos == "WR"){
  gValue2 = gScore2 / 86.7;
}
if(json[givenIndex[2]].pos == "TE"){
  gValue2 = gScore2 / 65;
}
}


if((gValue1 == 0) && (gValue2 == 0)){
var totalGValue = (gValue);

}
if((gValue1 != 0) && (gValue2 == 0)){
var totalGValue = ((gValue + gValue1) / 2);
}
if((gValue1 != 0) && (gValue2 != 0)){
var totalGValue = ((gValue + gValue1 + gValue2) / 3);
}



//Received Calculations

var rValue = 0;
var rValue1 = 0;
var rValue2 = 0;


if(receivedIndex[0] != undefined){  
var rScore = json[receivedIndex[0]].projection

if(json[receivedIndex[0]].pos == "QB"){
  rValue = rScore / 116;
}
if(json[receivedIndex[0]].pos == "RB"){
  rValue = rScore / 85;
}
if(json[receivedIndex[0]].pos == "WR"){
  rValue = rScore / 86.7;
}
if(json[receivedIndex[0]].pos == "TE"){
  rValue = rScore / 65;
}
}

if((receivedIndex[1] != undefined)){
  var rScore1 = json[receivedIndex[1]].projection
if(json[receivedIndex[1]].pos == "QB"){
  rValue1 = rScore1 / 116;
}
if(json[receivedIndex[1]].pos == "RB"){
  rValue1 = rScore1 / 85;
}
if(json[receivedIndex[1]].pos == "WR"){
  rValue1 = rScore1 / 86.7;
}
if(json[receivedIndex[1]].pos == "TE"){
  rValue1 = rScore1 / 65;
} 
}

if(receivedIndex[2] != undefined){
  var rScore2 = json[receivedIndex[2]].projection
if(json[receivedIndex[2]].pos == "QB"){
  rValue2 = rScore2 / 116;
}
if(json[receivedIndex[2]].pos == "RB"){
  rValue2 = rScore2 / 85;
}
if(json[receivedIndex[2]].pos == "WR"){
  rValue2 = rScore2 / 86.7;
}
if(json[receivedIndex[2]].pos == "TE"){
  rValue2 = rScore2 / 65;
}
} 

if((rValue1 == 0) && (rValue2 == 0)){
var totalRValue = (rValue);
}
if((rValue1 != 0) && (rValue2 == 0)){
var totalRValue = ((rValue + rValue1) /2);
}
if((rValue1 != 0) && (rValue2 != 0)){
var totalRValue = ((rValue + rValue1 + rValue2) / 3);
}


console.log(rValue);
console.log(totalRValue);

totalGValue *= 10;
totalGValue = totalGValue.toFixed(2);
totalRValue *= 10;
totalRValue = totalRValue.toFixed(2);




if((totalGValue == 0) || (totalRValue == 0)){
  html+= "<div>Something went wrong! Make sure your players' names are spelled correctly and placed in the right boxes</div>";
}

else if (totalGValue < totalRValue){
  html += "<div> Player 2 gets the best of this trade. He or she is only giving " + totalGValue + " Value Points away, while receiving " + totalRValue + "</div>";
  totalGValue = 0;
  totalRValue = 0;
;
}
else if (totalGValue > totalRValue){
  html += "<div> Player 1 gets the best of this trade. He or she is only giving " + totalRValue + " Value Points away, while receiving " + totalGValue + "</div>";
  totalGValue = 0;
  totalRValue = 0;
}


   document.getElementById('results1Box').innerHTML = html;

}

document.onkeydown = function(e){
    if(e.keyCode == 13){
    calculate();

  }
}
httpGetAsync('https://www.fantasyfootballdatapros.com/api/projections', myCallback);

