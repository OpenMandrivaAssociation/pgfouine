%define name            pgfouine
%define version         0.7.2
%define release         %mkrel 2
%define _requires_exceptions pear(version.php)

Name:	 %{name}
Version: %{version}
Release: %{release}
Summary: PostgreSQL log analyzer
License: GPL
Group:   System/Servers
Source0: %{name}-%{version}.tar.gz
#Patch0: %{name}-include_path.patch.bz2
URL:     http://pgfouine.projects.postgresql.org
Requires: postgresql-server
Requires: php-cli
BuildRoot: %{_tmppath}/%{name}-buildroot
Buildarch: noarch

%description
pgFouine is a PostgreSQL log analyzer used to generate 
detailed reports from a PostgreSQL log file. pgFouine 
can help you to determine which queries you should
optimize to speed up your PostgreSQL based application.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n  %{name}-%{version}
#%patch0 -p0

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
install -m 755 pgfouine.php %{buildroot}%{_bindir}
cp -r include %{buildroot}%{_libdir}/%{name}
install -m 644 AUTHORS ChangeLog COPYING INSTALL README THANKS %{buildroot}%{_docdir}/%{name}-%{version}
cp -r tests %{buildroot}%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_docdir}/%{name}-%{version}
%{_libdir}/%{name}



