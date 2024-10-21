// Jaacript Code Goes here
let img;

function preload(){
    let divData = document.querySelector('#canvas-div');
    let imagePath = divData.getAttribute('data-image');

    if(imagePath){
        img = loadImage('/static/'+imagePath);
    }
}

function setup(){
    let c = createCanvas(600,600);
    c.parent('canvas-div');

    // divData = document.querySelector('#canvas-div');
}

function draw(){
    background(255);

    if(img){
        image(img, 0, 0, width, height);
    }else{
        textAlign(CENTER, CENTER);
        textSize(16);
        fill(0);
        text('No image available.', width/2, height/2);
    }
    
}