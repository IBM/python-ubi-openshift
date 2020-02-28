init:
	pip install pipenv --upgrade
	pipenv install --dev
	pipenv install
test:
    pipenv shell
	pipenv run pytest