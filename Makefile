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
	$(COMPOSE) build format
	$(COMPOSE) run format


.PHONY: style
style:
	$(COMPOSE) build style
	$(COMPOSE) run style


.PHONY: complexity
complexity:
	$(COMPOSE) build complexity
	$(COMPOSE) run complexity


.PHONY: test
test:
	$(COMPOSE) build test
	$(COMPOSE) run test


.PHONY: security-sast
security-sast:
	$(COMPOSE) build security-sast
	$(COMPOSE) run security-sast
