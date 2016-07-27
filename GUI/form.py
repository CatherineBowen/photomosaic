#!/usr/bin/env python3

from cgitb import enable
enable()

print("Content-Type: text/html")
print()
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<!--
Design by TEMPLATED
http://templated.co
Released for free under the Creative Commons Attribution License
Name       : RedMarket 
Description: A two-column, fixed-width design with dark color scheme.
Version    : 1.0
Released   : 20140101
-->
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<style>
			#myTags > * {
				color: #CC0000;
			}
		</style>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>MosaicMake</title>
		<meta name="keywords" content="" />
		<meta name="description" content="" />
		<link href="http://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300,400,600,700,900" rel="stylesheet" />
		<link href="../default.css" rel="stylesheet" type="text/css" media="all" />
		<link href="../fonts.css" rel="stylesheet" type="text/css" media="all" />
		<link rel="icon" href="../jigsaw.png">
                <!-- tag stuff -->
		<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js" type="text/javascript" charset="utf-8"></script>
		<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js" type="text/javascript" charset="utf-8"></script>
		<script src="http://aehlke.github.io/tag-it/js/tag-it.js" type="text/javascript" charset="utf-8"></script>
		<link rel="stylesheet" type="text/css" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1/themes/flick/jquery-ui.css">
		<link href="http://aehlke.github.io/tag-it/css/jquery.tagit.css" rel="stylesheet" type="text/css">
		<!--[if IE 6]><link href="default_ie6.css" rel="stylesheet" type="text/css" /><![endif]-->
		<script src="../back_to_top.js" type="text/javascript"></script>
		<script type="text/javascript">
				
			function fillSpan(value){
				var span = document.getElementById('span');
				var option = value;
				if (option === '20' || option === '40') {
					span.innerHTML = "Your mosaic will be ready quickly but might not be as good as you'd like!"

				} else if (option === '50'){
					span.innerHTML = "This is the recommended number of photos for quality and speed!"
				} else if (option === '60' || option === '70'){
					span.innerHTML = "Your mosaic will be high quality but might take a while to load!"
				} else {
					span.innerHTML = ""
				}
			}
		</script>
	</head>
	<body>
		<a href="#" class="back-to-top"><br>Back to Top</a>
		<div id="header-wrapper" style="height: 35%;">
			<div id="header" class="container">
				<div id="logo">
					<h1 style=" color: white;"> <img src="../jigsaw.png" alt="jigsaw piece" height="25" width="25">  MosaicMake</h1>
				</div>	
				<div id="menu">
					<ul>
						<li class="active"><a href="http://143.239.81.202" accesskey="1" title="">Home</a></li>
					</ul>
				</div>
			</div>
		</div>
               	<script type="text/javascript">
    $(document).ready(function() {
        $("#myTags").tagit();
    });
		</script>
		<div id="wrapper" style='padding-top: 1em; padding-bottom: 2em;'>
			<br>
			<div class="container" style='border: 1px solid black; border-radius: .5em; padding: 1em; font-size: 17px;'>
				<form action="loading.py" method="get">
					<label for="photos">Choose the number of photos in your mosaic:  </label>
					<select name="photos" onchange='fillSpan(this.value)' required>
					<option value="20">20x20 (400)</option>
    					<option value="40">40x40 (1600)</option>
    					<option value="50">50x50 (2500)</option>
    					<option value="60">60x60 (3600)</option>
    					<option value="70">70x70 (4900)</option>
					</select><br />
					<span id='span' style='display: inline-block; padding-top: .5em;'></span>
					<br><br><label for="myTags" style='padding-bottom: .5em;'>Choose by tag which type of images will make up your mosaic:  </label>
					<br><br />
					<ul id="myTags">
    	                                	<!-- Existing list items will be pre-added to the tags -->
    	                                	<li>Sea</li>
    	                                	<li>Flower</li>
		                        </ul>
					<label for="opacity">Choose the level of definition: </label>
					<br><br />
					<input type="range" id="opacity" name="opacity" min="0" max="10">
					<br><br />
		                        <input type="submit" value="MosaicMake"><br><br>
				</form>
			</div>
		</div>
		<div id="copyright" class="container">
			<p>&copy; MosaicMake. All rights reserved. | released under the <a href="http://templated.co/license">Creative Commons Attribution</a> license | Design by <a href="http://templated.co" rel="nofollow">TEMPLATED</a>.</p>
		</div>
	</body>
</html>
""")
