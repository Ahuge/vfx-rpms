#This is a basic spec for PySide
%define debug_package %{nil}


%define name                PySide
%define version             1.2.4
%define _topdir             %(pwd)
# %define _topdir             /tmp/vfx-rpms/%{name}/%{version}
%define buildroot           ${_topdir}/%{name}-%{version}-root

BuildRoot:                  %{buildroot}
Summary:                    Python Bindings for Qt4
                            # ChangeME
License:                    Modified BSD
Name:                       %{name}
Version:                    %{version}
Release:                    1
Source:                     %{name}-%{version}.tar.gz
Prefix:                     /usr
Group:                      Development
Requires:                   python-devel qt-devel cmake python-pip

%description
Python bindings for the Qt C++ library for Qt 4.8.5

%prep
%setup -q -n %{name}-%{version}

%build
. /opt/rh/devtoolset-7/enable
pip2 install --install-option="--prefix=$RPM_BUILD_ROOT" PySide

%install
tree ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
/usr/lib
/usr/bin
