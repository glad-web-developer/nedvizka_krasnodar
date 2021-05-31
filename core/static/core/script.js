function vivisti_uvedomlenie(zagolovok, telo, type) {

    $('#uvedomlenie').find('.uvedomlenie_header').removeClass('bg-warning').removeClass('bg-danger');
    if (type === 'success') {
        $('#uvedomlenie').find('.uvedomlenie_header').addClass('bg-warning');
    }
    if (type === 'error') {
        $('#uvedomlenie').find('.uvedomlenie_header').addClass('bg-danger');
    }
    $('#uvedomlenie').find('.uvedomlenie_title').html(zagolovok);
    $('#uvedomlenie').find('.uvedomlenie_telo').html(telo);

    $('#uvedomlenie').toast('show');
}


function podsvetit_aktivnoe_menu() {
    $('.main_menu').find('.nav-link').each(function () {
        if ((window.location.href.indexOf( $(this).attr('href'))) > -1) {
            $(this).addClass('active');
        }
    });
}

//
$(() => {


    $(document).ready(function () {

        podsvetit_aktivnoe_menu();
        $('.zakritie_sidbara, main').on('click', function () {
            $('.my_sidebar').removeClass('active');
            // $('.overlay').removeClass('active');
        });

        $('.otkritie_sidbara').on('click', function () {
            $('.my_sidebar').toggleClass('active');
            // $('.overlay').addClass('active');
            // $('.collapse.in').toggleClass('in');
            // $('a[aria-expanded=true]').attr('aria-expanded', 'false');
        });
    });


});