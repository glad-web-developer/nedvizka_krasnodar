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
        if ((window.location.href.indexOf($(this).attr('href'))) > -1) {
            console.log(window.location.href)
            if ($(this).attr('href') !== '//95.189.108.18/') {
                $(this).addClass('active');
            } else {
                if (window.location.href === 'http://95.189.108.18/') {
                    $(this).addClass('active');
                }
            }


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


        $('.lightgallery2').lightGallery({
            thumbnail: true,
            share: false,
            download: false,
            zoom: false,
            autoplay: false,
            fullScreen: false,
            autoplayControls: false
        });

    });

    $('.dv_nedvizka input.number').keyup(function (e) {
        this.value = this.value.replace(" ", "").replace(" ", "");
        this.value = this.value.replace(/(\d)(?=(\d{3})+([^\d]|$))/g, "$1 ");
        rashitatIpoteku();
    });

    $('#input_srok').change(function (){
        rashitatIpoteku();
    })


    function rashitatIpoteku() {
        let data = {
            'stoimost': $('#input_stoimost').val(),
            'pervonachalni_vznos': $('#input_pervonachalni_vznos').val(),
            'srok': $('#input_srok').val(),
            'stavka': $('#input_stavka').val(),
        };

        $.get("/api/ipoteka/", data).done(function (data){
            $('.val_summa_kredita').text(data.summa_kredita.replace(/(\d)(?=(\d{3})+([^\d]|$))/g, "$1 "));
            $('.val_ezemes_platez').text(data.ezemes_platez.replace(/(\d)(?=(\d{3})+([^\d]|$))/g, "$1 "));
            $('.val_pereplata').text(data.pereplata.replace(/(\d)(?=(\d{3})+([^\d]|$))/g, "$1 "));
            $('.val_obshaia_viplata').text(data.obshaia_viplata.replace(/(\d)(?=(\d{3})+([^\d]|$))/g, "$1 "));
            $('.progress-bar-kredit').css('width', data.dolia_kredita+'%');
            $('.progress-bar-pereplata').css('width', data.dolia_pereplati+'%');


        }).fail(function (error) {
            $('.val_summa_kredita').text(0);
            $('.val_ezemes_platez').text(0);
            $('.val_pereplata').text(0);
            $('.val_obshaia_viplata').text(0);
            $('.progress-bar-kredit').css('width', 0);
            $('.progress-bar-pereplata').css('width', 0);
        })

    }

    rashitatIpoteku();


});

