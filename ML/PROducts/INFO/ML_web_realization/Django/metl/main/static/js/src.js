$(".scrolltocomp a").on("click", function () {
    let href = $(this).attr("href");

    $("html, body").animate({
        scrollTop: $(href).offset().top
    }, {
        duration: 1000,   // по умолчанию «400»
        easing: "linear" // по умолчанию «swing»
    });

    return false;
});

$(".scrolltocalc a").on("click", function () {
    let href = $(this).attr("href");

    $("html, body").animate({
        scrollTop: $(href).offset().top
    }, 
    {
        duration: 1000,   // по умолчанию «400»
        easing: "linear" // по умолчанию «swing»
        
    });


    return false;
});


const MyButtonSave = document.getElementById('button_rasschitat');
const MyButtonOpen = document.getElementById('open');

MyButtonSave.addEventListener("click", function () {
    MyButtonOpen.addEventListener(this.style.display == 'block');
});