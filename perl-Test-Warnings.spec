%define upstream_name Test-Warnings
%define upstream_version 0.016

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3
Summary:    Test for warnings and the lack of them
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(List::Util)
BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::More) >= 0.940.0
BuildRequires: perl(Test::Tester) >= 0.108.0
BuildArch:  noarch

%description
This module is intended to be used as a drop-in replacement for
Test::NoWarnings: it also adds an extra test, but runs this test
before done_testing calculates the test count, rather than after.
It does this by hooking into done_testing as well as via an END
block. You can declare a plan, or not, and things will still Just
Work.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc CONTRIBUTING Changes INSTALL LICENSE META.json META.yml MYMETA.yml README examples
%perl_vendorlib/*
%{_mandir}/man3/*


%changelog
* Sat Jun 21 2014 sander85 <sander85> 0.16.0-1.mga5
+ Revision: 638405
- update to 0.016

* Fri Mar 14 2014 jquelin <jquelin> 0.14.0-1.mga5
+ Revision: 603737
- update to 0.014

* Thu Feb 06 2014 sander85 <sander85> 0.13.0-1.mga5
+ Revision: 584461
- update to 0.013

* Tue Oct 22 2013 umeabot <umeabot> 0.11.0-2.mga4
+ Revision: 542264
- Mageia 4 Mass Rebuild

* Mon Oct 14 2013 sander85 <sander85> 0.11.0-1.mga4
+ Revision: 497172
- update to 0.011

* Wed Sep 25 2013 sander85 <sander85> 0.10.0-1.mga4
+ Revision: 485896
- update to 0.010

* Wed Sep 11 2013 sander85 <sander85> 0.9.0-1.mga4
+ Revision: 477557
- update to 0.009

* Sun Jul 14 2013 sander85 <sander85> 0.8.0-1.mga4
+ Revision: 454318
- update to 0.008

* Wed Jul 10 2013 sander85 <sander85> 0.7.0-1.mga4
+ Revision: 452642
- update to 0.007

* Tue Jul 09 2013 sander85 <sander85> 0.6.0-1.mga4
+ Revision: 452028
- imported package perl-Test-Warnings

