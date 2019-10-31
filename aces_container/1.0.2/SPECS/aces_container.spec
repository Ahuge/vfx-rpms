#This is a basic spec for aces_container
# %define _topdir             %(echo $HOME)/_dev/vfx-rpms/%{name}/%{version}

%define debug_package %{nil}


%define name                aces_container
%define version             1.0.2
%define _topdir             %(pwd)
%define buildroot           ${_topdir}/%{name}-%{version}-root

BuildRoot:                  %{buildroot}
Summary:                    Reference Implementation of SMPTE ST2065-4 http://www.oscars.org/aces
                            # ChangeME
Name:                       %{name}
Version:                    %{version}
License:                    Custom
Release:                    1
# Source:                     https://github.com/ampas/aces_container/archive/v1.0.2.tar.gz
Source:                     %{name}-%{version}.tar.gz
Prefix:                     /usr
Group:                      Development
Requires:                   cmake

%description
This folder contains a reference implementation for an ACES container file writer intended to be used with the Academy Color Encoding System (ACES). The resulting file is compliant with the ACES container specification (SMPTE S2065-4). However, there are a few things that are not demonstrated by this reference implementation.

Stereo channels
EndOfFileFiller
Arbitrary attributes and naming validations
half type attributes
keycode value validations

%prep
%setup -q -n %{name}-%{version}

%build
. /opt/rh/devtoolset-7/enable
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT/usr/local
make

%install
cd build
make install
find $RPM_BUILD_ROOT -type f | xargs sed -i "s|$RPM_BUILD_ROOT||g"

%files
%defattr(-,root,root)
/usr/local/lib
/usr/local/include/aces
