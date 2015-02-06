%define upstream_name    HTTP-Headers-Fast
%define upstream_version 0.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Faster implementation of HTTP::Headers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTTP/HTTP-Headers-Fast-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Module::Build)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Filter::Util::Call)
BuildRequires:	perl(HTTP::Date)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(YAML)
BuildArch:	noarch

%description
HTTP::Headers::Fast is a perl class for parsing/writing HTTP headers.

The interface is the same as HTTP::Headers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc  META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.130.0-3mdv2011.0
+ Revision: 656928
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.130.0-2mdv2011.0
+ Revision: 625026
- Add a missing build requires.
- import perl-HTTP-Headers-Fast



