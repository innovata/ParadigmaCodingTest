# Paradigma-Digital python-challenge






## Installation.

1. Download the package.

- git https://github.com/innovata/pychall.git

Or,

- Download ZIP file and unpacked it on your local computer. (https://github.com/innovata/pychall)

2. Move into the package-folder and Make a virtualenv of Python3.7

python3 -m virtualenv env

3. Install required packages.

pip install -r requirements.txt

4. Instal PostgreSQL(v11).


## Setup Environment.

1. PostgreSQL setup

- Run PostgreSQL server.

2. Terminal Envrionment setup

- 2-1. PostgreSQL server's User name

export PSQL_USER=user_name

- 2-2 PostgreSQL server URI

export PSQL_URI=postgresql://user_name:@127.0.0.1:5432


#### * Every terminal environment variables should be saved in each any new terminal.


## Run & Test.

1. Prepare Database.
- Create 2 Databases and 2 Tables

python run.py

2. Launch 3 flasks in 3 each terminals.

- 2.1 place-microservice

export FLASK_ENV=development
export FLASK_APP=pychall/places/app
export FLASK_RUN_PORT=8081

flask run

- 2.2 peopel-microservice

export FLASK_ENV=development
export FLASK_APP=pychall/people/app
export FLASK_RUN_PORT=8082

flask run

- 2.3 got-microservice

export FLASK_ENV=development

export FLASK_APP=pychall/got/app

export FLASK_RUN_PORT=8083

flask run

3. Test APIs in 2 ways.

- 3-1. Use a web-browser

http://127.0.0.1:8083/v1/places/

http://127.0.0.1:8083/v1/places/1

http://127.0.0.1:8083/spec

- 3-2. Use pychall/test/client.py

python test.py

And then Enter,

True

## Unit Test.

1. Way to test pychall.psql module

Shut down all flask apps.

python test.py

(Enter) False
