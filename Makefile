build:
	bash ./scripts/ubuntu/build.sh
SHELL := /bin/bash

.PHONY: install install-dev run test format lint docker-build docker-test docker-curl-test
lint:
	bash ./scripts/ubuntu/lint.sh

install:
	./scripts/ubuntu/install.sh

install-dev:
	./scripts/ubuntu/install-dev.sh

test:
	./scripts/ubuntu/test.sh

format:
	bash ./scripts/ubuntu/format.sh

run:
	./scripts/ubuntu/run.sh

docker-build:
	docker build -f docker/build.Dockerfile -t flask-template-build .

docker-test:
	docker build -f docker/test.Dockerfile -t flask-template-test .
	docker run --rm flask-template-test

docker-curl-test:
	./scripts/ubuntu/docker-curl-test.sh
