Name:		mathomatic
Version:	16.0.2
Release:	1
Summary:	General purpose CAS (Computer Algebra System)
URL:		http://mathomatic.org/
Source0:	http://mathomatic.org/%{name}-%{version}.tar.bz2
License:	LGPLv2
Group:		Sciences/Mathematics
BuildRequires:	desktop-file-utils
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel

%description
Mathomatic™ is a portable, command-line CAS and calculator software, written
entirely in the C programming language. It is free and open source software
(FOSS), published under the GNU Lesser General Public License (LGPL version
2.1), and has been under continual development since 1986. The software can
symbolically solve, simplify, combine, and compare algebraic equations,
simultaneously performing generalized standard, complex number, modular,
and polynomial arithmetic, as needed. It does some calculus and is very easy
to learn and use.

Mathomatic consists of both a text-mode symbolic math application,
and a symbolic math library, each suitable for desktops, laptops, servers,
handhelds, and embedded systems.

%prep
%setup -q
%__cat > makefile.lib << EOF
all:
EOF
%__mkdir_p lib
%__cp -a makefile.lib lib/makefile
%__mkdir_p %{name}_secure
%__mkdir_p %{name}_secure/lib
%__cp -a makefile.lib %{name}_secure/lib/makefile
%__cp -a *.[ch] makefile VERSION %{name}_secure

%build
%make CC=%{__cc} CC_OPTIMIZE="%{optflags}" READLINE=1 LDFLAGS="%{ldflags}" AOUT=%{name}
pushd %{name}_secure
%__ln_s ../%{name}.1 .
%__ln_s ../rmath.1 .
%__ln_s ../doc .
%__ln_s ../primes .
%make CC=%{__cc} CC_OPTIMIZE="%{optflags}" READLINE=1 LDFLAGS="%{ldflags}" AOUT=%{name}_secure %{name}_secure
popd

%check
%make CC=%{__cc} CC_OPTIMIZE="%{optflags}" READLINE=1 LDFLAGS="%{ldflags}" AOUT=%{name} check

%install
%makeinstall docdir=%{buildroot}%{_docdir}/%{name}
%__rm -rf %{buildroot}%{_docdir}/%{name}
%__rm -rf doc/%{name}.1
cd %{name}_secure
%__install -m 755 %{name}_secure %{buildroot}%{_bindir}/%{name}_secure
cd ..
%{_bindir}/desktop-file-validate %{buildroot}%{_datadir}/applications/mathomatic.desktop

%files
%defattr(0644,root,root,0755)
%doc NEWS README.txt VERSION doc/ tests/
%defattr(-,root,root)
%{_bindir}/%{name}
%{_bindir}/%{name}_secure
%{_mandir}/man1/mathomatic.1*
%{_datadir}/applications/mathomatic.desktop
%{_datadir}/pixmaps/mathomatic.png
%{_datadir}/pixmaps/mathomatic.xpm
