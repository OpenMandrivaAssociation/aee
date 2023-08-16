%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	An easy to use text editor
Name:		aee
Version:	2.2.22
Release:	1
License:	Artistic
Group:		Editors
# Abandoned upstream. We grab the source from FreeBSD's clone
Source0:	https://gitlab.com/ports1/aee/-/archive/%{version}/aee-%{version}.tar.gz
Patch0:		%{name}-2.2.15b-mdkconf.patch
Patch2:		%{name}-2.2.21-compile.patch
BuildRequires:	pkgconfig(x11)

%description
An easy to use text editor. Intended to be usable with little or no
instruction. Provides both a terminal (curses based) interface and native
X-Windows interface (in which case the executable is called xae). Features
include pop-up menus, journalling (to recover from system crash or loss of
connection), cut-and-paste, multiple buffers (associated with files or not),
and much more.

%files
%doc Artistic README.aee aee.1.ps aee.i18n.guide keypad
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help.ae
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1
chmod +x create.mk*

%build
make both OPTFLAGS="%{optflags}"

%install
install -m755 %{name} -D %{buildroot}%{_bindir}/%{name}
install -m755 xae -D %{buildroot}%{_bindir}/xae
install -m644 %{name}.1 -D %{buildroot}%{_mandir}/man1/%{name}.1
install -m644 help.ae -D %{buildroot}%{_datadir}/%{name}/help.ae
pushd %{buildroot}%{_bindir}
ln -s aee %{buildroot}%{_bindir}/rae
ln -s xae %{buildroot}%{_bindir}/rxae
popd

