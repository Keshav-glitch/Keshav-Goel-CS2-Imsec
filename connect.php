<?php
session_start();

// Get user input from form
$username = $_POST['email'];
$password = $_POST['password'];

// Validate inputs
if (empty($username) || empty($password)) {
    die("Email and password are required.");
}

// Database Connection
$conn = new mysqli('localhost', 'root', '', 'login');
if ($conn->connect_error) {
    die('Connection Failed: ' . $conn->connect_error);
}

// Prepare the SQL statement to fetch the user record
$stmt = $conn->prepare("SELECT * FROM user WHERE email = ?");
if ($stmt) {
    // Bind the parameters
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        // Fetch user record
        $row = $result->fetch_assoc();
        
        // Verify the password
        if (password_verify($password, $row['password'])) {
            // Password is correct, login successful
            $_SESSION['user_id'] = $row['id'];  // You can store other details as needed
            echo "Login successful!";
            // Redirect to a protected page (e.g., dashboard)
            header("Location: dashboard.php");
        } else {
            echo "Invalid password.";
        }
    } else {
        echo "No user found with that email.";
    }

    // Close the statement
    $stmt->close();
} else {
    echo "Error preparing query: " . $conn->error;
}

// Close the connection
$conn->close();
?>
