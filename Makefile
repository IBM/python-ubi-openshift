
init:
	pip install pipenv --upgrade
	pipenv install --dev
test:
	# This runs all of the tests, on both Python 2 and Python 3.
	detox
ci:
	pipenv run pytest

flake8:
	pipenv run flake8 --ignore=E501,F401,E128,E402,E731,F821 requests

coverage:
	pipenv run py.test --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=requests tests