%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname   mate-file-manager-image-converter

Summary:	Caja extension to mass resize images
Name:		caja-image-converter
Version:	1.6.0
Release:	2
Group:		Graphical desktop/Other
License:	GPLv2+
URL:		https://pub.mate-desktop.org
Source0:    http://pub.mate-desktop.org/releases/%{url_ver}/%{oname}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libcaja-extension)

Requires:	imagemagick
Requires:	%{_lib}caja-extension1 >= 1.6.0

%rename %{oname}

%description
Adds a "Resize Images..." menu item to the context menu of all images. This
opens a dialog where you set the desired image size and file name. A click
on "Resize" finally resizes the image(s) using ImageMagick's convert tool.

%prep
%setup -q -n %{oname}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING
%{_datadir}/caja-image-converter
%{_libdir}/caja/extensions-2.0/*.so

