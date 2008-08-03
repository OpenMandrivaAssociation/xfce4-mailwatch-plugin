Summary:	Mail Watcher plugin for the Xfce panel
Name:		xfce4-mailwatch-plugin
Version:	1.0.1
Release:	%mkrel 9
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://spuriousinterrupt.org/projects/mailwatch
Source0:	http://spuriousinterrupt.org/files/mailwatch/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel  >= 4.4.2
Requires:	xfce4-panel >= 4.4.2
Obsoletes:	xfce-mailwatch-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Mailwatch is a mail watcher plugin for the Xfce 4 panel.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--enable-ssl
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%post
%if %mdkversion < 200900
%{update_menus}
%endif
%clean_icon_cache hicolor

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/xfce4/panel-plugins/%{name}
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*.png
