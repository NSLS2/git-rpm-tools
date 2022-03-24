# git-rpm-tools v0.1 prealpha

An utility which aims to trivialize creating RPMs from an existing git repository. The workflow is as follows:

1. Create and drop a .spec file in `dist/` directory of an existing git repository
2. Run git-rpm-tools in the repository root
3. Get .rpm (or .src.rpm or both) in the repository root

The tool handles creation and cleanup of the rpmbuild tree, archiving the source code, moving .spec, .tar.gz, and .rpm files around, and performs various checks.
