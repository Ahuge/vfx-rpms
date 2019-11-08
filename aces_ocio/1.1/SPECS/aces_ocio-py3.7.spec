#This is a basic spec for aces_container
# %define _topdir             %(echo $HOME)/_dev/vfx-rpms/%{name}/%{version}

%define debug_package %{nil}

%define name                aces_ocio-py3.7
%define version             1.1
%define _topdir             %(pwd)
%define buildroot           ${_topdir}/%{name}-%{version}-root

BuildRoot:                  %{buildroot}
Summary:                    ACES ocio configs
                            # ChangeME
Name:                       %{name}
Version:                    %{version}
License:                    Custom
Release:                    1
Source:                     aces_ocio-%{version}.tar.gz
Prefix:                     /usr/local
Group:                      Development
Requires:                   cmake ctl

%description
aces_ocio is a OpenColorIO Color Configuration set to the AMPAS ACES standard

%prep
%setup -q -n aces_ocio-%{version}


%install
pip3 install --install-option="--prefix=$RPM_BUILD_ROOT/usr/local" --verbose .

%files
%defattr(-,root,root)
/usr/local/lib/python3.7/site-packages/aces_ocio-1.0.1-py3.7.egg-info
/usr/local/lib/python3.7/site-packages/aces_ocio
/usr/local/bin/create_aces_config
/usr/local/bin/generate_lut
/usr/local/bin/tests_aces_config
