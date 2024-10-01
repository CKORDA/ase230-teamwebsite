<?php
  function memberAge($dateOfBirth){
    $DOB = new DateTime($dateOfBirth);
    $todayDate = new DateTime();
    $age = $todayDate ->diff($DOB)->y;
    return $age;
  }

  function memberInfo($teamMembers, $memberNumber){
    $name = $teamMembers['name'];
    $role = $teamMembers['role'];
    $link = $teamMembers['link'];
    $image = $teamMembers['image'];
    echo '<div class="member-card">';
    echo '<img src="' . $image . '" alt="' . $name . '">';
    echo '<h2>' . $name . '</h2>';
    echo '<p>role ' . $role . '</p>';
    echo '<p>Link ' . $link . '</p>';
    echo '</div>';
  }
foreach ($teamMembers as $index => $memberInfo) {
    memberInfo($teamMembers, $index);
}
    
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
