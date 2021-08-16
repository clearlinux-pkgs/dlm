#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dlm
Version  : 4.1.0
Release  : 4
URL      : https://pagure.io/dlm/archive/dlm-4.1.0/dlm-dlm-4.1.0.tar.gz
Source0  : https://pagure.io/dlm/archive/dlm-4.1.0/dlm-dlm-4.1.0.tar.gz
Summary  : The dlm library
Group    : Development/Tools
License  : LGPL-2.1
Requires: dlm-bin = %{version}-%{release}
Requires: dlm-config = %{version}-%{release}
Requires: dlm-lib = %{version}-%{release}
Requires: dlm-license = %{version}-%{release}
Requires: dlm-man = %{version}-%{release}
BuildRequires : libxml2-dev
BuildRequires : pkgconfig(libcpg)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(pacemaker)
BuildRequires : util-linux-dev
BuildRequires : xz-dev

%description
| ``See https://pagure.io/dlm``
| ``See dlm_controld(8) at dlm.git/dlm_controld/dlm_controld.8``
| ``See dlm.conf(5) at dlm.git/dlm_controld/dlm.conf.5``

%package bin
Summary: bin components for the dlm package.
Group: Binaries
Requires: dlm-config = %{version}-%{release}
Requires: dlm-license = %{version}-%{release}

%description bin
bin components for the dlm package.


%package config
Summary: config components for the dlm package.
Group: Default

%description config
config components for the dlm package.


%package dev
Summary: dev components for the dlm package.
Group: Development
Requires: dlm-lib = %{version}-%{release}
Requires: dlm-bin = %{version}-%{release}
Provides: dlm-devel = %{version}-%{release}
Requires: dlm = %{version}-%{release}

%description dev
dev components for the dlm package.


%package lib
Summary: lib components for the dlm package.
Group: Libraries
Requires: dlm-license = %{version}-%{release}

%description lib
lib components for the dlm package.


%package license
Summary: license components for the dlm package.
Group: Default

%description license
license components for the dlm package.


%package man
Summary: man components for the dlm package.
Group: Default

%description man
man components for the dlm package.


%prep
%setup -q -n dlm-dlm-4.1.0
cd %{_builddir}/dlm-dlm-4.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629131199
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1629131199
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dlm
cp %{_builddir}/dlm-dlm-4.1.0/README.license %{buildroot}/usr/share/package-licenses/dlm/2303030c0e7e6704043065164610e93cfb922139
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dlm_controld
/usr/bin/dlm_stonith
/usr/bin/dlm_tool

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/51-dlm.rules

%files dev
%defattr(-,root,root,-)
/usr/include/libdlm.h
/usr/include/libdlmcontrol.h
/usr/lib64/libdlm.so
/usr/lib64/libdlm_lt.so
/usr/lib64/libdlmcontrol.so
/usr/lib64/pkgconfig/libdlm.pc
/usr/lib64/pkgconfig/libdlm_lt.pc
/usr/lib64/pkgconfig/libdlmcontrol.pc
/usr/share/man/man3/dlm_cleanup.3
/usr/share/man/man3/dlm_close_lockspace.3
/usr/share/man/man3/dlm_create_lockspace.3
/usr/share/man/man3/dlm_dispatch.3
/usr/share/man/man3/dlm_get_fd.3
/usr/share/man/man3/dlm_lock.3
/usr/share/man/man3/dlm_lock_wait.3
/usr/share/man/man3/dlm_ls_lock.3
/usr/share/man/man3/dlm_ls_lock_wait.3
/usr/share/man/man3/dlm_ls_lockx.3
/usr/share/man/man3/dlm_ls_pthread_init.3
/usr/share/man/man3/dlm_ls_unlock.3
/usr/share/man/man3/dlm_ls_unlock_wait.3
/usr/share/man/man3/dlm_new_lockspace.3
/usr/share/man/man3/dlm_open_lockspace.3
/usr/share/man/man3/dlm_pthread_init.3
/usr/share/man/man3/dlm_release_lockspace.3
/usr/share/man/man3/dlm_unlock.3
/usr/share/man/man3/dlm_unlock_wait.3
/usr/share/man/man3/libdlm.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdlm.so.3
/usr/lib64/libdlm.so.3.0
/usr/lib64/libdlm_lt.so.3
/usr/lib64/libdlm_lt.so.3.0
/usr/lib64/libdlmcontrol.so.3
/usr/lib64/libdlmcontrol.so.3.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dlm/2303030c0e7e6704043065164610e93cfb922139

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/dlm.conf.5
/usr/share/man/man8/dlm_controld.8
/usr/share/man/man8/dlm_stonith.8
/usr/share/man/man8/dlm_tool.8
