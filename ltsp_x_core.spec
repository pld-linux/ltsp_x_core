#
# TODO:
# longer descriptions
#
Summary:	Linux Terminal Server Project - X core for terminals
Summary(pl):	Podstawowa X dla terminali z Linux Terminal Server Project
Name:		ltsp_x_core
Version:	3.0.4
Release:	0.1
License:	GPL
Group:		Applications/Network
Source0:	http://dl.sourceforge.net/ltsp/%{name}-%{version}-i386.tgz
# Source0-md5:	94dc471e8537d47568f35044b1bcfd4a
URL:		http://www.ltsp.org/
Requires:	ltsp_core
AutoProv:	0
AutoReq:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ltspdir	/home/services/ltsp
%define		no_install_post_strip	1

%description
This package contains X core for LTSP terminals.

%description -l pl
Ten pakiet zawiera podstawowe X dla terminali LTSP.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ltspdir}

cd i386
cp -r {bin,etc,usr} $RPM_BUILD_ROOT%{_ltspdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_ltspdir}/bin/*
%{_ltspdir}/etc/*
%dir %{_ltspdir}/usr/X11R6
%attr(755,root,root) %{_ltspdir}/usr/X11R6/bin
%dir %{_ltspdir}/usr/X11R6/lib
%{_ltspdir}/usr/X11R6/lib/*.a
%attr(755,root,root) %{_ltspdir}/usr/X11R6/lib/*.so*
%attr(755,root,root) %{_ltspdir}/usr/X11R6/lib/X11
%attr(755,root,root) %{_ltspdir}/usr/X11R6/lib/modules
