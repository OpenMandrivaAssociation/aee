%define	name	aee
%define	version	2.2.15b
%define	release	%mkrel 6

Summary:	An easy to use text editor
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic
Group:		Editors
URL:		http://mahon.cwx.net/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-2.2.15b-mdkconf.patch.bz2
Patch1:		%{name}-2.2.15b-fix-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	X11-devel

%description
An easy to use text editor. Intended to be usable with little or no
instruction. Provides both a terminal (curses based) interface and native
X-Windows interface (in which case the executable is called xae). Features
include pop-up menus, journalling (to recover from system crash or loss of
connection), cut-and-paste, multiple buffers (associated with files or not),
and much more.

%prep
%setup -q
%patch0 -p1 -b .peroyvind
%patch1 -p1 -b .strfmt

%build
make both OPTFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -m755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m755 xae -D $RPM_BUILD_ROOT%{_bindir}/xae
install -m644 %{name}.1 -D $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install -m644 help.ae -D $RPM_BUILD_ROOT%{_datadir}/%{name}/help.ae
cd $RPM_BUILD_ROOT/usr/bin
ln -s aee $RPM_BUILD_ROOT%{_bindir}/rae
ln -s xae $RPM_BUILD_ROOT%{_bindir}/rxae

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Artistic README.aee aee.1.ps aee.i18n.guide keypad
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help.ae
%{_mandir}/man1/*

