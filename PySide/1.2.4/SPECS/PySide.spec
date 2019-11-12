#This is a basic spec for PySide
# %define _topdir             /tmp/vfx-rpms/%{name}/%{version}
%define debug_package %{nil}

%define name                PySide
%define version             1.2.4
%define _topdir             %(pwd)
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
if ! [ -d $RPM_BUILD_ROOT ]; then
    mkdir $RPM_BUILD_ROOT
fi

%install
. /opt/rh/devtoolset-7/enable
pip2 install --ignore-installed -t "$RPM_BUILD_ROOT/usr/local" PySide --isolated --verbose --no-binary :all:
mkdir -p "$RPM_BUILD_ROOT/usr/local/lib64/python2.7/site-packages/"
mv "$RPM_BUILD_ROOT/usr/local/PySide" "$RPM_BUILD_ROOT/usr/local/lib64/python2.7/site-packages/"
mv "$RPM_BUILD_ROOT/usr/local/PySide-1.2.4-py2.7.egg-info" "$RPM_BUILD_ROOT/usr/local/lib64/python2.7/site-packages/"
mv "$RPM_BUILD_ROOT/usr/local/pysideuic" "$RPM_BUILD_ROOT/usr/local/lib64/python2.7/site-packages/"

%files
%defattr(-,root,root)
/usr/local/bin
/usr/local/lib64/python2.7/site-packages/PySide
/usr/local/lib64/python2.7/site-packages/PySide-1.2.4-py2.7.egg-info
/usr/local/lib64/python2.7/site-packages/pysideuic
