#This is a basic spec for ILMBase

%define name                OpenEXRVFX
%define name_lower_base()   openexr
%define name_lower          %{name_lower_base}VFX
%define version             2.3.0
%define _topdir             /tmp/vfx-rpms/%{name_lower_base}/%{version}
%define buildroot           ${_topdir}/%{name_lower}-%{version}-root

BuildRoot:                  %{buildroot}
Summary:                    OpenEXR is a high dynamic-range (HDR) image file format
                            # ChangeME
License:                    Modified BSD
Name:                       %{name}
Version:                    %{version}
Release:                    2
Source:                     %{name_lower}-%{version}.tar.gz
Prefix:                     /usr
Group:                      Development/VisualEffects
Requires:                   zlib ilmbaseVFX >= %{version}

%description
OpenEXR is a high dynamic-range (HDR) image file format developed by Industrial Light & Magic for use in computer imaging applications.

OpenEXR is used by ILM on all motion pictures currently in production. The first movies to employ OpenEXR were Harry Potter and the Sorcerers Stone, Men in Black II, Gangs of New York, and Signs. Since then, OpenEXR has become ILM's main image file format.

OpenEXR's features include:
    - Higher dynamic range and color precision than existing 8- and 10-bit image file formats.
    - Support for 16-bit floating-point, 32-bit floating-point,   and 32-bit integer pixels. The 16-bit floating-point format, called "half", is compatible with the half data type in NVIDIA's Cg graphics language and is supported natively on their new GeForce FX and Quadro FX 3D graphics solutions.
    - Multiple image compression algorithms, both lossless and lossy. Some of the included codecs can achieve 2:1 lossless compression ratios on images with film grain. The lossy codecs have been tuned for visual quality and decoding performance.
    - Extensibility. New compression codecs and image types can easily be added by extending the C++ classes included in the OpenEXR software distribution. New image attributes (strings, vectors, integers, etc.) can be added to OpenEXR image headers without affecting backward compatibility with existing OpenEXR applications.
    - Deep Data. Pixels can store a variable length list of samples. The main rationale behind deep-images is to store multiple values at different depths for each pixel. Support for hard surface and volumetric representation requirements for deep compositing workflows.
    - Multi-part image files. Files can contain a number of separate, but related, images in one file. Access to any part is independent of the others; in particular, no access of data need take place for unrequested parts.

ILM has released OpenEXR as free software. The OpenEXR software distribution includes:
    - IlmImf, a library that reads and writes OpenEXR images.
    - IlmImfUtil, a convenience library to simplify development of OpenEXR utilities.
    - Half, a C++ class for manipulating half values as if they were a built-in C++ data type.
    - Imath, a math library with support for matrices, 2d- and 3d-transformations, solvers for linear/quadratic/cubic equations, and more.
    - exrdisplay, a sample application for viewing OpenEXR images on a display at various exposure settings.

%prep
%setup -q -n %{name_lower}-%{version}

%build
. /opt/rh/devtoolset-7/enable
env LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib:/usr/local/lib" CPATH="$CPATH:/usr/include:/usr/local/include" ./configure  --with-ilmbase-prefix=/usr/local
make

%install
make install prefix=$RPM_BUILD_ROOT/usr/local

%files
%defattr(-,root,root)
/usr/local/lib
/usr/local/include
/usr/local/bin
/usr/local/share
