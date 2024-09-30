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
    echo "<p>Date of Birth: " . $dob . "</p>";
    echo "<p>Age: " . $age . "</p>";
    echo "<p>Role: " . $role . "</p>";
    echo "</div>";
}

// Function to display Work Experience
function workExperience($teamMembers, $memberNumber) {
    $experienceName = $teamMembers[$memberNumber]['experience name'];
    $location = $teamMembers[$memberNumber]['experience location'];
    $year = $teamMembers[$memberNumber]['year'];
    $description = $teamMembers[$memberNumber]['description of the role'];
    $achievements = $teamMembers[$memberNumber]['achievements'];

    echo '<div class="work-experience">';
    echo '<h3>' . $experienceName . ' at ' . $location . '</h3>';
    echo '<p>' . $year . '</p>';
    echo '<p>' . $description . '</p>';
    echo '<h4>Achievements:</h4>';
    echo '<ul>';
    foreach ($achievements as $achievement) {
        echo '<li>' . $achievement . '</li>';
    }
    echo '</ul>';
    echo '</div>';
}
foreach ($teamMembers as $index => $memberInfo) { 
    workExperience($teamMembers, $index);
}
?>

