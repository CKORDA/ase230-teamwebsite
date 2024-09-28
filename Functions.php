<?php
// Function to calculate age based on date of birth
function calculateAge($dob) {
    $dob = new DateTime($dob);
    $currentDate = new DateTime();
    $age = $currentDate->diff($dob);
    return $age->y; // Return the years portion of the difference
}

// Function to generate a member card for the index page
function generateMemberCard($member, $index) {
    $age = calculateAge($member['dob']);
    $html = "<div class='member-card'>";
    $html .= "<h2>{$member['name']}</h2>";
    $html .= "<p>Member Age: {$age} years</p>";
    $html .= "<a href='detail.php?index={$index}'>View Details</a>";
    $html .= "</div>";
    return $html;
}

// Function to generate a work experience item for the detail page
function generateWorkExperience($experience) {
    $html = "<div class='work-experience'>";
    $html .= "<h3>{$experience['position']}</h3>";
    $html .= "<p>Company: {$experience['company']}</p>";
    $html .= "<p>Employment Period: {$experience['start_date']} to {$experience['end_date']}</p>";
    $html .= "</div>";
    return $html;
}
?>
