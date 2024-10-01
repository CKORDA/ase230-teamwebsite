<?php
// Include the functions.php file
include 'functions.php'; 

// Define an array for member information
$teamMembers = [
    [
        "name" => "Cheyenne Korda",
        "role" => "Cyber Security Analyst",
        "image" => "assets/images/profileCK.jpg",
        "dob" => "2004-03-14"
    ],
    [
        "name" => "Ramatoulaye Signate",
        "role" => "Software Developer",
        "image" => "assets/images/profile.jpg",
        "dob" => "2000-11-21"
    ],
    [
        "name" => "Evan McQueary",
        "role" => "Cybersecurity Analyst",
        "image" => "assets/images/ProfileEM.jpg",
        "dob" => "2003-07-01"
    ],
    [
        "name" => "Monju Tanakajima",
        "role" => "Cybersecurity Specialist",
        "image" => "assets/images/ProfileMT.jpg",
        "dob" => "2004-02-07"
    ]
];
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
    
    <!-- Custom CSS -->
    <style>
        .primary-info {
            text-align: left; /* Ensures text is left-aligned */
        }

        .title {
            margin-bottom: 0.5rem; /* Adjusts the margin for better spacing */
        }
        }
    </style>
</head>

<body>
<article class="resume-wrapper text-center position-relative">
    <div class="resume-wrapper-inner mx-auto text-start bg-white shadow-lg">
        <h1 class="py-4 text-center">OUR AMAZING TEAM</h1>
    </div>
</article>

<!-- Member display section -->
<section class="team-section text-center pt-4">
    <div class="container">
        <h2 class="text-center mb-4">Meet the Team</h2>
        <?php
        // Loop through each member and call the displayCard function to display their information
        foreach ($teamMembers as $member) {
            displayCard($member);
        }
        ?>
    </div>
</section>

<footer class="footer text-center pt-2 pb-5">
    <small class="copyright">Designed with <span class="sr-only">love</span><i class="fas fa-heart"></i> by Cheyenne, Ramatoulaye, Monju, and Evan</small>
</footer>
</body>
</html>
