Summary:	Dockable cpu monitor for WindowMaker
Summary(pl.UTF-8):	Dokowalny monitor procesora dla WindowMakera
Name:		wmcpu
Version:	1.3
Release:	5
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.ne.jp/asahi/linux/timecop/software/%{name}-%{version}.tar.gz
# Source0-md5:	1e8e108c613cde810eed40e6ce4c26d9
Source1:	%{name}.desktop
URL:		http://www.ne.jp/asahi/linux/timecop/
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmcpu is a program for WindowMaker Dock which gives a graphical
representation of the info provided by uptime.

%description -l pl.UTF-8
wmcpu jest programem dla Doku WindowMakera, wyświetlającym w formie
graficznej informacje o wykorzystaniu zasobów systemowych.

%prep
%setup -q

%build
%{__make} %{name} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall" \
	LDFLAGS="-L/usr/%{_lib} -lXpm -lXext -lX11"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/wmcpu.desktop
