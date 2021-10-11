$(document).ready(function () {
    // Init
    $('.image-section1').hide();
    $('.loader1').hide();
    $('#result1').hide();

    // Upload Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview1').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview1').hide();
                $('#imagePreview1').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload1").change(function () {
        $('.image-section1').show();
        $('#btn-predict1').fadeIn();
        $('#result1').text('');
        $('#result1').hide();
        readURL(this);
    });

    // Predict
    $('#btn-predict1').click(function () {
        var form_data = new FormData($('#upload-file1')[0]);
        var cropName = $('#crop-choose1').find(":selected").text();
        var url='';
        // Show loading animation
        if(cropName=="मक्का"){
          url= '/maize_disease';
        }
        if(cropName=="चावल"){
          url= '/rice_disease';
        }
        $(this).hide();
        $('.loader1').show();

        // Make prediction by calling api /predict
        $.ajax{
            type: 'POST',
            url: url,
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader1').hide();
                $('#result1').fadeIn(300);
                $('#result1').text(' Result:  ' + data);
                console.log('Success!');
            },
        });
    });

});
