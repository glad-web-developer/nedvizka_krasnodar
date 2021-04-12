// function vivisti_uvedomlenie(zagolovok, telo, type) {
//
//     $('#uvedomlenie').find('.uvedomlenie_header').removeClass('bg-success').removeClass('bg-danger');
//     if (type === 'success') {
//         $('#uvedomlenie').find('.uvedomlenie_header').addClass('bg-success');
//     }
//     if (type === 'error') {
//         $('#uvedomlenie').find('.uvedomlenie_header').addClass('bg-danger');
//     }
//     $('#uvedomlenie').find('.uvedomlenie_title').html(zagolovok);
//     $('#uvedomlenie').find('.uvedomlenie_telo').html(telo);
//
//     $('#uvedomlenie').toast('show');
// }
//
$(() => {

    // $('.lightgallery2').lightGallery({
    //     thumbnail: true,
    //     share: false,
    //     download: false,
    //     zoom: false,
    //     autoplay: false,
    //     fullScreen: false,
    //     autoplayControls: false
    // });
    //
    //
    // $('.forma_obratnoi_sviazi form').submit(function (e) {
    //     e.preventDefault();
    //
    //     let url = e.currentTarget.action;
    //     let data = $(e.currentTarget).serialize();
    //     $(e.currentTarget).find('.btn').attr('disabled', 'disabled').text('Заявка отправлена');
    //     $.ajax({
    //         url: url,
    //         type: 'post',
    //         dataType: 'application/json',
    //         data: data,
    //         complete: function (data) {
    //             if (data.status === 200) {
    //                vivisti_uvedomlenie(
    //                    'Заявка отправлена',
    //                    ' <b class="">Ваша заявка отправлена. <br>Мы Вам перезвоним</b>',
    //                    'success')
    //             } else {
    //                  vivisti_uvedomlenie(
    //                    'Что-то пошло не так',
    //                    ' <b class="">Попробуйте обновить страницу и отправить форму повторно.<br> Если не получиться, то пожалуйста сообщите нам о проблеме</b>',
    //                    'error')
    //             }
    //         }
    //     });


    // })


     $(document).ready(function () {


            $('.zakritie_sidbara, main').on('click', function () {
                $('.my_sidebar').removeClass('active');
                // $('.overlay').removeClass('active');
            });

            $('.otkritie_sidbara').on('click', function () {
                $('.my_sidebar').addClass('active');
                // $('.overlay').addClass('active');
                // $('.collapse.in').toggleClass('in');
                // $('a[aria-expanded=true]').attr('aria-expanded', 'false');
            });
        });


});