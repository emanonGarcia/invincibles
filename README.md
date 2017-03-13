#The Invincibles
It goes without saying that during the 2003-04 season the Arsenal FC were the kings of English football. During this period, they were able to compete in 49 League matches while going undefeated. A feat that has them forever known as The Invincibles.  In what follows a database, invincibles0304, is constructed containing a squad table. The table contains the player stats, for those that contributed the most to the campaign, organized by their kit (jersey) number.

##Getting Started
After downloading and unzipping, the local directory will contain 4 files. invincibles.csv contain the organized data with which the database is constructed. data_load.py constructs the database and player.py is an auxiliary script to the main the_invicibles_py.

###Prerequisites
This is a python3 specific script. Download by visiting [Python](https://www.python.org/downloads/) or if arleady have python and need to install the version 3 on a mac
```
$ pip install python3
```
[Postgres](http://postgresapp.com/)
[Postico](https://eggerapps.at/postico/)
Update PATH Environment Variable
```
$ export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.6/bin/
```

Install [Psycopg2](https://www.tunnelsup.com/setting-up-postgres-on-mac-osx/) Module
```
$ pip3 install psycopg2
```

###Installing
After install in the prereq, change the dbname and user in data_load.py to fit your needs and run the_invicibles_py from the command line.

##Author
* **Luis Garcia** - *Initial work* - [emanonGarcia](https://www.github.com/emanongarcia)
