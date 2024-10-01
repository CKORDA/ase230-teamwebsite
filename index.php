<?php
// Define an array for member information
$teamMembers = [
    [
        "name" => "Cheyenne Korda",
        "role" => "Cyber Security Analyst",
        // "link" => "http://localhost/ase230/02/CHEYENNE_KORDA.php",
        "image" => "assets/images/profileCK.jpg",
        "dob" => "2004-03-14"
    ],
    [
        "name" => "Ramatoulaye Signate",
        "role" => "Software Developer",
        // "link" => "http://localhost/nku/ase230/Resume/01/Rama_SIGNATE.php",
        "image" => "assets/images/profile.jpg",
        "dob" => "2000-11-21"
    ],
    [
        "name" => "Evan McQueary",
        "role" => "Cybersecurity Analyst",
        // "link" => "http://localhost/Assignment_1/Evan_McQueary.php",
        "image" => "assets/images/ProfileEM.jpg",
        "dob" => "--"
    ],
    [
        "name" => "Monju Tanakajima",
        "role" => "Cybersecurity Specialist",
        "link" => "",
        "image" => "assets/images/ProfileMT.jpg",
        "dob" => "2004-02-07"
    ]
];

function memberAge($dateofBirth) {
    $DOB = new DateTime($dateofBirth);
    $todayDate = new DateTime();
    $age = $todayDate->diff($DOB)->y;
    return $age;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Our amazing team</title>

    <!-- Meta -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Your name's resume">
    <meta name="author" content="Your name">
    <link rel="shortcut icon" href="favicon.ico">

    <!-- Google Font -->
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900" rel="stylesheet">

    <!-- FontAwesome JS-->
    <script defer src="assets/fontawesome/js/all.min.js"></script>

    <!-- Theme CSS -->
    <link id="theme-style" rel="stylesheet" href="assets/css/pillar-1.css">
</head>

<body>
<article class="resume-wrapper text-center position-relative">
    <div class="resume-wrapper-inner mx-auto text-start bg-white shadow-lg">
        <h1 class="py-4 text-center">OUR AMAZING TEAM</h1>
    </div>
</article>

<!-- Move member display section here -->
<section class="team-section text-center pt-4">
    <div class="container">
        <h2 class="text-center mb-4">Meet the Team</h2>
        <?php
        $index = 0;
        // Loop through each member and call the displayCard function to display their information
        foreach ($teamMembers as $member) {
            displayCard($member);
            $index++;
        } ?>
    </div>
</section>

<footer class="footer text-center pt-2 pb-5">
    <!--/* This template is free as long as you keep the footer attribution link. If you'd like to use the template without the attribution link, you can buy the commercial license via our website: themes.3rdwavemedia.com Thank you for your support. :) */-->
    <small class="copyright">Designed with <span class="sr-only">love</span><i class="fas fa-heart"></i> by Cheyenne, Ramatoulaye, Monju, and Evan</small>
</footer>
</body>
</html>
