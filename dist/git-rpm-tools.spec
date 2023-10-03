Name:           git-rpm-tools
Version:        0.5
Release:        1%{?dist}
Summary:        RPM packaging helper for Git repos

License:        BSD-3-Clause
URL:            https://github.com/NSLS2/git-rpm-tools
Source0:        %{name}-%{version}.tar.gz

#BuildRequires:
Requires:       bash rpmdevtools

#BuildArch:      x86_64
#ExclusiveArch:  x86_64

# Prevent rpmbuild from smart-generating dependencies list
#AutoReq:        no

# Prevent rpmbuild from auto-mangling executable shebangs
# %%undefine __brp_mangle_shebangs

%description
A set of tools to facilitate RPM packaging of Git repositories

%global debug_package %{nil}

%prep
%autosetup -p1

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
cp ./scripts/git-rpm-tools %{buildroot}/usr/local/bin

%files
/usr/local/bin/*

%changelog
* Tue Oct 03 2023 Derbenev, Anton <aderbenev@bnl.gov> - 0.5-1
- Added -a option to absorb uncommitted changes
- Added clean command to remove rpms and build tree
- Updated .gitignore

* Tue Apr 04 2023 Derbenev, Anton <aderbenev@bnl.gov> - 0.4-1
- Added Makefile for self-rpm-build

* Tue Apr 04 2023 Derbenev, Anton <aderbenev@bnl.gov> - 0.3-2
- Added license info

* Tue Feb 14 2023 Derbenev, Anton <aderbenev@bnl.gov> - 0.3-1
- Exit code fix, more verbosity on clean

* Fri Aug 19 2022 Derbenev, Anton <aderbenev@bnl.gov> - 0.2-2
- Disabled debug package

* Fri Aug 19 2022 Derbenev, Anton <aderbenev@bnl.gov> - 0.2-1
- Added script version print-out

* Mon Mar 7 2022 Anton Derbenev <aderbenev@bnl.gov> - 0.1-1
- First version
