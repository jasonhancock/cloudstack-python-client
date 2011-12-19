%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary:	Python client library for the CloudStack API
Name:		python-cloudstack
Version:	0.1
Release:	1%{?dist}
License:	MIT
Group:		Development/Languages
URL:		https://github.com/jasonhancock/cloudstack-python-client
Source:		python-cloudstack-0.1.tar.gz
BuildRequires:	python-devel, python-setuptools-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Python client library for the CloudStack API

%prep
%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE README.md example1.py example2.py 
%{python_sitelib}/*

%changelog
* Mon Dec 19 2011 Jason Hancock <jsnbyh@gmail.com> 0.1-1
- Initial spec file
