var myImg = new Image(),
    canvas = document.createElement('canvas'),
    context = canvas.getContext('2d'),
    ascList = [];

myImg.onload = function() {
    context.drawImage(myImg, 0, 0);
    ascList = context.getImageData(0, 0, myImg.width, myImg.height).data.filter(function(value, index) {
        return (index + 1) % 4 !== 0;
    });
    console.log(String.fromCharCode.apply(null, ascList));
}
myImg.src = '/wp-content/themes/northern/images/puzzle.png';
