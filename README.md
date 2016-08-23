Configuration for Windows (only):

1) Install WAMP server

2) Change httpd.conf for the apache server to include:

	AddHandler cgi-script .cgi .py
	Options Indexes FollowSymLinks ExecCGI
	
3) Place the python script in /cgi-bin/ directory 
and the html file in the /www/ directory

4) Configure the host and port settings and access the utility at
ip:port/powercont.html

