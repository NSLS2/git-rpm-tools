# git-rpm-tools v0.8

An utility which aims to trivialize creating RPMs from an existing git repository.

The tool handles creation and cleanup of the rpmbuild tree, archiving the source code,
moving .spec, .tar.gz, and .rpm files around, and performs various checks.

## Usage

The default workflow is as follows:

1. Create and drop a .spec file in `dist/` directory of an existing git repository
2. Run `git-rpm-tools` in the repository root
3. The .rpm (or .src.rpm or both) will be generated in the repository root

See `git-rpm-tools -h` for list of all available options and customizations.
Custom branch, package, source tarball name, and .spec file to use can be defined.

## Dependencies

`rpmdevtools` package is reqiuired to run the tool.
