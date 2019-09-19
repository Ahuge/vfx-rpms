#This is a basic spec for ILMBase

%define name                OpenImageIO
%define name_lower_base()   OpenImageIO
%define name_lower          %{name_lower_base}
%define version             1.8.17
%define _topdir             /tmp/vfx-rpms/%{name_lower_base}/%{version}
%define buildroot           ${_topdir}/%{name_lower}-%{version}-root

%define python_version()    2.7

BuildRoot:                  %{buildroot}
Summary:                    OIIO is a high dynamic-range (HDR) image file format
                            # ChangeME
License:                    Modified BSD
Name:                       %{name}
Version:                    %{version}
Release:                    2
Source:                     %{name_lower}-%{version}.tar.gz
Prefix:                     /usr
Group:                      Development/VisualEffects
Requires:                   zlib IlmBase OpenEXR LibRaw python

%description
OpenImageIO provides simple but powerful ImageInput and ImageOutput APIs that abstract the reading and writing of 2D image file formats. 
They don’t support every possible way of encoding images in memory, but for a reasonable and common set of desired functionality, they provide an exceptionally easy way for an application using the APIs support a wide — and extensible — selection of image formats without knowing the details of any of these formats.

%prep
%setup -q -n %{name_lower}-%{version}

%build
. /opt/rh/devtoolset-7/enable
env LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib:/usr/lib64:/usr/local/lib:/usr/local/lib64" \
    CPATH="$CPATH:/usr/include:/usr/local/include" \
    make PYTHON_VERSION=%{python_version}

%install
[[ -d $RPM_BUILD_ROOT/usr/local ]] || mkdir $RPM_BUILD_ROOT/usr/local -p
echo $PWD
ls $PWD/dist
ls $PWD/dist/linux64
cp -R $PWD/dist/linux64/* $RPM_BUILD_ROOT/usr/local

%files
%defattr(-,root,root)
/usr/local/bin
/usr/local/lib64
/usr/local/include
/usr/local/share
