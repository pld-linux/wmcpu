Summary:	Dockable cpu monitor for WindowMaker
Summary(pl):	Dokowalny monitor procesora dla WindowMakera
Name:		wmcpu
Version: 	1.2
Release:	2
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source0:	http://www.linuxwarez.com/~timecop/%{name}-%{version}.tar.gz
Source1:	wmcpu.desktop
Patch:		wmcpu-makefile.patch
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
wmcpu is a program for WindowMaker Dock which gives a graphical 
representation of the info provided by uptime.

%description -l pl
wmcpu jest programem dla Doku WindowMakera, wy�wietlaj�cym
w formie graficznej informacje o wykorzystaniu zasob�w systemowych.

%prep
%setup -q -n %{name}.app
%patch -p0

%build
make -C %{name} CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},/etc/X11/applnk/DockApplets} 

install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/DockApplets

gzip -9nf CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.gz
%attr(755,root,root) %{_bindir}/%{name}

/etc/X11/applnk/DockApplets/wmcpu.desktop
