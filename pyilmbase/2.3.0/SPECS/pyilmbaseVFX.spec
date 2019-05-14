#This is a basic spec for ILMBase

%define name                PyIlmBaseVFX
%define name_lower_base()   pyilmbase
%define name_lower          %{name_lower_base}VFX
%define version             2.3.0
%define _topdir             /tmp/vfx-rpms/%{name_lower_base}/%{version}
%define buildroot           ${_topdir}/%{name_lower}-%{version}-root

BuildRoot:                  %{buildroot}
Summary:                    Python Bindings for ILMBaseVFX
                            # ChangeME
License:                    Modified BSD
Name:                       %{name}
Version:                    %{version}
Release:                    2
Source:                     %{name_lower}-%{version}.tar.gz
Prefix:                     /usr
Group:                      Development/VisualEffects
Requires:                   boost-python ilmbaseVFX >= %{version}

%description

%prep
%setup -q -n %{name_lower}-%{version}

%build
. /opt/rh/devtoolset-7/enable
pip install numpy
env LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib:/usr/local/lib" CPATH="$CPATH:/usr/include:/usr/local/include" ./configure --disable-namespaceversioning --with-ilmbase-prefix=/usr/local
make

%install
make install prefix=$RPM_BUILD_ROOT/usr/local

%files
%defattr(-,root,root)
/usr/local/lib
/usr/local/include
/usr/local/lib64
/usr/local/share
