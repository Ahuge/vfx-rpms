#This is a basic spec for ILMBase

%define _base()             IlmBase
%define name                %{_base}
%define version             2.3.0
%define _topdir             %(pwd)
# %define _topdir             /tmp/vfx-rpms/%{_base}/%{version}
%define buildroot           %{_topdir}/%{name}-%{version}-root

BuildRoot:                  %{buildroot}
Summary:                    ILMBase libraries
                            # ChangeME
License:                    Modified BSD
Name:                       %{name}
Version:                    %{version}
Release:                    10
Source:                     %{name}-%{version}.tar.gz
Prefix:                     /usr
Group:                      Development/Visual Effects

%description
ILMBase is a set of libraries used most often by OpenEXR

%prep
%setup -q

%build
. /opt/rh/devtoolset-7/enable
./configure
make

%install
make install prefix=$RPM_BUILD_ROOT/usr/local

%files
%defattr(-,root,root)
/usr/local/lib
/usr/local/include
