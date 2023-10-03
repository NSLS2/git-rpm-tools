.PHONY: rpm srpm alldirty clean

rpm:
	./scripts/git-rpm-tools bb

srpm:
	./scripts/git-rpm-tools bs

alldirty:
	./scripts/git-rpm-tools -d -a ba

clean:
	./scripts/git-rpm-tools clean
