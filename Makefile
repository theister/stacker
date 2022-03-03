.PHONY: build lint test-unit test-functional test build-wheel compile-requirements

build:
	docker build -t remind101/stacker .

lint:
	flake8 --ignore E402,W503,W504,W605,N818 --exclude stacker/tests/ stacker
	flake8 --ignore E402,N802,W605,N818 stacker/tests # ignore setUp naming

test-unit: clean
	pytest

clean:
	rm -rf .egg stacker.egg-info build dist

test-functional:
	cd tests && bats test_suite

# General testing target for most development.
test: lint test-unit

apidocs:
	sphinx-apidoc --force -o docs/api stacker

build-wheel: clean test
	pip install -U build
	python -m build --wheel

compile-requirements:
	pip install -U pip-tools
	pip-compile requirements.in test-requirements.in -o requirements.txt
	pip install -r requirements.txt
