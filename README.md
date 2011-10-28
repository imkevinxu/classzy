Classzy
=======

Nyan nyan nyan (>")>  
http://classzy.projectnyan.com/  
http://bit.ly/classzy

Pre-requisites
--------------

- Install Github
- Install Python
- Install Django

To Import Everything
--------------------
	git clone git@github.com:imkevinxu/Classzy.git
	
Initial Setup
--------------
	cd Classzy
	python manage.py syncdb
	git update-index --assume-unchanged settings.py
	
- **Change TEMPLATE_DIRS path to your absolute path** in settings.py


To Run Locally
--------------
	python manage.py runserver
	
- Go to http://localhost:8000/
	
To Push
-------
	git remote add deploy ssh://ec2-user@classzy.projectnyan.com/classzy/.git (only do once)
	ssh-add classzy.pem (once every time terminal is open)
	git push origin master && git push deploy master

To Access Server
----------------
Get classzy.pem

	chmod 400 classzy.pem
	ssh -i classzy.pem ec2-user@classzy.projectnyan.com

While Inside Server
-------------------
- work - enters project folder
- restart - restarts the server

Typical work cycle
------------------

- Edit files locally
- git add/commit
- git push origin master
- git push deploy master
- ssh into server and restart