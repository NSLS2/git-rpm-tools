Name:           git-rpm-tools
Version:        0.1
Release:        1%{?dist}
Summary:        RPM packaging helper for Git repos

License:        GPL
#URL:
Source0:        %{name}-%{version}.tar.gz

#BuildRequires:
Requires:       bash

BuildArch:      x86_64
#ExclusiveArch:  x86_64

# Prevent rpmbuild from smart-generating dependencies list
AutoReq:        no

# Prevent rpmbuild from auto-mangling executable shebangs
#%undefine __brp_mangle_shebangs

%description
A set of tools to facilitate RPM packaging of Git repositories

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

* Mon Mar 7 2022 Anton Derbenev <aderbenev@bnl.gov> - 1-1
- First version

