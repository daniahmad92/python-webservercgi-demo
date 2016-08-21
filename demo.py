#!C:\Python27\python

htmlstring= '''
<html>
<head>
    <title>Demo CGI</title>
</head>
<body>
<h1>Salam Kenal</h1>
<p>Saya Dadan ahmad dani</p>
</body>
</html>
'''

print ("Content-type: text/html\r\n\r\n")
print (htmlstring);
