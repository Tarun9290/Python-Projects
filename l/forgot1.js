$(document).ready(function() {
    $("#forgot-pass-form").submit(function(e) {
      e.preventDefault(); // Prevent the form from submitting via HTTP
  
      var formData = $(this).serialize(); // Serialize the form data
  
      $.ajax({
        url: "forgot_pass.php", // The URL of the PHP script to handle the form submission
        type: "POST", // HTTP method
        data: formData, // Form data
        dataType: "json", // The type of data to expect back from the server
        success: function(data) {
          // Handle the response from the server
          if (data.status === "success") {
            // Display a success message
            $("#forgot-pass-msg").removeClass("error").addClass("success").text(data.message);
          } else {
            // Display an error message
            $("#forgot-pass-msg").removeClass("success").addClass("error").text(data.message);
          }
        },
        error: function(jqXHR, textStatus, errorThrown) {
          // Handle errors
          console.log(textStatus, errorThrown);
        }
      });
    });
  });
  