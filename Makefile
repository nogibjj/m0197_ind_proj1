install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv --cov=main --cov=tests test_*.py
	python -m pytest -vv --cov=main --cov=tests tests/*.py
	python -m pytest --nbval $(src/*.ipynb)

format:	
	black *.py 

lint:
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py src/*.py
	#ruff linting is 10-100X faster than pylint
	ruff check *.py src/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint
		
all: install lint test format
