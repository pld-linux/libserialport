#
# Conditional build:
%bcond_without	static_libs	# static library build
#
Summary:	Cross-platform serial port access library
Summary(pl.UTF-8):	Wieloplatformowa biblioteka dostępu do portu szeregowego
Name:		libserialport
Version:	0.1.1
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	http://sigrok.org/download/source/libserialport/%{name}-%{version}.tar.gz
# Source0-md5:	b93f0325a6157198152b5bd7e8182b51
URL:		http://sigrok.org/wiki/Libserialport
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	doxygen
BuildRequires:	libtool >= 2:2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minimal, cross-platform shared library written in C that is intended
to take care of the OS-specific details when writing software that
uses serial ports.

%description -l pl.UTF-8
Minimalna, wieloplatformowa, napisana w C biblioteka współdzielona
mająca na celu zadbać o wszystkie specyficzne dla systemu operacyjnego
szczegóły przy pisaniu oprogramowania wykorzystującego porty
szeregowe.

%package devel
Summary:	Development files for libserialport
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libserialport
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	udev-devel

%description devel
This package contains the header files for developing applications
that use libserialport.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę libserialport.

%package static
Summary:	Static libserialport library
Summary(pl.UTF-8):	Statyczna biblioteka libserialport
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libserialport library.

%description static -l pl.UTF-8
Statyczna biblioteka libserialport.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I autostuff
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}

%{__make}

doxygen Doxyfile

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libserialport.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libserialport.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libserialport.so.0

%files devel
%defattr(644,root,root,755)
%doc doxy/html-api/*
%attr(755,root,root) %{_libdir}/libserialport.so
%{_includedir}/libserialport.h
%{_pkgconfigdir}/libserialport.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libserialport.a
%endif
