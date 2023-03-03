async function click_sound(event) {
    const audio = new Audio('../static/sounds/click_sound.mp3');
    audio.preload = 'auto'

    event.preventDefault();
    
    await audio.play();
    
    window.location = event.currentTarget.href;
    
}


function getDeepslatePosition() {
    var randomX = Math.floor(Math.random() * 31) * 66;
    var randomY = Math.floor(Math.random() * 12) * 66;
    return randomX + "px " + randomY + "px";
}
function getStonePosition() {
    var randomX = Math.floor(Math.random() * 31) * 66;
    var randomY = Math.floor(Math.random() * 4) * 66;
    return randomX + "px " + randomY + "px";
}

var sectionMain = document.getElementById("section-main");
sectionMain.style.backgroundPosition = getDeepslatePosition() + ", " + getDeepslatePosition() + ", " + getDeepslatePosition() + ", " + getDeepslatePosition() + ", " + getDeepslatePosition() + ", " + "66px 66px";

var headerMain = document.getElementById("header-main");
headerMain.style.backgroundPosition = getStonePosition() + ", " + getStonePosition() + ", " + getStonePosition() + ", " + getStonePosition() + ", " + getStonePosition() + ", " + getStonePosition() + ", " + "66px 66px";