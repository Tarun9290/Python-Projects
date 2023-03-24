<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  // Get the email address from the form
  $email = $_POST['email'];

  // Check if the email address is valid
  if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $error = 'Invalid email address';
  } else {
    // Generate a random password reset token
    $token = bin2hex(random_bytes(32));

    // Store the token in the database with the corresponding email address
    // You should replace this with your own database code
    $db = new mysqli('localhost', 'username', 'password', 'database_name');
    $stmt = $db->prepare("INSERT INTO password_reset_tokens (email, token) VALUES (?, ?)");
    $stmt->bind_param("ss", $email, $token);
    $stmt->execute();

    // Send the password reset link to the user's email address
    // You should replace this with your own email sending code
    $subject = 'Password Reset';
    $message = 'Please click on the following link to reset your password: http://localhost/reset_password.php?token=' . $token;
    $headers = 'From: webmaster@example.com';
    mail($email, $subject, $message, $headers);

    // Show a success message
    $success = 'A password reset link has been sent to your email address';
  }
}
?>
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Forgot Password</title>
  <link rel="stylesheet" href="forgot_password.css">
</head>
<body>
  <div class="container">
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
      <h1>Forgot Password</h1>
      <p>Please enter your email address below to receive a password reset link.</p>
      <label for="email"><b>Email</b></label>
      <input type="email" placeholder="Enter Email" name="email" required>
      <button type="submit">Submit</button>
      <?php if (isset($error)) { ?>
        <div class="error"><?php echo $error; ?></div>
      <?php } ?>
      <?php if (isset($success)) { ?>
        <div class="success"><?php echo $success; ?></div>
      <?php } ?>
    </form>
  </div>
  <script src="forgot_password.js"></script>
</body>
</html>
