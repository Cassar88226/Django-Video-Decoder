var sign_up = 'sign_up/';
var log_in = 'log_in';
var log_out = 'log_out';
$(document).on('click', ".menu__login__form__submit", function() {
    var email = $("#id_username").val();
    var pwd = $("#id_password").val();
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    console.log(email);
    $.ajax({
        url: log_in,
        headers: {
            "X-CSRFToken": csrftoken
        },
        data: {
            '_email': email,
            '_pwd': pwd,
        },
        cache: true,
        dataType: 'json',
        success: function(data, status) {
            if (data.content == "ok") {
                // $(".PopupMenu").remove();
                window.location.reload();
                // window.location = window.location;
            } else {
                var err = data.content;
                err = err.replace(/password1/g, "Password");
                err = err.replace(/password2/g, "Password confirm")
                document.getElementById('errornote').innerHTML = err;
                document.getElementById('errornote').style.display = "block";
            }
        },
        error: function() {
            document.getElementById('errornote').innerHTML = "Please enter the correct username and password for a staff account";
            document.getElementById('errornote').style.display = "block";
        },
        timeout: 3000
    });
});

$(document).on('click', "#menu_logout", function() {
    $.ajax({
        url: log_out,
        success: function(data, status) {
            window.location.href = '/';
        }
    });
});



