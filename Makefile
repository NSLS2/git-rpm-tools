.PHONY: dirs localinstall bundle flatbundle rpm srpm clean

rpm:
	./scripts/git-rpm-tools bb

srpm:
	./scripts/git-rpm-tools bs

clean:
	rm -rf *.rpm
