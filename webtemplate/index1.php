


<?php 
    //echo "test";
    //if(filter_has_var(INPUT_POST,'predict30Submit')) {
        //echo "success";
    //}

    if(isset($_POST['predict30Submit'])) {
        echo "test";
        header('Location:pyTest.php');

    }
	
	if(isset($_POST['customPredict'])) {
		echo "Got predict";

		if(isset($_POST['data']) && isset($_POST['algorithm'])) {


			
			//Predict Jan2019
			//Predict Feb2019
			//Predict Mar2019
			//Predict Apr2019
			//Predict May2019
			//Predict Jun2019
			$dataset = $_POST['data'];
			$algo = $_POST['algorithm'];



			echo "GOT DATA ALSO";
		}
	}

?>


<!DOCTYPE HTML>

<html>
	<head>
		<title>Nashville Crime Prediction</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
		<script src="index.js"></script>
	</head>
	<body>

		<!-- Header -->
			<header id="header">
				<div class="logo"><a href="index.html">Nashville Crime Prediction</span></a></div>
				<a href="#menu"><span>Menu</span></a>
			</header>

		<!-- Nav -->
			<nav id="menu">
				<ul class="links">
					<li><a href="index.html">Home</a></li>
					<li><a href="generic.html">Generic</a></li>
					<li><a href="elements.html">Elements</a></li>
				</ul>
			</nav>

		<!-- Banner -->
		<!--
			Note: To show a background image, set the "data-bg" attribute below
			to the full filename of your image. This is used in each section to set
			the background image.
		-->
			<section id="banner" class="bg-img" data-bg="banner.jpg">
				<div class="inner">
					<header>
						<h1>Nashville Crime Prediction</h1>
					</header>
				</div>
				<a href="#one" class="more">Learn More</a>
			</section>

		<!-- ---------------------------------------------One---------------------------------------   -->
			<section id="one" class="wrapper post bg-img" data-bg="banner2.jpg">
				<div class="inner">
					<article class="box">
						<header>
							<h2>Create Map</h2>
						</header>
						<div class="field half first">
                            <!-- <form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>"> -->
                            <form method="POST" action="">
                                <button type="submit" name="predict30Submit"> Predict next 30 days</button>
                            </form>
						</div>
						
						<form  method="POST" id="myForm">				
							<p>Customize your prediction</p>
									<div class="dropdown">

										<select id="data" name="data">
											<option value="">- Choose Data -</option>
											<option value="twenty18">Predict January 2019</option>
											<option value="twenty17">2017 data</option>
											<option value="twenty16">2016 data</option>
										</select>
										<select id="alogrithm" name="algorithm">
											<option value="">- Choose Algorithm -</option>
											<option value="Decision Tree">Decision Tree</option>
											<option value="Backprogation">Backprogation</option>
											<option value="K_nearest">K-nearest</option>								
										</select>
									</div>
								<br>
							<ul class="actions">
								<button type="submit" name="customPredict">Run Algorithm </button>
						</form>
							</ul>
					</article>
				</div>
				<a href="#two" class="more">Learn More</a>
			</section>

		<!-- ---------------------------------------------Two--------------------------------------------- -->
			<section id="two" class="wrapper post bg-img" data-bg="banner3.jpg">
				<div class="inner">
					<article class="box">
						<header>
							<h2>About Project</h2>
						</header>
						<div class="content">
							<p>Crime is rampant throughout society, especially in a growing city like Nashville, where thousands of incidents are reported every month. Researchers have tested varying different methodologies to help police departments effectively use their limited resources to deter crime more efficiently in their respective cities. Specifically in [1, 2], researchers used neural networks and machine learning to create hotspot predictions, an NxN area where crime is more likely to happen in the coming month. With an accurate hotspot prediction tool, police can turn their focus to these specific areas to reduce crime.</p>
						</div>
						<footer>
							<a href="generic.html" class="button alt">Learn More</a>
						</footer>
					</article>
				</div>
				<a href="#three" class="more">Learn More</a>
			</section>

		<!-- Three -->
			<section id="three" class="wrapper post bg-img" data-bg="banner4.jpg">
				<div class="inner">
					<article class="box">
						<header>
							<h2>About Us</h2>
						</header>
						<div class="content">
							<p>Scelerisque enim mi curae erat ultricies lobortis donec velit in per cum consectetur purus a enim platea vestibulum lacinia et elit ante scelerisque vestibulum. At urna condimentum sed vulputate a duis in senectus ullamcorper lacus cubilia consectetur odio proin sociosqu a parturient nam ac blandit praesent aptent. Eros dignissim mus mauris a natoque ad suspendisse nulla a urna in tincidunt tristique enim arcu litora scelerisque eros suspendisse.</p>
						</div>
						<footer>
							<a href="generic.html" class="button alt">Learn More</a>
						</footer>
					</article>
				</div>
				<a href="#four" class="more">Learn More</a>
			</section>

		
		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/jquery.scrollex.min.js"></script>
			<script src="assets/js/skel.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>