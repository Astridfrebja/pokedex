// ===== Elementer =====

const button = document.getElementById("button");
const buttonImage = document.getElementById("button-image");

const menu = document.getElementById("menu");

const camera = document.getElementById("camera");
const gallery = document.getElementById("gallery");

const imagePicker = document.getElementById("image-picker");

// ===== Tilstand =====

let selected = 0;

// ===== Meny =====

function updateMenu(){

    camera.classList.toggle("selected", selected === 0);
    gallery.classList.toggle("selected", selected === 1);

}

button.addEventListener("click", (event)=>{

    event.stopPropagation();

    buttonImage.classList.add("pressed");

    setTimeout(()=>{

        buttonImage.classList.remove("pressed");

    },100);

    menu.classList.toggle("show");

    updateMenu();

});

// ===== Tastatur =====

document.addEventListener("keydown",(event)=>{

    if(!menu.classList.contains("show")) return;

    if(event.key==="ArrowUp"){

        selected=0;
        updateMenu();

    }

    else if(event.key==="ArrowDown"){

        selected=1;
        updateMenu();

    }

    else if(event.key==="Enter"){

        if(selected===0){

            openCamera();

        }

        else{

            openGallery();

        }

    }

});

// ===== Kamera =====

camera.addEventListener("click",(event)=>{

    event.stopPropagation();

    selected=0;
    updateMenu();

    openCamera();

});

// ===== Galleri =====

gallery.addEventListener("click",(event)=>{

    event.stopPropagation();

    selected=1;
    updateMenu();

    openGallery();

});

function openCamera(){

    menu.classList.remove("show");

    alert("Her skal kamera åpnes");

}

function openGallery(){

    menu.classList.remove("show");

    imagePicker.click();

}

// ===== Lukk meny =====

document.addEventListener("click",(event)=>{

    if(
        !menu.contains(event.target) &&
        !button.contains(event.target)
    ){

        menu.classList.remove("show");

    }

});