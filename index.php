<?php
// Define an array for member information
$teamMembers = [
    [
        "name" => "Cheyenne Korda",
        "role" => "Cyber Security Analyst",
      //  "link" => "http://localhost/ase230/02/CHEYENNE_KORDA.php",
        "image" => "assets/images/profileCK.jpg"
    ],
    [
        "name" => "Ramatoulaye signate",
        "role" => "software developer",
       // "link" => "http://localhost/nku/ase230/Resume/01/Rama_SIGNATE.php",
        "image" => "assets/images/profile.jpg"
    ],
    [
        "name" => "Evan McQueary",
        "role" => "Cybersecurity Analyst",
        // "link" => "http://localhost/Assignment_1/Evan_McQueary.php",
        "image" => "assets/images/ProfileEM.jpg"
    ],
    [
        "name" => "Monju Tanakajima",
        "role" => "Cybersecurity Specialist",
        "link" => "",
        "image" => "assets/images/ProfileMT.jpg"  
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
</head>

<body>
<article class="resume-wrapper text-center position-relative">
    <div class="resume-wrapper-inner mx-auto text-start bg-white shadow-lg">
        <h1 class="py-4 text-center">OUR AMAZING TEAM</h1>


        <?php
        $index=0;
         foreach ($teamMembers as $member) { ?>
            <header class="resume-header mt-4 pt-4 pt-md-0">
                <div class="row">
                    <div class="col-block col-md-auto resume-picture-holder text-center text-md-start">
                    <img class="picture" src="<?php echo $member['image']; ?>" alt="" width="150" height= "220">
                    </div><!--//col-->
                    <div class="col">
                        <div class="row p-4 justify-content-center justify-content-md-between">
                            <div class="primary-info col-auto">
                                <h1 class="name mt-0 mb-1 text-white text-uppercase text-uppercase"><?php echo $member['name']; ?></h1>
                                <div class="title mb-3"><?php echo $member['role']; ?></div>
                                <a href="detail.php?index=<?php echo $index; ?>" class="btn btn-secondary">See full profile</a>
                            </div><!--//primary-info-->
                            <div class="secondary-info col-auto mt-2">
                            </div><!--//secondary-info-->
                        </div><!--//row-->

                    </div><!--//col-->
                </div><!--//row-->
            </header>
            
        <?php 
        $index++;
    } ?>

    </div>
</article>

<footer class="footer text-center pt-2 pb-5">
    <!--/* This template is free as long as you keep the footer attribution link. If you'd like to use the template without the attribution link, you can buy the commercial license via our website: themes.3rdwavemedia.com Thank you for your support. :) */-->
    <small class="copyright">Designed with <span class="sr-only">love</span><i class="fas fa-heart"></i> by Cheyenne, Ramatoulaye, Monju, and Evan</small>
</footer>

