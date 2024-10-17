%define __noautoreq /usr/bin/php

Name:	 pgfouine
Version: 1.0
Release: 5
Summary: PostgreSQL log analyzer

License: GPL
Group:   System/Servers
Source0: %{name}-%{version}.tar.bz2
URL:     https://pgfouine.projects.postgresql.org
Requires: postgresql-server
Requires: php-cli
Buildarch: noarch

%description
pgFouine is a PostgreSQL log analyzer used to generate 
detailed reports from a PostgreSQL log file. pgFouine 
can help you to determine which queries you should
optimize to speed up your PostgreSQL based application.

%prep
%setup -q -n  %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
mkdir -p %{buildroot}%{_libdir}/%{name}
install -m 755 pgfouine.php %{buildroot}%{_bindir}
cp -r include %{buildroot}%{_libdir}/%{name}
install -m 644 AUTHORS ChangeLog COPYING INSTALL README THANKS %{buildroot}%{_docdir}/%{name}-%{version}
cp -r tests %{buildroot}%{_docdir}/%{name}-%{version}

%clean

%files
%{_bindir}/*
%{_docdir}/%{name}-%{version}
%{_libdir}/%{name}





