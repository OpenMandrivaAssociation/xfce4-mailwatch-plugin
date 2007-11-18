%define oname xfce4-mailwatch-plugin

Summary:	Mail Watcher plugin for the Xfce panel
Name:		xfce-mailwatch-plugin
Version:	1.0.1
Release:	%mkrel 5
License:	GPL
Group:		Graphical desktop/Xfce
URL:		http://spuriousinterrupt.org/projects/mailwatch
Source0:	http://spuriousinterrupt.org/files/mailwatch/%{oname}-%{version}.tar.bz2
BuildRequires:	xfce-panel-devel >= 4.4.1
BuildRequires:	libxfcegui4-devel
Requires:	xfce-panel >= 4.4.1
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Mailwatch is a plugin for the Xfce 4 panel. It is intended to replace the 
current (4.0, 4.2) mail checker plugin in Xfce 4.4.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x \
	--disable-static \
	--enable-ssl
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{oname}

%post
%{update_menus}
%clean_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/xfce4/panel-plugins/%{oname}
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*.png
