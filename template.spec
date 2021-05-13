%define debug_package %{nil}

Summary: {{SUMMARY}}
Name: {{PACKAGE}}
Version: {{VERSION}}
Release: 1%{?dist}
Group: Applications
License: {{LICENSE}}
Packager: {{MAINTAINER}}
Vendor: {{VENDOR}}

Source: tmp.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildArch: {{ARCH}}
AutoReqProv: no

%description
{{DESC}}

%prep
rm -rf $RPM_BUILD_ROOT

%setup -n %{name}

%build

%install
{{INSTALL}}

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
%defattr(-, root, root)
{{FILES}}

%changelog
