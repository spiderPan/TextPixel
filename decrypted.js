var myImg = new Image(),
    canvas = document.createElement('canvas'),
    context = canvas.getContext('2d'),
    ascList = [];
myImg.src = '/wp-content/themes/northern/images/puzzle.png';
context.drawImage(myImg, 0, 0);
for (var x = 0; x < myImg.width; x++) {
    for (var y = 0; y < myImg.height; y++) {
        var data = context.getImageData(x, y, 1, 1).data;
        ascList.push(data[0])
        ascList.push(data[1])
        ascList.push(data[2])
    }
}

str = String.fromCharCode.apply(null, ascList);
