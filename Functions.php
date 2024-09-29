<?php
// Function to calculate age based on date of birth
function calculateAge($dob) {
    $dob = new DateTime($dob);
    $currentDate = new DateTime();
    $age = $currentDate->diff($dob);
    return $age->y; // Return the years portion of the difference
}

// Function to display each member's information in a card
function displayCard($memberInfo) {
    $name = $memberInfo['name'];
    $dob = $memberInfo['dob'];
    $role = $memberInfo['role'];
    $age = calculateAge($dob);  // Use the age calculation function

    // Generate the HTML for the card using PHP
    echo "<div class='card'>";
    echo "<h2>" . $name . "</h2>";
    echo "<p>Age: " . $age . "</p>";
    echo "<p>Role: " . $role . "</p>";
    echo "</div>";
}
?>

