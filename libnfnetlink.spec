#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libnfnetlink
Version  : 1.0.1
Release  : 7
URL      : http://ftp.netfilter.org/pub/libnfnetlink/libnfnetlink-1.0.1.tar.bz2
Source0  : http://ftp.netfilter.org/pub/libnfnetlink/libnfnetlink-1.0.1.tar.bz2
Summary  : Low-level netfilter netlink communication library
Group    : Development/Tools
License  : GPL-2.0
Requires: libnfnetlink-lib

%description
libnfnetlink - userspace library for handling of netfilter netlink messages
(C) 2001-2005 Netfilter Core Team <coreteam@netfilter.org>
===========================================================================

%package dev
Summary: dev components for the libnfnetlink package.
Group: Development
Requires: libnfnetlink-lib

%description dev
dev components for the libnfnetlink package.


%package lib
Summary: lib components for the libnfnetlink package.
Group: Libraries

%description lib
lib components for the libnfnetlink package.


%prep
%setup -q -n libnfnetlink-1.0.1

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libnfnetlink/libnfnetlink.h
/usr/include/libnfnetlink/linux_nfnetlink.h
/usr/include/libnfnetlink/linux_nfnetlink_compat.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
