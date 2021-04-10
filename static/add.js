$('.poll3').hide();
$('.poll4').hide();
$('.vs3').hide();
$('.vs4').hide();
$('.min').hide();

let poll = [$('.poll3'),$('.poll4')];
let vs = [$('.vs3'),$('.vs4')];
let p = 0
$('.add').click(()=>{
    poll[p].show();;
    vs[p].show();
    p++;
    $(".min").show()
    if (p==2){
        $('.add').hide()

    }
})

$('.min').click(()=>{
    p--;
    poll[p].hide();
    vs[p].hide();
    $('.add').show()
    if (p==0){
        $('.min').hide()
        $('.add').show()
    }
})