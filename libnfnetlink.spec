#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD55D978A8A1420E4 (coreteam@netfilter.org)
#
Name     : libnfnetlink
Version  : 1.0.2
Release  : 17
URL      : https://www.netfilter.org/projects/libnfnetlink/files/libnfnetlink-1.0.2.tar.bz2
Source0  : https://www.netfilter.org/projects/libnfnetlink/files/libnfnetlink-1.0.2.tar.bz2
Source1  : https://www.netfilter.org/projects/libnfnetlink/files/libnfnetlink-1.0.2.tar.bz2.sig
Summary  : Low-level netfilter netlink communication library
Group    : Development/Tools
License  : GPL-2.0
Requires: libnfnetlink-lib = %{version}-%{release}
Requires: libnfnetlink-license = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32

%description
libnfnetlink - userspace library for handling of netfilter netlink messages
(C) 2001-2005 Netfilter Core Team <coreteam@netfilter.org>
===========================================================================

%package dev
Summary: dev components for the libnfnetlink package.
Group: Development
Requires: libnfnetlink-lib = %{version}-%{release}
Provides: libnfnetlink-devel = %{version}-%{release}
Requires: libnfnetlink = %{version}-%{release}

%description dev
dev components for the libnfnetlink package.


%package dev32
Summary: dev32 components for the libnfnetlink package.
Group: Default
Requires: libnfnetlink-lib32 = %{version}-%{release}
Requires: libnfnetlink-dev = %{version}-%{release}

%description dev32
dev32 components for the libnfnetlink package.


%package lib
Summary: lib components for the libnfnetlink package.
Group: Libraries
Requires: libnfnetlink-license = %{version}-%{release}

%description lib
lib components for the libnfnetlink package.


%package lib32
Summary: lib32 components for the libnfnetlink package.
Group: Default
Requires: libnfnetlink-license = %{version}-%{release}

%description lib32
lib32 components for the libnfnetlink package.


%package license
Summary: license components for the libnfnetlink package.
Group: Default

%description license
license components for the libnfnetlink package.


%prep
%setup -q -n libnfnetlink-1.0.2
cd %{_builddir}/libnfnetlink-1.0.2
pushd ..
cp -a libnfnetlink-1.0.2 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649176616
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1649176616
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libnfnetlink
cp %{_builddir}/libnfnetlink-1.0.2/COPYING %{buildroot}/usr/share/package-licenses/libnfnetlink/075d599585584bb0e4b526f5c40cb6b17e0da35a
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libnfnetlink/libnfnetlink.h
/usr/include/libnfnetlink/linux_nfnetlink.h
/usr/include/libnfnetlink/linux_nfnetlink_compat.h
/usr/lib64/libnfnetlink.so
/usr/lib64/pkgconfig/libnfnetlink.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libnfnetlink.so
/usr/lib32/pkgconfig/32libnfnetlink.pc
/usr/lib32/pkgconfig/libnfnetlink.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnfnetlink.so.0
/usr/lib64/libnfnetlink.so.0.2.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libnfnetlink.so.0
/usr/lib32/libnfnetlink.so.0.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libnfnetlink/075d599585584bb0e4b526f5c40cb6b17e0da35a
