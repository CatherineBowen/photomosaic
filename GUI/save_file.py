#!/usr/bin/env python3

import cgi, os
from cgitb import enable
enable()
from cgi import FieldStorage
from hashlib import sha256
from time import time
from shelve import open
from PIL import Image
from http.cookies import SimpleCookie

sid = sha256(repr(time()).encode()).hexdigest()

cookie = SimpleCookie()
cookie['token'] = sid
cookie['mode'] = 'upload'
print(cookie)

output = ''
status = False
form_data = FieldStorage()

if len(form_data) != 0:
        # Get filename here.
        fileitem = form_data['filename']

        # Test if the file was uploaded
        if fileitem.filename:
                # strip leading path from file name to avoid 
                # directory traversal attacks
                # fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
                # sid = sha256(repr(time()).encode()).hexdigest()
                mypath = '/var/www/html/tmp_fold/usr_' + sid
                if not os.path.isdir(mypath):
                        os.makedirs(mypath)
                        os.chmod(mypath, 0o777)
                # open(mypath + '/' + fn, 'wb').write(fileitem.file.read())
                img = Image.open(fileitem.file)
                img.convert('RGB')
                img.save(mypath + '/profile.png')
                os.chmod(mypath + '/profile.png',0o777)
                status = True

else:
        output = 'Please upload a file'
        status = False

if status:
        print("Location:http://143.239.81.202/cgi-bin/resize.py")
print('Content-Type: text/html')
print()

print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<!--
Design by TEMPLATED
<!--
Design by TEMPLATED
http://templated.co
Released for free under the Creative Commons Attribution License

Name       : RedMarket
Description: A two-column, fixed-width design with dark color scheme.
Version    : 1.0
Released   : 20140101

-->
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Webpage</title>
<meta name="keywords" content="" />
<meta name="description" content="" />
<link href="http://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300,400,600,700,900" rel="stylesheet" />
<link href="../default.css" rel="stylesheet" type="text/css" media="all" />
<link href="../fonts.css" rel="stylesheet" type="text/css" media="all" />

<!--[if IE 6]><link href="default_ie6.css" rel="stylesheet" type="text/css" /><![endif]-->

<script src="../back_to_top.js" type="text/javascript"></script>
</head>

<body>
<a href="#" class="back-to-top"><br>Back to Top</a>
<div id="header-wrapper">
        <div id="header" class="container">
                <div id="logo">
                                            <h1 style=" color: white;"> <img src="../jigsaw.png" alt="jigsaw piece" height="25" width="25">  MosaicMake</h1>
                </div>
        </div>
</div>
<div id='wrapper' style='padding: 1em; margin-left: auto; margin-right: auto;'>
        <div id='upload' class="container">
                <form enctype="multipart/form-data" action="save_file.py" method="post">
                        <p>Upload a photo:</p><br />
                        <input id="file" type="file" name="filename" />
                        <br>
                        <p>%s</p>
                        <br>
                        <p><input id="submit" type="submit" value="Upload" /></p>
                </form>
        </div>
</div>
</div>
<div id="copyright" class="container">
        <p>&copy; Untitled. All rights reserved. | released under the <a href="http://templated.co/license">Creative Commons Attribution</a> license | Design by <a href="http://templated.co" rel="nofollow">TEMPLATED</a>.</p>
</div>
</body>
</html>""" % (output))
