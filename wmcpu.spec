Summary:	Dockable cpu monitor for WindowMaker
Summary(pl):	Dokowalny monitor procesora dla WindowMakera
Name:		wmcpu
Version: 	1.2
Release:	1
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source:		http://www.linuxwarez.com/~timecop/%{name}-%{version}.tar.gz
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
wmcpu is a program for WindowMaker Dock which gives a graphical 
representation of the info provided by uptime.

%description -l pl
wmcpu jest programem dla Doku WindowMakera, wy¶wietlaj±cym
w formie graficznej informacje o wykorzystaniu zasobów systemowych.

%prep
%setup -q -n %{name}.app

%build
make -C %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir} 

install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}

gzip -9nf CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.gz
%attr(755,root,root) %{_bindir}/%{name}

%changelog
* Mon May 24 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [1.2-1]
- initial RPM release.
