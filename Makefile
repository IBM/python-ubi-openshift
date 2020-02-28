init:
	pip install pipenv --upgrade
	pipenv install
	pipenv install --dev
test:
	# This runs all of the tests, on both Python 2 and Python 3.
	detox
ci:
	pipenv run pytest -v

