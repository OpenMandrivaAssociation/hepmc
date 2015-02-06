# hepevt symbol should be defined externally (?)
%define _disable_ld_no_undefined	1

%define name	hepmc
%define major	3
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Name:		%{name}
Group:		Sciences/Physics
License:	GPLv2+
Version:	2.06.08
Release:	2
Summary:	C++ Event Record for Monte Carlo Generators
URL:		https://savannah.cern.ch/projects/hepmc/
Source0:	http://lcgapp.cern.ch/project/simu/HepMC/download/HepMC-%{version}.tar.gz

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
%setup -q -n HepMC-%{version}

%build
autoreconf -ifs

# momentum = MEV or GEV - must select one
# length = MM or CM - must select one
# default values just using the first of the two reported available options
%configure --with-momentum=MEV --with-length=MM --enable-shared --disable-static

%make

%install
%makeinstall_std
find %{buildroot} -type f -name '*.la' -exec rm -f {} \;

mkdir -p %{buildroot}%{_docdir}/%{name}
mv -f %{buildroot}%{_datadir}/HepMC/doc/* %{buildroot}%{_docdir}/%{name}
mv -f %{buildroot}%{_datadir}/HepMC/examples %{buildroot}%{_docdir}/%{name}/examples
rmdir %{buildroot}%{_datadir}/HepMC/doc
rmdir %{buildroot}%{_datadir}/HepMC

%files		-n %{libname}
%{_libdir}/lib*.so.*

%files		-n %{devname}
%doc %{_docdir}/%{name}/
%{_libdir}/lib*.so
%{_includedir}/HepMC/


%changelog
* Fri Mar 02 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.06.08-1
+ Revision: 781755
- version update 2.0.6.08

* Fri Jan 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.06.07-1
+ Revision: 762905
- version 2.06.07

* Mon Dec 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.06.05-1
+ Revision: 737892
- Update to latest upstream release version 2.06.05

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.05.00-2mdv2011.0
+ Revision: 611092
- rebuild

* Wed Dec 02 2009 Paulo Andrade <pcpa@mandriva.com.br> 2.05.00-1mdv2010.1
+ Revision: 472724
- Import HepMC 2.05.00
- hepmc

