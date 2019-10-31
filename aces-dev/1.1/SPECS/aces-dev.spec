#This is a basic spec for aces_container
# %define _topdir             %(echo $HOME)/_dev/vfx-rpms/%{name}/%{version}

%define debug_package %{nil}

%define name                aces-dev
%define version             1.1
%define _topdir             %(pwd)
%define buildroot           ${_topdir}/%{name}-%{version}-root

BuildRoot:                  %{buildroot}
Summary:                    AMPAS Academy Color Encoding System Developer Resources http://www.oscars.org/aces
                            # ChangeME
Name:                       %{name}
Version:                    %{version}
License:                    Custom
Release:                    1
Source:                     %{name}-%{version}.tar.gz
Prefix:                     /usr/local/share
Group:                      Development
Requires:                   cmake ctl

%description
The Academy Color Encoding System (ACES) is a set of components that facilitates a wide range of motion picture and television workflows while eliminating the ambiguity of legacy file formats. The system is designed to support both all-digital and hybrid film-digital motion picture workflows.

The basic ACES components are:

Color encoding and metric specifications, file format specifications, color transformations, and an open source reference implementation
A set of reference images and calibration targets for film scanners and recorders
Documentation on the system and software tools
This toolkit is intended to serve as a distribution mechanism for key components of the system, including the reference implementation transforms, reference images, and documentation.

%prep
%setup -q -n %{name}-%{version}

%build
find . -type f -exec sed -i 's/\"\"\"\"/\"\"\"/g' {} +
find . -type f -exec sed -i 's/\t/    /g' {} +

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/share/aces-dev
cp -R documents images transforms LICENSE.md $RPM_BUILD_ROOT/usr/local/share/aces-dev/

%files
%defattr(-,root,root)
/usr/local/share/aces-dev
