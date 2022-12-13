$(function(){
    $(document).on("click", "#logout", function(){
        sessionStorage.clear()
        window.location = `index.html`;
    })
})