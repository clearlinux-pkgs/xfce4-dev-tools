#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: 750e50d
#
Name     : xfce4-dev-tools
Version  : 4.18.1
Release  : 15
URL      : https://archive.xfce.org/src/xfce/xfce4-dev-tools/4.18/xfce4-dev-tools-4.18.1.tar.bz2
Source0  : https://archive.xfce.org/src/xfce/xfce4-dev-tools/4.18/xfce4-dev-tools-4.18.1.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-dev-tools-bin = %{version}-%{release}
Requires: xfce4-dev-tools-license = %{version}-%{release}
Requires: xfce4-dev-tools-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(glib-2.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![License](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://gitlab.xfce.org/xfce/xfce4-dev-tools/-/blob/master/COPYING)

%package bin
Summary: bin components for the xfce4-dev-tools package.
Group: Binaries
Requires: xfce4-dev-tools-license = %{version}-%{release}

%description bin
bin components for the xfce4-dev-tools package.


%package dev
Summary: dev components for the xfce4-dev-tools package.
Group: Development
Requires: xfce4-dev-tools-bin = %{version}-%{release}
Provides: xfce4-dev-tools-devel = %{version}-%{release}
Requires: xfce4-dev-tools = %{version}-%{release}

%description dev
dev components for the xfce4-dev-tools package.


%package license
Summary: license components for the xfce4-dev-tools package.
Group: Default

%description license
license components for the xfce4-dev-tools package.


%package man
Summary: man components for the xfce4-dev-tools package.
Group: Default

%description man
man components for the xfce4-dev-tools package.


%prep
%setup -q -n xfce4-dev-tools-4.18.1
cd %{_builddir}/xfce4-dev-tools-4.18.1
pushd ..
cp -a xfce4-dev-tools-4.18.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707108606
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707108606
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfce4-dev-tools
cp %{_builddir}/xfce4-dev-tools-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xfce4-dev-tools/4cc77b90af91e615a64ae04893fdffa7939db84c || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/xdt-csource
/usr/bin/xdt-autogen
/usr/bin/xdt-csource
/usr/bin/xfce-build
/usr/bin/xfce-do-release
/usr/bin/xfce-get-release-notes
/usr/bin/xfce-get-translations
/usr/bin/xfce-update-news

%files dev
%defattr(-,root,root,-)
/usr/share/aclocal/*.m4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xfce4-dev-tools/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xdt-csource.1
