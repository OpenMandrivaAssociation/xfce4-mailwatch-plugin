Summary:	Mail Watcher plugin for the Xfce panel
Name:		xfce4-mailwatch-plugin
Version:	1.2.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://spuriousinterrupt.org/projects/mailwatch
Source0:	http://spuriousinterrupt.org/files/mailwatch/%{name}-%{version}.tar.bz2
Patch0:		xfce4-mailwatch-plugin-1.1.0-rosa-linkage.patch
Patch1:		xfce4-mailwatch-plugin-1.1.0-rosa-gnutls3.patch
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1.0)
BuildRequires:	pkgconfig(exo-1)
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

