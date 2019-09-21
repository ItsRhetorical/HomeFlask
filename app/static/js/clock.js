var time = ""


function tickClock(){

    findTime();
    displayDecimalTime();
    displayBitTime();
}


function findTime(){
    var currentTime = new Date();
    var elapsedTime = currentTime - startTime;
    var ms = elapsedTime;
    var hh = Math.floor(ms / 1000 / 60 / 60);
    ms -= hh* 1000 * 60 * 60;
    var mm = Math.floor(ms / 1000 / 60);
    ms -= mm * 1000 * 60;
    var ss = Math.floor(ms / 1000);
    ms -= ss * 1000
    var ds = Math.floor(ms / 100);
    ms -= ds * 100

    time = hh.toString().padStart(2,'0')+mm.toString().padStart(2,'0')+ss.toString().padStart(2,'0')+ds
}

function displayDecimalTime(){

    document.getElementById('1h').innerHTML = time.substr(0,1)
    document.getElementById('0h').innerHTML = time.substr(1,1)
    document.getElementById('1m').innerHTML = time.substr(2,1)
    document.getElementById('0m').innerHTML = time.substr(3,1)
    document.getElementById('1s').innerHTML = time.substr(4,1)
    document.getElementById('0s').innerHTML = time.substr(5,1)
    document.getElementById('ds').innerHTML = time.substr(6,1)

}

function displayBitTime(){

    for(i=0; i<=3; i++){

         displayBit("1h"+i, getBinaryPart(time.substr(0,1),i));
         displayBit("0h"+i, getBinaryPart(time.substr(1,1),i));
         displayBit("1m"+i, getBinaryPart(time.substr(2,1),i));
         displayBit("0m"+i, getBinaryPart(time.substr(3,1),i));
         displayBit("1s"+i, getBinaryPart(time.substr(4,1),i));
         displayBit("0s"+i, getBinaryPart(time.substr(5,1),i));
         displayBit("ds"+i, getBinaryPart(time.substr(6,1),i));
    }

}

function displayBit(id, value){
    if ( value == 1)
    {
        //document.getElementById(id).innerHTML = "<span class=\"glyphicon glyphicon-remove-circle\" aria-hidden=\"true\"></span>";
//        document.getElementById(id).innerHTML = "<svg height=\"20\" width=\"20\">  <circle cx=\"10\" cy=\"10\" r=\"10\" fill=\"black\" /></svg>";
        document.getElementById(id).style.background='black'
    }
    else {
//        document.getElementById(id).innerHTML = "<svg height=\"20\" width=\"20\">  <circle cx=\"10\" cy=\"10\" r=\"10\" fill=\"grey\" /></svg>";
        document.getElementById(id).style.background='grey'
    }
}

function getBinaryPart(num, place){
    if (Math.floor(num/Math.pow(2,place))%2 ==1){
        return 1
    } else {
        return 0
    }
}

function resetTimer() {
    startTime = new Date();
}

var startTime = new Date();
switch(ClockType) {
    case 'Clock':
        startTime.setHours(0);
        startTime.setMinutes(0);
        startTime.setSeconds(0);
        startTime.setMilliseconds(0);
        break;
    case 'Stopwatch':
        document.getElementById('reset_button').style.visibility = 'visible';
        break;
    default:
        alert("failed to pass clock type");
}

function setSizes(){

    var tdWidth = document.getElementById('1h3').getBoundingClientRect().width/2
    var overlayWidth = document.getElementById('1h').getBoundingClientRect().width/2

    var tdTop = document.getElementById('1h3').getBoundingClientRect().top
    var tdHeight = document.getElementById('BinaryDisplay').getBoundingClientRect().height
    var overlayHeight = document.getElementById('1h').getBoundingClientRect().height

    var offsets = {
        'ds': document.getElementById('ds3').getBoundingClientRect().left,
        '0s': document.getElementById('0s3').getBoundingClientRect().left,
        '1s': document.getElementById('1s3').getBoundingClientRect().left,
        '0m': document.getElementById('0m3').getBoundingClientRect().left,
        '1m': document.getElementById('1m3').getBoundingClientRect().left,
        '0h': document.getElementById('0h3').getBoundingClientRect().left,
        '1h': document.getElementById('1h3').getBoundingClientRect().left
    }
    document.getElementById('ds').style.left = offsets['ds'] + tdWidth - overlayWidth + 'px'
    document.getElementById('0s').style.left = offsets['0s'] + tdWidth - overlayWidth + 'px'
    document.getElementById('1s').style.left = offsets['1s'] + tdWidth - overlayWidth + 'px'
    document.getElementById('0m').style.left = offsets['0m'] + tdWidth - overlayWidth + 'px'
    document.getElementById('1m').style.left = offsets['1m'] + tdWidth - overlayWidth + 'px'
    document.getElementById('0h').style.left = offsets['0h'] + tdWidth - overlayWidth + 'px'
    document.getElementById('1h').style.left = offsets['1h'] + tdWidth - overlayWidth + 'px'

    document.getElementById('ds').style.top = tdTop + (tdHeight - overlayHeight)/2 + 'px'
    document.getElementById('0s').style.top = tdTop + (tdHeight - overlayHeight)/2 + 'px'
    document.getElementById('1s').style.top = tdTop + (tdHeight - overlayHeight)/2 + 'px'
    document.getElementById('0m').style.top = tdTop + (tdHeight - overlayHeight)/2 + 'px'
    document.getElementById('1m').style.top = tdTop + (tdHeight - overlayHeight)/2 + 'px'
    document.getElementById('0h').style.top = tdTop + (tdHeight - overlayHeight)/2 + 'px'
    document.getElementById('1h').style.top = tdTop + (tdHeight - overlayHeight)/2 + 'px'
}

window.onresize = setSizes

setSizes();
tickClock();

var tickRate = setInterval(tickClock,100);