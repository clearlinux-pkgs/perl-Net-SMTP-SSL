#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Net-SMTP-SSL
Version  : 1.04
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Net-SMTP-SSL-1.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Net-SMTP-SSL-1.04.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-smtp-ssl-perl/libnet-smtp-ssl-perl_1.04-1.debian.tar.xz
Summary  : 'SSL support for Net::SMTP'
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Net-SMTP-SSL-license = %{version}-%{release}
Requires: perl-Net-SMTP-SSL-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(IO::Socket::SSL)
BuildRequires : perl(Net::SSLeay)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Net::SMTP::SSL - SSL support for Net::SMTP
SYNOPSIS
use Net::SMTP::SSL;

my $smtps = Net::SMTP::SSL->new("example.com", Port => 465);

%package dev
Summary: dev components for the perl-Net-SMTP-SSL package.
Group: Development
Provides: perl-Net-SMTP-SSL-devel = %{version}-%{release}
Requires: perl-Net-SMTP-SSL = %{version}-%{release}

%description dev
dev components for the perl-Net-SMTP-SSL package.


%package license
Summary: license components for the perl-Net-SMTP-SSL package.
Group: Default

%description license
license components for the perl-Net-SMTP-SSL package.


%package perl
Summary: perl components for the perl-Net-SMTP-SSL package.
Group: Default
Requires: perl-Net-SMTP-SSL = %{version}-%{release}

%description perl
perl components for the perl-Net-SMTP-SSL package.


%prep
%setup -q -n Net-SMTP-SSL-1.04
cd %{_builddir}
tar xf %{_sourcedir}/libnet-smtp-ssl-perl_1.04-1.debian.tar.xz
cd %{_builddir}/Net-SMTP-SSL-1.04
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Net-SMTP-SSL-1.04/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-SMTP-SSL
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Net-SMTP-SSL/a2cc7c2b3eca0e259ce85f70493bfe95e2fd8dff || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::SMTP::SSL.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-SMTP-SSL/a2cc7c2b3eca0e259ce85f70493bfe95e2fd8dff

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
