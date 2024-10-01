<?php

function memberAge($dateofBirth) {
    $DOB = new DateTime($dateofBirth);
    $todayDate = new DateTime();
    $age = $todayDate->diff($DOB)->y;
    return $age;
}

function displayCard($member) {
    // Outputs the HTML structure for a team member
    echo '<header class="resume-header mt-4 pt-4 pt-md-0">';
    echo '    <div class="row">';
    echo '        <div class="col-block col-md-auto resume-picture-holder text-center text-md-start">';
    echo '            <img class="picture" src="' . htmlspecialchars($member['image']) . '" alt="' . htmlspecialchars($member['name']) . '" width="150" height="220">';
    echo '        </div><!--//col-->';
    echo '        <div class="col">';
    echo '            <div class="row p-4 justify-content-start">'; // Change to justify-content-start for left alignment
    echo '                <div class="primary-info col-auto">';
    echo '                    <h1 class="name mt-0 mb-1 text-white text-uppercase">' . htmlspecialchars($member['name']) . '</h1>';
    echo '                    <div class="title mb-3">' . htmlspecialchars($member['role']) . '</div>';
    echo '                    <p class="mb-0">Age: ' . memberAge($member['dob']) . '</p>'; // Added age display
    echo '                    <a href="detail.php?index=' . array_search($member, $GLOBALS['teamMembers']) . '" class="btn btn-secondary">See full profile</a>';
    echo '                </div><!--//primary-info-->';
    echo '                <div class="secondary-info col-auto mt-2">';
    echo '                </div><!--//secondary-info-->';
    echo '            </div><!--//row-->';
    echo '        </div><!--//col-->';
    echo '    </div><!--//row-->';
    echo '</header>';
    
  function workExperience($teamMembers, $memberNumber) {
    $experienceName = $teamMembers[$memberNumber]['experience name'];
    $location = $teamMembers[$memberNumber]['experience location'];
    $year = $teamMembers[$memberNumber]['year'];
    $description = $teamMembers[$memberNumber]['description of the role'];

    echo '<div class="work-experience">';
    echo '<h3>' . $experienceName . ' at ' . $location . '</h3>';
    echo '<p>' . $year . '</p>';
    echo '<p>' . $description . '</p>';
    echo '</div>';

}
?>
