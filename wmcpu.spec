Summary:	Dockable cpu monitor for WindowMaker
Summary(pl):	Dokowalny monitor procesora dla WindowMakera
Name:		wmcpu
Version:	1.2
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://www.linuxwarez.com/~timecop/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
wmcpu is a program for WindowMaker Dock which gives a graphical
representation of the info provided by uptime.

%description -l pl
wmcpu jest programem dla Doku WindowMakera, wy¶wietlaj±cym w formie
graficznej informacje o wykorzystaniu zasobów systemowych.

%prep
%setup -q -n %{name}.app
%patch -p0

%build
%{__make} -C %{name} CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets} 

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.gz
%attr(755,root,root) %{_bindir}/%{name}

%{_applnkdir}/DockApplets/wmcpu.desktop
