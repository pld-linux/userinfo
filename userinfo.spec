Summary:	Shows information about a local user
Summary(pl):	Pokazuje informacje o lokalnych u¿ytkownikach
Name:		userinfo
Version:	2.0
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://arbornet.org/~bjk/userinfo/%{name}-%{version}.tar.gz
# Source0-md5:	53846e00d984d84babfe09063c02b6b1
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

%description -l pl
userinfo jest ma³ym konsolowym narzêdziem, które pokazuje tyle
informacji o lokalnym u¿ytkowniku, ile to tylko mo¿liwe. Wy¶wietla:
informacjê z plików passwd, mail info, login info i wiele innych

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
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_mandir}/man1/*1.*
