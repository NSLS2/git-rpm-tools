Name:           git-rpm-tools
Version:        0.2
Release:        1%{?dist}
Summary:        RPM packaging helper for Git repos

License:        GPL
URL:            https://github.com/NSLS2/git-rpm-tools
Source0:        %{name}-%{version}.tar.gz

#BuildRequires:
Requires:       bash rpmdevtools

#BuildArch:      x86_64
#ExclusiveArch:  x86_64

# Prevent rpmbuild from smart-generating dependencies list
#AutoReq:        no

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
* Fri Aug 19 2022 Derbenev, Anton <aderbenev@bnl.gov> - 0.2-1
- Added script version print-out

* Mon Mar 7 2022 Anton Derbenev <aderbenev@bnl.gov> - 0.1-1
- First version
