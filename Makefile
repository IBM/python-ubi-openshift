init:
	pip install pipenv --upgrade
	pipenv install
	pipenv install --dev
test:
	# tox runs all of the tests in parallel
	# see https://tox.readthedocs.io/en/latest/ 
	tox -p
ci:
	pipenv run pytest -v
