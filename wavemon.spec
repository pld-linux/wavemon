Summary:	Monitoring application for wireless network devices
Summary(pl.UTF-8):	Narzędzie monitorujące dla urządzeń sieci bezprzewodowych
Name:		wavemon
Version:	0.7.2
Release:	2
License:	GPL v2
Group:		Applications/Networking
Source0:	http://eden-feed.erg.abdn.ac.uk/wavemon/stable-releases/%{name}-%{version}.tar.bz2
# Source0-md5:	0dec700364df7bfb2e066624d0acf7bb
URL:		http://eden-feed.erg.abdn.ac.uk/wavemon/
BuildRequires:	autoconf
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monitoring application for wireless network devices.

%description -l pl.UTF-8
Narzędzie monitorujące dla urządzeń sieci bezprzewodowych.

%prep
%setup -q
sed -e 's|\[ncurses.h|\[ncurses/ncurses.h|' -i configure.ac

%build
%{__autoconf}
%configure
%{__make} \
	CFLAGS="-I/usr/include/ncurses %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1
install *.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
