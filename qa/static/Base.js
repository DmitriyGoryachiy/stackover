$(document).ready(function () {


        $('.question-edit-link').click(function() {
            $('.bgdialog').show();
            $('.dialog').load($(this).attr('href'));
            return false;
        })

        $(document).on('submit','ajax-form', function() {
            var form = $(this);
            $.ajax({url: form.attr('action'), method: 'POST', data: $('form').serialize()})
//            $.post(form.attr('action'), form.serialize(), function(data) {
//                form.html(data)
//            })
            return false;
        })


//        $('.ajax-form').click(function() {
//            var form = $(this);
//            $form.on("submit", function() {
//                $.post('/', function(response){
//                    $(".title").html(response)
//                })
//            })
//            return false;
////            var element = $(this);
////            $.post('/',function(data) {
////                element.html(data)
////            })
//        })
//        $('.ajax-form').click(function() {
//           var form = $(this);
//            $.post(form.attr('action'), form.serialize(), function(data) {
//                form.html(data)
//            })
//            return false;
//        })

        function csrfSafeMethod(method) {
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
                }
            }
        });


    function updateLikes() {
        var ids = Array();
        $('.likecount').each(function () {
            ids.push($(this).data('question-id'))
        });

        $.getJSON('/questions/likes/', {ids: ids.join(',')}, function (data) {
            for (var i in data) {
                $('.likecount[data-question-id='+i+']').html(data[i]);
            }
        })

    }
    updateLikes();

//    window.setInterval(updateLikes, 2000);

    $('.likecount').click(function() {
        var url = $(this).data('likes-url');
        var element = $(this);
        $.post(url,function(data) {
            element.html(data)
        })
    })





//    $("#search-field").autocomplete({
//        source: "/ajax_calls/myFunction",
//        minLength: 2,
//    });





});