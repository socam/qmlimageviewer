
Summary: A simple yet powerful image viewer for X11.
Name: qmlimageviewer
Version: 1.0
Source: %{name}-%{version}.tgz
Release: 1%{?dist}
License: Fidesol
Group: Multimedia/Graphics

%description
SOCAM Image viewer

%prep
%setup -q -n %{name}-%{version}

%build


%install
mkdir -p %{buildroot}/opt/socam
cp  %{_builddir}/%{name}-%{version}/socam_iv.qml  %{buildroot}/opt/socam

mkdir -p %{buildroot}/usr/share/applications
cp  %{_builddir}/%{name}-%{version}/socam_iv.desktop  %{buildroot}/usr/share/applications


%files
%defattr(-,root,root)
/opt/socam/socam_iv.qml
/usr/share/applications/socam_iv.desktop

%changelog
