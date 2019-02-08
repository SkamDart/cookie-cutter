.PHONY: clean coverage install lint test unit_test

SRC_DIR=project_name
TEST_DIR=tests
TEST_ENV=test

test:
	ENV=$(TEST_ENV) pytest --cov=$(SRC_DIR) $(TEST_DIR)/

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name 'flake8.log' -delete
	find . -name 'htmlcov' -delete

coverage:
	coverage html --fail-under=90

install:
	pip install -r requirements-dev.txt --process-dependency-links

lint:
	flake8 $(SRC_DIR)

run:
	gunicorn --config gunicorn_config.py wsgi:app

unit_test:
	ENV=$(TEST_ENV) pytest --cov=$(SRC_DIR) $(TEST_DIR)/unit

functional:
	ENV=$(TEST_ENV) pytest --cov=$(SRC_DIR) $(TEST_DIR)/functional

