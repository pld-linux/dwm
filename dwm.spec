Summary:	Dynamic window manager for X
Name:		dwm
Version:	5.8.2
Release:	1
License:	MIT
Group:		X11/Window Managers
Source0:	http://dl.suckless.org/dwm/%{name}-%{version}.tar.gz
# Source0-md5:	f0b422bfeaa812d66c6dd15c3cc92a6b
Patch0:		%{name}-flags.patch
URL:		http://dwm.suckless.org/
#BuildRequires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dwm is a dynamic window manager for X. It manages windows in tiled,
monocle and floating layouts. All of the layouts can be applied
dynamically, optimising the environment for the application in use and
the task performed.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/dwm
%{_mandir}/man1/dwm.1*
