# bertelsmann

1. Clone the repo: 
git clone https://github.com/olivetom/bertelsmann.git

2. Check out the repo if previously cloned
Go into it and make sure you have the latest.

cd bertelesmann
git pull origin master

3. Set up the Python environment
Run

pipenv sync --dev

From now on, precede commands with pipenv run to make sure they use the correct environment.


4. Kick off a command
Before you get started, please run a command that will confirm everything is all right.

git pull
cd Lesson3
pipenv run python 001_and_perceptron.py
cd ..

5. Specify python version using:

pipenv --python /usr/bin/python3.6