<?php
// Function to calculate age based on date of birth
function calculateAge($dob) {
    $dob = new DateTime($dob);
    $currentDate = new DateTime();
    $age = $currentDate->diff($dob);
    return $age->y; // Return the years portion of the difference
}
?>
