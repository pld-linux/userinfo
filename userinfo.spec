Summary:	Shows information about a local user
Summary(pl):	Pokazuje informacje o lokalnych u¿ytkownikach
Name:		userinfo
Version:	1.3
Release:	1
License:	GPL v2
Group:		Applications/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(pl):	Aplikacje/System
Group(pt_BR):	Aplicações/Sistema
Source0:	http://m-net.arbornet.org/~bjk/userinfo/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
URL:		http://arbornet.org/~bjk/userinfo/
BuildRequires:	automake
BuildRequires:	autoconf
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
aclocal
autoconf
%configure \
	--with-aliases=/etc/mail/aliases

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README TODO BUGS

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*1.*
%doc *.gz
