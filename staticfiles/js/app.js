$(function () {
  // Get CSRF token from the cookie or the hidden input field
  function getCSRFToken() {
    var csrfToken = $("input[name='csrfmiddlewaretoken']").val(); // CSRF token from the form
    if (!csrfToken) {
      csrfToken = Cookies.get('csrftoken'); // Alternatively, get from cookies if you're using js-cookie
    }
    return csrfToken;
  }

  $('#image').on('change', function () {
    const file = this.files[0];
    const reader = new FileReader();
    const img = $('#previewImage');

    reader.onload = function (e) {
      img.attr('src', e.target.result);
      img.show();
    };

    if (file) {
      reader.readAsDataURL(file);
    }
  });

  
  $('#submit').click(async function () {
    var $btn = $(this);

    const item = localStorage.getItem('selectedModel')

    var form_data = new FormData($('#uploadForm')[0]);
    var qrScanner = $('#qrScanner');

    const imgSrc = $('#previewImage').attr('src');

    if (!imgSrc) {
      swal('Image not found!', '', 'error');
      return;
    }

    if (!item) {
      swal('Model not found!', '', 'error');
      return;
    }

    form_data.append('model', item);

    $btn.prop('disabled', true);
    qrScanner.show();

    setTimeout(function () {
 
      $.ajax({
        type: 'POST',
        url: '/detect',
        data: form_data,
        contentType: false,
        processData: false,
        headers: {
          "X-CSRFToken": getCSRFToken() 
        },
        complete: function () {
          $btn.removeAttr('disabled');
          $btn.html('Detect');
          qrScanner.hide();
        },
        dataType: 'json'
      }).done(async function (data) {
        const datas = await data
        swal(datas.label, 'Probalitas : ' + datas.probabilities, '' + datas.value);
      }).fail(function (data) {
        console.error(data);
      });
    }, 1000);
  });
});
