function vivisti_uvedomlenie(zagolovok, telo, type) {

    $('#uvedomlenie').find('.uvedomlenie_header').removeClass('bg-info').removeClass('bg-danger');
    if (type === 'success') {
        $('#uvedomlenie').find('.uvedomlenie_header').addClass('bg-info');
    }
    if (type === 'error') {
        $('#uvedomlenie').find('.uvedomlenie_header').addClass('bg-danger');
    }
    $('#uvedomlenie').find('.uvedomlenie_title').html(zagolovok);
    $('#uvedomlenie').find('.uvedomlenie_telo').html(telo);

    $('#uvedomlenie').toast('show');
}
//
$(() => {



     $(document).ready(function () {


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