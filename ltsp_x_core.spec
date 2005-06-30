# TODO:
# longer descriptions
#
%define		_arch	i386
%define		_pver	4.1
Summary:	Linux Terminal Server Project - X core for terminals
Summary(pl):	Podstawowe X dla terminali z Linux Terminal Server Project
Name:		ltsp_x_core
Version:	4.0.1
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.ltsp.org/ltsp-utils-0.11.tgz
# Source0-md5:	b17b350b18b04d769fcadcd12885a573
Source1:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-x-fonts-1.5-0-%{_arch}.tgz
# Source1-md5:	59de48e31774c3d36a7cd535ae3be9dc
Source2:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-x-core-1.5-0-%{_arch}.tgz
# Source2-md5:	6bec9fe1f85b346f3812e0a5bacdbb1d
Source3:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-freetype-1.1-0-%{_arch}.tgz
# Source3-md5:	33244fc4ebaf79e64bd019e9c0136b77
URL:		http://www.ltsp.org/
Requires:	ltsp_core
AutoProv:	0
AutoReq:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ltspdir	/home/services/ltsp

%description
This package contains X core for LTSP terminals.

%description -l pl
Ten pakiet zawiera podstawowe X dla terminali LTSP.

%prep
%setup -q -n ltsp-utils

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ltspdir}
tar zxf %{SOURCE1}
tar zxf %{SOURCE2}
tar zxf %{SOURCE3}
cd i386
cp -r {etc,usr} $RPM_BUILD_ROOT%{_ltspdir}
ln -sf ../init.d/xprint $RPM_BUILD_ROOT%{_ltspdir}/etc/rc.d/xprint
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc README
%{_ltspdir}/etc/*
%dir %{_ltspdir}/usr/X11R6
%attr(755,root,root) %{_ltspdir}/usr/X11R6/bin
%{_ltspdir}/usr/X11R6/include/X11/fonts
%dir %{_ltspdir}/usr/X11R6/lib
%{_ltspdir}/usr/X11R6/lib/*.a
%attr(755,root,root) %{_ltspdir}/usr/X11R6/lib/*.so*
%attr(755,root,root) %{_ltspdir}/usr/X11R6/lib/X11
%attr(755,root,root) %{_ltspdir}/usr/X11R6/lib/modules
%attr(755,root,root) %{_ltspdir}/usr/bin
%{_ltspdir}/usr/include
%{_ltspdir}/usr/lib
%{_ltspdir}/usr/share
