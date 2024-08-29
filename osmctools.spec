Summary:	Fast tools to convert, filter and update OpenStreetMap data files
Summary(pl.UTF-8):	Szybkie narzędzia do konwersji, filtrowania i aktualizacji plików danych OpenStreetMap
Name:		osmctools
Version:	0.9
Release:	1
License:	AGPL v3
Group:		Applications
#Source0Download: https://gitlab.com/osm-c-tools/osmctools/-/releases
Source0:	https://gitlab.com/osm-c-tools/osmctools/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	7ab264d49065765e57fccdf5f5fc66b7
URL:		https://gitlab.com/osm-c-tools/osmctools
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast tools to convert, filter and update OpenStreetMap data files.

%description -l pl.UTF-8
Szybkie narzędzia do konwersji, filtrowania i aktualizacji plików
danych OpenStreetMap.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/osmconvert
%attr(755,root,root) %{_bindir}/osmfilter
%attr(755,root,root) %{_bindir}/osmupdate
