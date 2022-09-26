var name = "";
var count = 0;
var globalHighScore = 0;
var i = 0;
var json = [];
var startCount = 0;
var prevScore = 0;

window.onload = function () {
  globalHighScore = localStorage.getItem('high-score')
  prevScore = localStorage.getItem('previous-score')
  count = 0;
  flag(random());
};

document.onkeydown = function(e){
  if(e.keyCode == 13){
    guess();
  }
}

document.getElementById('timer').innerHTML = "1:00";

function startTimer() {
  var presentTime = document.getElementById('timer').innerHTML;
  var timeArray = presentTime.split(/[:]+/);
  var m = timeArray[0];
  var s = checkSecond((timeArray[1] - 1));
  if(s==59){m=m-1}
  

  document.getElementById('timer').innerHTML =  m + ":" + s;
  setTimeout(startTimer, 1000);
  if(s == 0 && m == 0){
    location.reload();
  }
  startCount += 1;
    document.getElementById("btn").style.display = "none";
}

function checkSecond(sec) {
  if (sec < 10 && sec >= 0) {sec = "0" + sec}; // add zero in front of numbers < 10
  if (sec < 0) {sec = "59"};
  return sec;
}


function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}


//https://restcountries.eu/rest/v2/all
function myCallback(text) {
  json = JSON.parse(text);
  flag(random());
}



function guess(q){
  var htmlOne = ' ';
  q = document.getElementById('search').value;

  if(q === name){
    count+= 1;
    json.splice(i, 1);
    flag(random());
    document.getElementById('search').value = "";
  }

  document.getElementById('score-container').innerHTML = htmlOne;
}


//200
function random(){
  i = Math.floor(Math.random() * json.length);
  var country = json[i];
  return country;
}

function flag(country) {
  var html = '';
  random();
  if(name === null){
    random();
  }
  

  name = country.name;
  console.log('this flag is', name);
  var flag = country.flag;
  var alpha2code = country.alpha2Code.toLowerCase();

  html += '<div>Score: ' + count + '</div>';

  if(count > globalHighScore){
    globalHighScore = count;
    localStorage.setItem('high-score', globalHighScore);
  }

  html += '<div>Previous Score: ' + prevScore + '</div>';
  html += '<div>High Score: ' + globalHighScore + '</div>';
   //html += '<div class="flex flag-tile">';

  if(startCount > 0){
   html += '<img class="icon" src="https://flagcdn.com/' + alpha2code + '.svg">';
  }
  html += '</div>';
   
  document.getElementById('flag-container').innerHTML = html;
  localStorage.setItem('previous-score', count);
  
}
  



httpGetAsync('list.json', myCallback);



