# Delectus Video Art Website

## Getting Started

1. Install Xcode
2. Install Python
3. Install virtualenv
4. Install MAMP
5. Create a database in MySQL named "delectus-django"
6. Fill in the database with some production backup
7. Setup virtualenv in repo `virtualenv .`
8. Source virtualenv CLIs `source bin/activate`
9. Install python modules `pip install -r requirements.txt`
9. Run a django db sync `python manage.py syncdb`
10. Start the server! `python manage.py runserver`

## Forking & Contributing

1. Fork the main github repo https://github.com/cooperbattersby/delectus
2. Go to your fork and clone your repo e.g. `git clone git@github.com:<USERNAME>/delectus.git`
3. Follow "Getting Started" if you're setting up for the first time.
4. Make some code changes, and commit everything `git add .; git commit -a -m "<YOUR MESSAGE HERE>"`
5. Make sure your changes are in sync with the master remote repo
	````
	git add remote upstream git@github.com:cooperbattersby/delectus.git
	git pull upstream master
	````
5. Push your changes to your local repo `git push origin master`

## Deploying to the web via Heroku

1. Set up a heroku account
2. Install Heroku Toolbelt
3. Login to your heroku account `heroku login`
4. Create a new app on heroku `heroku apps:create delectus-<username>`
5. Remove the POST
5. Add the "ClearDB MySQL Database Ignite" addon `heroku addons:add cleardb`
6. Push to the heroku remote `git push heroku master`
7. Sync the db `heroku run python manage.py syncdb`
8. See your website `heroku open`
9. Check for any issues `heroku logs`