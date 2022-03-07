# basic.spec

Name:           basic-package
Version:        1
Release:        1%{?dist}
Summary:        Basic template package

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
%undefine __brp_mangle_shebangs

%description
Basic template package

%prep
%autosetup -p1

%build

%install

%files

%changelog

* Mon Mar 7 2022 Anton Derbenev <aderbenev@bnl.gov> - 1-1
- First version
