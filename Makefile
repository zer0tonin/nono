# -*- mode: makefile -*-

COMPOSE = docker-compose -p nono


.PHONY: run
run:
	$(COMPOSE) build app
	$(COMPOSE) run app

.PHONY: down
down:
	$(COMPOSE) down --volumes --rmi=local


.PHONY: format
format:
	black --target-version py37 nono


.PHONY: style
style:
	black --target-version py37 --check nono


.PHONY: complexity
complexity:
	xenon --ignore "tests" --max-absolute A --max-modules A --max-average A nono


.PHONY: test
test:
	pytest -s nono


.PHONY: security-sast
security-sast:
	bandit -r nono -x test


.PHONY: type
type:
	mypy nono --ignore-missing-import
