%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-8

Name:           libnvjitlink
Epoch:          1
Version:        12.8.61
Release:        1%{?dist}
Summary:        NVIDIA compiler library for JIT LTO functionality
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-x86_64/%{name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-sbsa/%{name}-linux-sbsa-%{version}-archive.tar.xz
Source3:        nvjitlink.pc

Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
NVJIT link compiler LTO functionality native runtime library.
Just-in-time link-time-optimization (JIT LTO) allows developers to proved
runtime linking of specialized kernel functions with no-call overhead.

%package devel
Summary:        Development files for NVIDIA compiler library for JIT LTO functionality
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
This package provides development files for the CUDA NVIDIA compiler library for
JIT LTO functionality.

%package static
Summary:        Static libraries for NVIDIA compiler library for JIT LTO functionality
Requires:       %{name}-devel%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description static
This package contains static libraries for NVIDIA compiler library for JIT LTO
functionality.

%prep
%ifarch x86_64
%setup -q -n %{name}-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{name}-linux-sbsa-%{version}-archive
%endif

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig/

cp -fr include/* %{buildroot}%{_includedir}/
cp -fr lib/lib* %{buildroot}%{_libdir}/
cp -fr %{SOURCE3} %{buildroot}/%{_libdir}/pkgconfig/

# Set proper variables
sed -i \
    -e 's|CUDA_VERSION|%{version}|g' \
    -e 's|LIBDIR|%{_libdir}|g' \
    -e 's|INCLUDE_DIR|%{_includedir}|g' \
    %{buildroot}/%{_libdir}/pkgconfig/*.pc

%files
%license LICENSE
%{_libdir}/libnvJitLink.so.*

%files devel
%{_includedir}/nvJitLink.h
%{_libdir}/libnvJitLink.so
%{_libdir}/pkgconfig/nvjitlink.pc

%files static
%{_libdir}/libnvJitLink_static.a

%changelog
* Fri Feb 07 2025 Simone Caronni <negativo17@gmail.com> - 1:12.8.61-1
- Update to 12.8.61.

* Fri Dec 13 2024 Simone Caronni <negativo17@gmail.com> - 1:12.6.85-1
- Update to 12.6.85.

* Thu Sep 19 2024 Simone Caronni <negativo17@gmail.com> - 1:12.6.68-1
- Update to 12.6.68.

* Thu Jul 11 2024 Simone Caronni <negativo17@gmail.com> - 1:12.5.82-1
- Update to 12.5.82.

* Tue Mar 12 2024 Simone Caronni <negativo17@gmail.com> - 1:12.4.99-1
- Update to 12.4.99.
- Drop ppc64le.

* Tue Nov 28 2023 Simone Caronni <negativo17@gmail.com> - 1:12.3.101-1
- Update to 12.3.101.

* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 1:12.2.140-1
- Update to 12.2.140.

* Tue Jul 11 2023 Simone Caronni <negativo17@gmail.com> - 1:12.2.91-1
- Update to 12.2.91.

* Thu Jun 08 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.105-1
- Update to 12.1.105.

* Tue Apr 11 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.55-1
- Update to 12.1.55.

* Sat Feb 25 2023 Simone Caronni <negativo17@gmail.com> - 1:12.0.140-1
- Update to 12.0.140.

* Fri Dec 16 2022 Simone Caronni <negativo17@gmail.com> - 1:12.0.76-1
- First build.
