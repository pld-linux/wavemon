Summary:	monitoring application for wireless network devices
Name:		wavemon
Version:	0.4.0b
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.wavemage.com/wavemon-current.tar.gz
# Source0-md5:	2baab37eb967fc38dc53f8e4f609daac
Patch0:		%{name}-exit.patch
URL:		http://www.wavemage.com/projects.html
BuildRequires:  ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
monitoring application for wireless network devices.

%prep
%setup -q 
%patch0 -p1

%build
%configure2_13
%{__make} \
	CFLAGS="-I%{_includedir}/ncurses %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man{1,5}}

install %{name} $RPM_BUILD_ROOT%{_sbindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1
install *.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog README TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
