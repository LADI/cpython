DISTDIR ?= $(shell portageq distdir)
TAG ?= HEAD
VERSION ?= $(shell git describe --tags $(TAG))

dist:
	git archive $(TAG) | xz > $(DISTDIR)/python-gentoo-patches-$(VERSION).tar.xz
