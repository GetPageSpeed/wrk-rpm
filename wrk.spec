Name: wrk
Version: 4.2.0
Release: 1%{?dist}
Summary: HTTP benchmarking tool
License: Modified Apache 2.0 License
URL: https://github.com/wg/wrk

Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: pkgconfig(luajit2)
BuildRequires: pkgconfig(openssl)

%if ( 0%{?fedora} >= 27 )
BuildRequires: perl
%endif

%description
  wrk is a modern HTTP benchmarking tool capable of generating significant
  load when run on a single multi-core CPU. It combines a multithreaded
  design with scalable event notification systems such as epoll and kqueue.

  An optional LuaJIT script can perform HTTP request generation, response
  processing, and custom reporting. Details are available in SCRIPTING and
  several examples are located in %{_docdir}/%{name}-%{version}/scripts/

%prep
%setup -q
# Upstream Makefile hardcodes `-lluajit-5.1` and binary `luajit`. luajit2 in
# GetPageSpeed extras ships /usr/bin/luajit2 + libluajit2-5.1.so.2, so retarget
# the Makefile to those names.
sed -i 's@-I$(WITH_LUAJIT)/include@`pkg-config --cflags luajit2`@' Makefile
sed -i 's@-L$(WITH_LUAJIT)/lib@@'                                  Makefile
sed -i 's@-I$(WITH_OPENSSL)/include@`pkg-config --cflags openssl`@' Makefile
sed -i 's@-L$(WITH_OPENSSL)/lib@@'                                  Makefile
sed -i 's@-lluajit-5\.1@`pkg-config --libs luajit2`@'                Makefile
sed -i 's@\bluajit -bc\b@luajit2 -bc@'                              Makefile

%build
# EL7 doesn't have this macro: %%make_build macro
# passing -g because Makefile doesn't (for debuginfo)
# FC36 when linking gives error:
# /usr/bin/ld: obj/wrk.o: relocation R_X86_64_32 against `.text' can not be used when making a PIE object; recompile with -fPIE
CFLAGS='-g -fPIE' %{__make} VER=%{version} %{?_smp_mflags} WITH_LUAJIT=SYS WITH_OPENSSL=SYS

%install
%{__install} -Dpm0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
# Virtually add license macro for EL6:
%{!?_licensedir:%global license %%doc}
%license LICENSE NOTICE
%doc README.md CHANGES SCRIPTING scripts
%{_bindir}/%{name}

%changelog
* Tue Dec 14 2021 Danila Vershinin <info@getpagespeed.com> 4.2.0-1
- release 4.2.0

* Sat Jun 15 2019 Danila Vershinin <info@getpagespeed.com> 4.1.0-3
- proper debuginfo package
- link against system libraries

* Sat Oct 27 2018 Anatolii Vorona <vorona.tolik@gmail.com> 4.1.0-1
- added build requires for Copr Build Service (fedora 27+)

* Thu May 10 2018 GetPageSpeed Builder <info@getpagespeed.com> 4.1.0-1
- new upstream release 4.1.0
- removed build requires as they are bundled with source now

* Sat Apr 01 2017 GetPageSpeed Builder <info@getpagespeed.com> 4.0.2-2
- new package built with tito

* Mon Nov  7 2016 IWAI, Masaharu <iwaim.sub@gmail.com> - 4.0.2-1
- initial release

