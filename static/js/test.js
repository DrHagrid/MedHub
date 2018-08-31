$(document).ready(function () {
    var form = $('#test');
    var ans_btn = $('#answer_btn');

    function next(test_type, unit, section, test_id, element_id){
        var data = {};
        data.action = 'next';
        data.test_type = test_type;
        data.unit = unit;
        data.section = section;
        data.test_id = test_id;
        data.element_id = element_id;

        var csrf_token = $('#test [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr("action");
        $.ajax({
            url:url,
            type:'POST',
            data:data,
            cache:true,
            success: function(data){
                if (data.test_type == 'input') {
                    $('.form-group').html('<input class="form-control" id="answer" placeholder="Введите ответ">');
                    $('.form-group').removeClass('has-success');
                    $('.form-group').removeClass('has-danger');
                    $('#answer').val('');

                }
                if (data.test_type == 'radio') {
                    $('.form-group').html(data.options_html);
                }

                $('.element-title').html(data.title);
                if (data.image_url) {
                    if ($('.test-img').html().trim() != '') {
                        $('#test-img-img').attr('src', data.image_url)
                    }
                    else {
                        $('.test-img').html("");
                        $('.test-img').append('<img src="' + data.image_url + '" class="img-fluid" id="test-img-img">');
                    }
                }
                else {
                    $('.test-img').html("");
                }
                $('#test_btn').html("Проверить");
                test_btn.setAttribute('data-action', 'check');

                answer_btn.setAttribute('data-answer', data.answer);
                answer_btn.setAttribute('disabled', '');
                $('.alert-answer').html("");
            },
            error: function(){
                console.log("ERROR");
            }
        });
    };

    function check(test_type, unit, section, test_id, element_id, answer, start){
        var data = {};
        data.action = 'check';
        data.test_type = test_type;
        data.unit = unit;
        data.section = section;
        data.test_id = test_id;
        data.element_id = element_id;
        data.answer = answer;
        data.start = start;

        var csrf_token = $('#test [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr("action");
        $.ajax({
            url:url,
            type:'POST',
            data:data,
            cache:true,
            success: function(data){
                if (data.response == 'True') {
                    var percent = Math.round((parseInt($('.counter').text()) + 1) / parseInt($('.total').text()) * 100);
                    test_progress.setAttribute('style', 'width: ' + percent + '%');
                    test_progress.setAttribute('aria-valuenow', percent);
                    $('.counter').html(parseInt($('.counter').text()) + 1);

                    $('.form-group').removeClass('has-danger');
                    $('.form-group').addClass('has-success');
                    $('#answer').focus();
                    if (data.next_element_id != 0) {
                        $('#test_btn').html("Продолжить");
                        test_btn.setAttribute('data-action', 'next');
                        test_btn.setAttribute('data-test_type', data.next_test_type);
                        test_btn.setAttribute('data-element_id', data.next_element_id);
                    }
                    else {
                        $('#test_btn').html("Завершить");
                        test_btn.setAttribute('data-action', 'end');
                        test_btn.setAttribute('data-element_id', data.next_element_id);
                    }
                }
                else {
                    $('.form-group').addClass('has-danger');
                    $('#answer').focus();
                    $('#answer_btn').removeAttr('disabled');
                }
            },
            error: function(){
                console.log("ERROR");
            }
        });
    };

    form.on('submit', function (e) {
        e.preventDefault();

        var btn = $('#test_btn');
        var test_type = test_btn.getAttribute("data-test_type");
        var action = test_btn.getAttribute("data-action");

        var unit = btn.data("unit");
        var section = btn.data("section");

        var test_id = btn.data("test_id");
        var element_id = test_btn.getAttribute("data-element_id");
        var start = test_btn.getAttribute("data-start");
        test_btn.setAttribute("data-start", "false");


        if (test_type == 'input') {
            var answer = $('#answer').val();
        }
        if (test_type == 'radio') {
            var radio = $('input[name=test]:checked');
            var answer = radio.val()
        }
        if (action == 'check') {
            check(test_type, unit, section, test_id, element_id, answer, start);
        }
        if (action == 'next') {
            next(test_type, unit, section, test_id, element_id);
        }
        if (action == 'end') {
            document.location.href = '/start/' + unit + '/' + section + '/test/' + test_id + '/stat/';
        }
    });

    ans_btn.on('click', function (e) {
        e.preventDefault();
        var answer = answer_btn.getAttribute("data-answer");
        $('.alert-answer').html("");
        $('.alert-answer').append('<div class="alert alert-warning">\n' +
            '                <div class="container">\n' +
            '                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">\n' +
            '                        <span aria-hidden="true"><i class="material-icons">clear</i></span>\n' +
            '                    </button>\n' +
            '                    <b>Ответ: <span class="answer">' + answer + '</span></b>\n' +
            '                </div>\n' +
            '            </div>');

    });
});