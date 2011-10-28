Classzy
=======

Nyan nyan nyan (>")>

Pre-requisites
--------------

- Install Github
- Install Python
- Install Django

To Import Everything
--------------------
	git clone git@github.com:imkevinxu/Classzy.git
	
To Run Locally
--------------
	cd Classzy
	python manage.py syncdb
	python manage.py runserver
	
- **Change TEMPLATE_DIRS path to your absolute path**
- Go to http://localhost:8000/
	
To Push
-------
	git remote add deploy ec2-user@classzy.projectnyan.com:~/classzy/classzy.git (only do once)
	git push origin master && git push deploy master

To Access Server
----------------
Get classzy.pem

	ssh-add classzy.pem (must do everytime)
	ssh ec2-user@classzy.projectnyan.com
	
Or...

	ssh -i classzy.pem ec2-user@classzy.projectnyan.com

While Inside Server
-------------------
- work - enters project folder
- restart - restarts the server