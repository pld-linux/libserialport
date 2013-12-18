Summary:	Cross-platform serial port access library
Name:		libserialport
Version:	0.1
Release:	1
License:	GPL v3+
Group:		Libraries
URL:		http://www.sigrok.org/
Source0:	http://sigrok.org/download/source/libserialport/%{name}-%{version}.tar.gz
# Source0-md5:	37b226331432a571f247b6406af606db
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	udev-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minimal, cross-platform shared library written in C that is intended
to take care of the OS-specific details when writing software that
uses serial ports.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static \
	--disable-silent-rules \
	--enable-all-drivers \

%{__make}

doxygen Doxyfile

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_libdir}/libserialport.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libserialport.so.0

%files devel
%defattr(644,root,root,755)
%doc doxy/html-api/*
%{_includedir}/libserialport.h
%attr(755,root,root) %{_libdir}/libserialport.so
%{_pkgconfigdir}/libserialport.pc
