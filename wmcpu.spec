Summary:	Dockable cpu monitor for WindowMaker
Summary(pl):	Dokowalny monitor procesora dla WindowMakera
Name:		wmcpu
Version:	1.3
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.ne.jp/asahi/linux/timecop/software/%{name}-%{version}.tar.gz
# Source0-md5:	1e8e108c613cde810eed40e6ce4c26d9
Source1:	%{name}.desktop
URL:		http://www.ne.jp/asahi/linux/timecop/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmcpu is a program for WindowMaker Dock which gives a graphical
representation of the info provided by uptime.

%description -l pl
wmcpu jest programem dla Doku WindowMakera, wy¶wietlaj±cym w formie
graficznej informacje o wykorzystaniu zasobów systemowych.

%prep
%setup -q

%build
%{__make} %{name} \
	CC=%{__cc} \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}

#%%{_applnkdir}/DockApplets/wmcpu.desktop
