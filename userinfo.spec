Summary:	Shows information about a local user
Summary(pl.UTF-8):   Pokazuje informacje o lokalnych użytkownikach
Name:		userinfo
Version:	2.1
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://arbornet.org/~bjk/userinfo/%{name}-%{version}.tar.gz
# Source0-md5:	e3ac891b4e902954747eadc9d74e3408
Patch0:		%{name}-utmpx.patch
URL:		http://arbornet.org/~bjk/userinfo/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
Requires:	utempter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
userinfo is a small console utility which shows as much information
about a local user as possible. Output options include: password file
info, mail info, login info and more.

%description -l pl.UTF-8
userinfo jest małym konsolowym narzędziem, które pokazuje tyle
informacji o lokalnym użytkowniku, ile to tylko możliwe. Wyświetla:
informację z plików passwd, mail info, login info i wiele innych

%prep
%setup  -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-aliases=/etc/mail/aliases

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
# what about  /usr/lib/userinfo/{login.la,mail.la,passwd.la} ?
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_mandir}/man1/*1.*
