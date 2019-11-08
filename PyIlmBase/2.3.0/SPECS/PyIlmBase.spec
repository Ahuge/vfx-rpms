#This is a basic spec for ILMBase

%define name                PyIlmBase
%define name_lower_base()   PyIlmBase
%define name_lower          %{name_lower_base}
%define version             2.3.0
%define _topdir             %(pwd)
# %define _topdir             /tmp/vfx-rpms/%{name_lower_base}/%{version}
%define buildroot           ${_topdir}/%{name_lower}-%{version}-root

BuildRoot:                  %{buildroot}
Summary:                    Python Bindings for ILMBase
                            # ChangeME
License:                    Modified BSD
Name:                       %{name}
Version:                    %{version}
Release:                    10
Source:                     %{name_lower}-%{version}.tar.gz
Prefix:                     /usr
Group:                      Development/VisualEffects
Requires:                   boost-python IlmBase >= %{version} python

%description

%prep
%setup -q -n %{name_lower}-%{version}

%build
. /opt/rh/devtoolset-7/enable
pip install numpy==1.16.3
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/lib:/usr/lib:/usr/local/lib64:/usr/lib64"
./bootstrap
./configure --with-ilmbase-prefix=/usr/local
make

%install
make install prefix=$RPM_BUILD_ROOT/usr/local

%files
%defattr(-,root,root)
/usr/local/lib
/usr/local/include
/usr/local/lib64
/usr/local/share
