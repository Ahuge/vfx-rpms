#This is a basic spec for ILMBase

%define name                OpenColorIO
%define name_lower_base()   OpenColorIO
%define name_lower          %{name_lower_base}
%define version             1.0.9
%define _topdir             /tmp/vfx-rpms/%{name_lower_base}/%{version}
%define buildroot           ${_topdir}/%{name_lower}-%{version}-root

%define python_version()    2.7

BuildRoot:                  %{buildroot}
Summary:                    OpenColorIO (OCIO) is a complete color management solution geared towards motion picture production with an emphasis on visual effects and computer animation. OCIO provides a straightforward and consistent user experience across all supporting applications while allowing for sophisticated back-end configuration options suitable for high-end production usage. OCIO is compatible with the Academy Color Encoding Specification (ACES) and is LUT-format agnostic, supporting many popular formats.
                            # ChangeME
License:                    Modified BSD
Name:                       %{name}
Version:                    %{version}
Release:                    3
Source:                     %{name_lower}-%{version}.tar.gz
Prefix:                     /usr
Group:                      Development/VisualEffects
Requires:                   ilmbase >= 2.3.0 

%description
OpenColorIO (OCIO) is a complete color management solution geared towards motion picture production with an emphasis on visual effects and computer animation. OCIO provides a straightforward and consistent user experience across all supporting applications while allowing for sophisticated back-end configuration options suitable for high-end production usage. OCIO is compatible with the Academy Color Encoding Specification (ACES) and is LUT-format agnostic, supporting many popular formats.

%prep
%setup -q 

%build
. /opt/rh/devtoolset-7/enable
mkdir build && cd build
cmake -DOCIO_INSTALL_EXR_PACKAGES=MISSING -DILMBASE_DIRS=/usr/local -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT/usr/local ..
make -j8

%install
cd build
make install prefix=$RPM_BUILD_ROOT/usr/local
find $RPM_BUILD_ROOT -type f | xargs sed -i "s|$RPM_BUILD_ROOT||g"

%files
%defattr(-,root,root)
/usr/local/lib
/usr/local/include
/usr/local/bin
/usr/local/share
