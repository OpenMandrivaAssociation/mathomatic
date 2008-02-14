Name:		mathomatic
Version:	12.8.6
Release:	%mkrel 1
Epoch:		0
Summary: 	General purpose CAS (Computer Algebra System)
URL:		http://mathomatic.orgserve.de/math/
Source0:	http://www.panix.com/~gesslein/mathomatic-%{version}.tar.bz2
License:	LGPL
Group:		Sciences/Mathematics
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:  desktop-file-utils
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel

%description
Mathomatic is a portable, general purpose CAS (Computer Algebra System) 
written entirely in C. It is free software (GNU LGPL license). This is a 
console mode application and library that easily compiles and runs under 
any operating system with a C compiler. There are no dependencies other 
than the standard C libraries. Mathomatic has been under development 
since 1986 and now stands at 16,000 lines of highly efficient code. The 
author is George Gesslein II.

%prep
%setup -q
%{__cat} > makefile.lib << EOF
all:
EOF
%{__mkdir_p} lib
%{__cp} -a makefile.lib lib/makefile
%{__mkdir_p} %{name}_secure
%{__mkdir_p} %{name}_secure/lib
%{__cp} -a makefile.lib %{name}_secure/lib/makefile
%{__cp} -a *.[ch] makefile VERSION %{name}_secure

%build
# build the standard version and test it
%{__sed} -e 's/-O /%{optflags} /' makefile > makefile.opt
%{make} CC=%{__cc} READLINE=1 LDFLAGS= AOUT=%{name} -f makefile.opt
%{make} CC=%{__cc} READLINE=1 LDFLAGS= AOUT=%{name} -f makefile.opt check

# build the secure version
cd %{name}_secure
%{__ln_s} ../%{name}.1 .
%{__ln_s} ../doc .
%{__ln_s} ../primes .
%{__sed} -e 's/-O /%{optflags} -DSECURE -DTIMEOUT_SECONDS=3600 /' makefile > makefile.secure
%{make} CC=%{__cc} READLINE=1 LDFLAGS= AOUT=%{name}_secure -f makefile.secure
cd ..

%install
%{__rm} -rf %{buildroot}
%makeinstall docdir=%{buildroot}%{_docdir}/%{name}
# remove the installed docs since these are picked up in %%doc already
%{__rm} -rf %{buildroot}%{_docdir}/%{name}
# remove manual since its installed already
%{__rm} -rf doc/%{name}.1
# install the secure binary
cd %{name}_secure
%{__install} -m 755 %{name}_secure %{buildroot}%{_bindir}/%{name}_secure
cd ..

%{_bindir}/desktop-file-validate %{buildroot}%{_datadir}/applications/mathomatic.desktop

%post
%{update_desktop_database}

%postun
%{clean_desktop_database}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc changes.txt COPYING README.txt VERSION doc/ tests/
%defattr(-,root,root)
%{_bindir}/%{name}
%{_bindir}/%{name}_secure
%{_mandir}/man1/mathomatic.1*
%{_datadir}/applications/mathomatic.desktop
%{_datadir}/pixmaps/mathomatic.png
