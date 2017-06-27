PYTHON = python3
PYTEST = pytest

PACKAGE = conreality
VERSION = `cat VERSION`

SOURCES =

BINARIES =

dist/$(PACKAGE)-$(VERSION).tar.gz: setup.py $(SOURCES)
	$(PYTHON) setup.py sdist

all: build

build: setup.py $(SOURCES)
	$(PYTHON) setup.py build

check: $(SOURCES) test/test_package.py
	PYTHONPATH=src $(PYTEST)

dist: dist/$(PACKAGE)-$(VERSION).tar.gz

install: setup.py $(SOURCES)
	$(PYTHON) setup.py build

clean: setup.py
	@rm -Rf *~ dist/*
	$(PYTHON) setup.py clean

distclean: clean

mostlyclean: clean

.PHONY: build check install clean distclean mostlyclean
