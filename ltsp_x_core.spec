#
# TODO:
# desc, cleanups
#
Summary:	Linux Terminal Server Project - X Core
Summary(pl):	Baza X Linux Terminal Server Project
Name:		ltsp_x_core
Version:	3.0.4
Release:	0.1
License:	GPL
Group:		Applications/Network
Source0:	http://cesnet.dl.sourceforge.net/sourceforge/ltsp/%{name}-%{version}-i386.tgz
URL:		http://www.ltsp.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define		_ltspdir	/home/services/ltsp
%define no_install_post_strip	1
%define _noautoprovfiles        "%{_ltspdir}/usr/X11R6/lib/* tdfx_dri.so"
%define _noautoreq		"libc.so.6 libc.so.6 libc.so.6 libc.so.6 libc.so.6 libc.so.6 libdl.so.2 libdl.so.2 libdl.so.2 libm.so.6 libm.so.6 libpthread.so.0 libpthread.so.0 libstdc++-libc6.2-2.so.3 glibc libstdc++-compat libX11.so.6 libXext.so.6 libexpat.so.1 libfontconfig.so.1 libfreetype.so.6 libGL.so.1 libICE.so.6 libSM.so.6 libXmu.so.6 libXpm.so.4 libXrender.so.1 libXt.so.6"

%description
Kernel package

%description -l pl

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ltspdir}/

cd i386
cp -r {bin,etc,usr} $RPM_BUILD_ROOT%{_ltspdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,755)
%doc README
%{_ltspdir}/bin/
%attr(644,root,root)%{_ltspdir}/etc/*
%{_ltspdir}/usr/X11R6/bin/
%attr(644,root,root)%{_ltspdir}/usr/X11R6/lib/*.a
%{_ltspdir}/usr/X11R6/lib/*.so*
%attr(644,root,root)%{_ltspdir}/usr/X11R6/lib/X11/
%attr(644,root,root)%{_ltspdir}/usr/X11R6/lib/modules/
