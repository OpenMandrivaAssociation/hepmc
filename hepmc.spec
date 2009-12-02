# hepevt symbol should be defined externally (?)
%define _disable_ld_no_undefined	1

%define name	hepmc
%define major	3
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Name:		%{name}
Group:		Sciences/Physics
License:	GPLv2+
Version:	2.05.00
Release:	%mkrel 1
Summary:	C++ Event Record for Monte Carlo Generators
URL:		https://savannah.cern.ch/projects/hepmc/
Source0:	http://lcgapp.cern.ch/project/simu/HepMC/download/HepMC-2.05.00.tar.gz
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
%setup -q -n HepMC-2.05.00

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
mv -f %{buildroot}/usr/doc/HepMC/* %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}/examples
mv -f %{buildroot}/usr/examples/HepMC/* %{buildroot}%{_datadir}/%{name}/examples

%clean
rm -fr %{buildroot}

%files		-n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files		-n %{devname}
%defattr(-,root,root)
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%dir %{_includedir}/HepMC
%{_includedir}/HepMC/*
