%define name            pgfouine
%define version         1.0
%define release         %mkrel 3
%define _requires_exceptions pear(version.php)

Name:	 %{name}
Version: %{version}
Release: %{release}
Summary: PostgreSQL log analyzer
License: GPL
Group:   System/Servers
Source0: %{name}-%{version}.tar.bz2
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





%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0-3mdv2010.0
+ Revision: 430682
- rebuild

* Mon Jun 16 2008 Michael Scherer <misc@mandriva.org> 1.0-2mdv2009.0
+ Revision: 219441
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.0-1mdv2008.0
+ Revision: 23215
- 1.0


* Tue Jan 02 2007 Anne Nicolas <anne.nicolas@mandriva.com> 0.7.2-2mdv2007.0
+ Revision: 103038
- New version
- Import pgfouine

