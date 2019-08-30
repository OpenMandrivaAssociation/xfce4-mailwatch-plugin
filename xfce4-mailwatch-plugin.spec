Summary:	Mail Watcher plugin for the Xfce panel
Name:		xfce4-mailwatch-plugin
Version:	1.2.0
Release:	4
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://spuriousinterrupt.org/projects/mailwatch
Source0:	http://spuriousinterrupt.org/files/mailwatch/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4ui-1)
BuildRequires:	pkgconfig(exo-2)
BuildRequires:	gnutls-devel
BuildRequires:	libgcrypt-devel
# required for patch0
BuildRequires:	xfce4-dev-tools
Requires:	xfce4-panel

%description
Mailwatch is a mail watcher plugin for the Xfce 4 panel.

%prep
%setup -q

%build
%xdt_autogen
%define Werror_cflags %nil

%configure \
	--disable-static \
	--enable-ssl
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_libdir}/xfce4/panel/plugins/libmailwatch.so
%{_datadir}/xfce4/panel/plugins/mailwatch.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
