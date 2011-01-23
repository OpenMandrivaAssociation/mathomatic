Name:		mathomatic
Version:	15.4.1
Release:	%mkrel 1
Epoch:		0
Summary: 	General purpose CAS (Computer Algebra System)
URL:		http://mathomatic.orgserve.de/math/
Source0:	http://www.panix.com/~gesslein/%{name}-%{version}.tar.bz2
License:	LGPLv2
Group:		Sciences/Mathematics
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:  desktop-file-utils
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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
%{__sed} -e 's/-O3 /%{optflags} /' makefile > makefile.opt
%{make} CC=%{__cc} READLINE=1 LDFLAGS="%{ldflags}" AOUT=%{name} -f makefile.opt
%{make} CC=%{__cc} READLINE=1 LDFLAGS="%{ldflags}" AOUT=%{name} -f makefile.opt check
cd %{name}_secure
%{__ln_s} ../%{name}.1 .
%{__ln_s} ../doc .
%{__ln_s} ../primes .
%{__sed} -e 's/-O3 /%{optflags} -DSECURE -DTIMEOUT_SECONDS=3600 /' makefile > makefile.secure
%{make} CC=%{__cc} READLINE=1 LDFLAGS="%{ldflags}" AOUT=%{name}_secure -f makefile.secure
cd ..

%install
%{__rm} -rf %{buildroot}
%makeinstall docdir=%{buildroot}%{_docdir}/%{name}
%{__rm} -rf %{buildroot}%{_docdir}/%{name}
%{__rm} -rf doc/%{name}.1
cd %{name}_secure
%{__install} -m 755 %{name}_secure %{buildroot}%{_bindir}/%{name}_secure
cd ..
%{_bindir}/desktop-file-validate %{buildroot}%{_datadir}/applications/mathomatic.desktop
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc changes.txt README.txt VERSION doc/ tests/
%defattr(-,root,root)
%{_bindir}/%{name}
%{_bindir}/%{name}_secure
%{_mandir}/man1/mathomatic.1*
%{_datadir}/applications/mathomatic.desktop
%{_datadir}/pixmaps/mathomatic.png
%{_datadir}/pixmaps/mathomatic.xpm
