%define upstream_name Test-Warnings
%define upstream_version 0.031

# Avoid nasty build dependency loop
%define dont_gprintify 1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3
Summary:    Test for warnings and the lack of them
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/pod/Test::Warnings
Source0:    http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
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
%doc CONTRIBUTING Changes INSTALL META.json META.yml README examples
%perl_vendorlib/*
%{_mandir}/man3/*
