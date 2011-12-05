# hepevt symbol should be defined externally (?)
%define _disable_ld_no_undefined	1

%define name	hepmc
%define major	3
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Name:		%{name}
Group:		Sciences/Physics
License:	GPLv2+
Version:	2.06.05
Release:	%mkrel 1
Summary:	C++ Event Record for Monte Carlo Generators
URL:		https://savannah.cern.ch/projects/hepmc/
Source0:	http://lcgapp.cern.ch/project/simu/HepMC/download/HepMC-2.06.05.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The HepMC package is an object oriented event record written in C++ for
High Energy Physics Monte Carlo Generators. Many extensions from HEPEVT,
the Fortran HEP standard, are supported: the number of entries is unlimited,
spin density matrices can be stored with each vertex, flow patterns
(such as color) can be stored and traced, integers representing random
number generator states can be stored, and an arbitrary number of event
weights can be included. Particles and vertices are kept separate in a
graph structure, physically similar to a physics event. The added
information supports the modularisation of event generators. The package
has been kept as simple as possible with minimal internal/external
dependencies. Event information is accessed by means of iterators supplied
with the package.

Reference: M. Dobbs and J.B. Hansen, Comput. Phys. Commun. 134 (2001) 41.

%package	-n %{libname}
Summary:	C++ Event Record for Monte Carlo Generators
Group:		System/Libraries
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description	-n %{libname}
The HepMC package is an object oriented event record written in C++ for
High Energy Physics Monte Carlo Generators. Many extensions from HEPEVT,
the Fortran HEP standard, are supported: the number of entries is unlimited,
spin density matrices can be stored with each vertex, flow patterns
(such as color) can be stored and traced, integers representing random
number generator states can be stored, and an arbitrary number of event
weights can be included. Particles and vertices are kept separate in a
graph structure, physically similar to a physics event. The added
information supports the modularisation of event generators. The package
has been kept as simple as possible with minimal internal/external
dependencies. Event information is accessed by means of iterators supplied
with the package.

Reference: M. Dobbs and J.B. Hansen, Comput. Phys. Commun. 134 (2001) 41.

%package	-n %{devname}
Summary:	HepMC development files
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description	-n %{devname}
HepMC development files.

%prep
%setup -q -n HepMC-2.06.05

%build
autoreconf -ifs

# momentum = MEV or GEV - must select one
# length = MM or CM - must select one
# default values just using the first of the two reported available options
%configure --with-momentum=MEV --with-length=MM --enable-shared --disable-static

%make

%install
%makeinstall_std
mkdir -p %{buildroot}%{_docdir}/%{name}
mv -f %{buildroot}%{_datadir}/HepMC/doc/* %{buildroot}%{_docdir}/%{name}
mv -f %{buildroot}%{_datadir}/HepMC/examples %{buildroot}%{_docdir}/%{name}/examples
rmdir %{buildroot}%{_datadir}/HepMC/doc
rmdir %{buildroot}%{_datadir}/HepMC

%clean
rm -fr %{buildroot}

%files		-n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files		-n %{devname}
%defattr(-,root,root)
%doc %{_docdir}/%{name}/
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/HepMC/
