<?php
include 'Functions.php';

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
        "dob" => "--"
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
    <title>Our Amazing Team</title>
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

        <!-- PHP Loop to display each team member card -->
        <?php
        $index = 0;
        foreach ($teamMembers as $member) { ?>
            <header class="resume-header mt-4 pt-4 pt-md-0">
                <div class="row">
                    <!-- Profile Picture -->
                    <div class="col-block col-md-auto resume-picture-holder text-center text-md-start">
                        <img class="picture" src="<?php echo $member['image']; ?>" alt="<?php echo $member['name']; ?>" width="150" height="220">
                    </div>
                    
                    <!-- Member Information -->
                    <div class="col">
                        <div class="row p-4 justify-content-center justify-content-md-between">
                            <div class="primary-info col-auto">
                                <h1 class="name mt-0 mb-1 text-white text-uppercase"><?php echo $member['name']; ?></h1>
                                <div class="title mb-3"><?php echo $member['role']; ?></div>

                                <!-- Link to detail page -->
                                <a href="detail.php?index=<?php echo $index; ?>" class="btn btn-secondary">See full profile</a>
                            </div>
                        </div>
                    </div>
                </div>
            </header>
        <?php 
            $index++;
        } ?>
    </div>
</article>

<!-- Footer Section -->
<footer class="footer text-center pt-2 pb-5">
    <small class="copyright">Designed with <i class="fas fa-heart"></i> by Cheyenne, Ramatoulaye, Monju, and Evan</small>
</footer>

</body>
</html>
