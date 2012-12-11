Summary:	Mail Watcher plugin for the Xfce panel
Name:		xfce4-mailwatch-plugin
Version:	1.1.0
Release:	6
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://spuriousinterrupt.org/projects/mailwatch
Source0:	http://spuriousinterrupt.org/files/mailwatch/%{name}-%{version}.tar.bz2
Patch0:		xfce4-mailwatch-plugin-1.1.0-rosa-linkage.patch
Patch1:		xfce4-mailwatch-plugin-1.1.0-rosa-gnutls3.patch
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	pkgconfig(libxfcegui4-1.0) >= 4.4.2
BuildRequires:	gnutls-devel
BuildRequires:	libgcrypt-devel
# required for patch0
BuildRequires:	xfce4-dev-tools
Requires:	xfce4-panel >= 4.4.2

%description
Mailwatch is a mail watcher plugin for the Xfce 4 panel.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
xdt-autogen
%define Werror_cflags %nil

%configure2_5x \
	--disable-static \
	--enable-ssl
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_libdir}/xfce4/panel-plugins/%{name}
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*.png


%changelog
* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-5mdv2010.1
+ Revision: 543428
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0-4mdv2010.0
+ Revision: 446058
- rebuild

* Sun Mar 22 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-3mdv2009.1
+ Revision: 360391
- disable checks for format-strings

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-2mdv2009.1
+ Revision: 294998
- rebuild for new Xfce4.6 beta1

* Tue Sep 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-1mdv2009.0
+ Revision: 285103
- update to new version 1.1.0
- add missing buildrequires on gnutls-devel

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-9mdv2009.0
+ Revision: 262360
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-8mdv2009.0
+ Revision: 256872
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix description

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-6mdv2008.1
+ Revision: 110560
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING
- use upstream name

* Fri Jun 22 2007 Thierry Vignaud <tv@mandriva.org> 1.0.1-5mdv2008.0
+ Revision: 43193
- fix group

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 1.0.1-4mdv2008.0
+ Revision: 36545
- rebuild with correct optflags

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - fix path

* Sun Jun 03 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-1mdv2008.0
+ Revision: 34779
- update to latest version
- spec file clean

