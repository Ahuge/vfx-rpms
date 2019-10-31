#This is a basic spec for aces_container
# %define _topdir             %(echo $HOME)/_dev/vfx-rpms/%{name}/%{version}

# %define debug_package %{nil}


%define name                ctl
%define version             1.5.2
%define _topdir             %(pwd)
%define buildroot           ${_topdir}/%{name}-%{version}-root

BuildRoot:                  %{buildroot}
Summary:                    The Color Transformation Language (CTL)
                            # ChangeME
Name:                       %{name}
Version:                    %{version}
License:                    Custom
Release:                    1
Source:                     %{name}-%{version}.tar.gz
Prefix:                     /usr
Group:                      Development
Requires:                   cmake IlmBase OpenEXR libtiff aces_container

%description
The Color Transformation Language, or CTL, is a programming language for digital color management.

Digital color management requires translating digital images between different representations or color spaces. For example, the pixels in an image may encode the colors that should be seen when the image is displayed on a video monitor. Printing this image on paper, or recording it on motion picture film requires transforming the pixels to an appropriate representation: Video, inks on paper and film all have different color gamuts and dynamic ranges. Color mixing is additive for video, but subtractive for inks and film. Video and film typically use three color channels, while four or more inks are used for printing on paper. A color management system must transform each pixel in the original image to corresponding amounts of ink or film density values.

The details of how each pixel is transformed can be fairly complex, and they are often subject to artistic decisions. When images are exchanged between different parties, it is desirable to exchange exact descriptions of appropriate color transforms along with the digital image files. Two people in different geographical locations may each have a copy of the same digital image file. When one of them prints the image on paper, he or she wants to be sure that the result is the same as as for the other person. In order to achieve identical results, the two must agree on details of the printing process (for example, inks and paper), and they must agree on the transform that converts pixels in the file into amounts of ink on paper. Of course, this requires a description of the transform.

The Color Transformation Language, or CTL, is a small programming language that was designed to serve as a building block for digital color management systems. CTL allows users to describe color transforms in a concise and unambiguous way by expressing them as programs. In order to apply a given transform to an image, the color management system instructs a CTL interpreter to load and run the CTL program that describes the transform. The original and the transformed image constitute the CTL program's input and output.

Color transforms can be shared by distributing CTL programs. Two parties with the same CTL program can apply the same transform to an image.

%prep
%setup -q -n %{name}-%{version}

%build
. /opt/rh/devtoolset-6/enable
# Patch for https://github.com/ampas/CTL/pull/73
find . -type f -exec sed -i 's/inst->lineNumber() << ": " << e);/inst->lineNumber() << ": " << e.what());/g' {} +
# find . -type f -exec sed -i 's/add_library( ctldpx/add_library( ctldpx ${DO_SHARED}/g' {} +

mkdir build && cd build
cmake .. # -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT/usr/local
make

%install
. /opt/rh/devtoolset-6/enable
cd build
make DESTDIR=$RPM_BUILD_ROOT install
set +e
find "%{buildroot}" -type f -name "*.so" | while read so_file
do
    strip --strip-debug "$so_file"
done
set -e
# find $RPM_BUILD_ROOT -type f | xargs sed -i “s|$RPM_BUILD_ROOT||g”
# find $RPM_BUILD_ROOT -type f | xargs sed -i "s|$RPM_BUILD_ROOT||g"

%files
%defattr(-,root,root)
/usr/local/lib
/usr/local/bin
/usr/local/include
/usr/local/doc

