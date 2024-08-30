%global major 3
%global libname	%mklibname jodycode
%global devname	%mklibname jodycode -d

Summary:	Shared code used by several utilities written by Jody Bruchon
Name:		libjodycode
Version:	3.1.1
Release:	1
Group:		System/Libraries
License:	MIT
URL:		https://codeberg.org/jbruchon/libjodycode/
Source0:	https://codeberg.org/jbruchon/%{name}/archive/v%{version}.tar.gz

%description
libjodycode is a software code library containing code shared among
several of the programs written by Jody Bruchon such as imagepile,
jdupes, winregfs, and zeromerge. These shared pieces of code were
copied between each program as they were updated. As the number of
programs increased and keeping these pieces of code synced became more
annoying, the decision was made to combine all of them into a single
reusable shared library.

#-----------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared code used by several utilities written by Jody Bruchon
Group:		System/Libraries

%description -n %{libname}
libjodycode is a software code library containing code shared among
several of the programs written by Jody Bruchon such as imagepile,
jdupes, winregfs, and zeromerge. These shared pieces of code were
copied between each program as they were updated. As the number of
programs increased and keeping these pieces of code synced became more
annoying, the decision was made to combine all of them into a single
reusable shared library.

%files -n %{libname}
%license LICENSE.txt
%doc CHANGES.txt README.md
%{_libdir}/%{name}.so.%{major}*
%{_mandir}/man7/%{name}.7.*

#-----------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel
Provides:	jodycode-devel

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%files -n %{devname}
%{_includedir}/libjodycode.h
%{_libdir}/libjodycode.so

#-----------------------------------------------------------------------

%prep
%autosetup -n %{name}

%build
#configure
%set_build_flags
%make_build HARDEN=1 PREFIX="%{_prefix}" LIB_DIR="%{_libdir}"

%install
%make_install HARDEN=1 PREFIX="%{_prefix}" LIB_DIR="%{_libdir}"

# remove static
rm -f %{buildroot}%{_libdir}/%{name}*.a

