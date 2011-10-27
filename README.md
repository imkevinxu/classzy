Classzy
=======

Nyan nyan nyan

Initial Steps
-------------
	git clone git@github.com:imkevinxu/Classzy.git
	cd Classzy
	python manage.py syncdb
	
- Change TEMPLATE_DIRS path to your absolute path

To Run
------
	python runserver
	Go to http://localhost:8000/

Steps to SSH to server
----------------------

- Obtain classzy.pem

Two ways to SSH

- Store classzy.pem into location
	ssh-add classzy.pem
	ssh ec2-user@classzy.projectnyan.com
	
- Or...
	ssh -i classzy.pem ec2-user@classzy.projectnyan.com