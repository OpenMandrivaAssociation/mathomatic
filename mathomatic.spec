Name:		mathomatic
Version:	16.0.5
Release:	2
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


%changelog
* Sun Sep 09 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 16.0.3-1
+ Revision: 816618
- update to 16.0.3
- update to 16.0.2

* Mon Jul 23 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 16.0.1-1
+ Revision: 810631
- update to 16.0.1

* Mon Jul 02 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 16.0.0-1
+ Revision: 807779
- update to 16.0.0

* Wed Jun 06 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 15.8.5-1
+ Revision: 802988
- update to 15.8.5

* Fri May 11 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 15.8.4-1
+ Revision: 798189
- update to 15.8.4

* Tue Apr 17 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 15.8.2-1
+ Revision: 791450
- update to 15.8.2

* Fri Mar 02 2012 Alexander Khrukin <akhrukin@mandriva.org> 0:15.8.0-1
+ Revision: 781770
- version update 15.8.0

* Thu Dec 22 2011 Andrey Bondrov <abondrov@mandriva.org> 0:15.7.2-1
+ Revision: 744465
- New version 15.7.2

* Sun Jun 12 2011 Funda Wang <fwang@mandriva.org> 0:15.6.2-1
+ Revision: 684349
- update to new version 15.6.2

* Mon Jun 06 2011 Funda Wang <fwang@mandriva.org> 0:15.6.1-1
+ Revision: 682953
- fix build
- update to new version 15.6.1

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0:15.4.3-2
+ Revision: 640483
- rebuild to obsolete old packages

* Tue Feb 08 2011 Sandro Cazzaniga <kharec@mandriva.org> 0:15.4.3-1
+ Revision: 636785
- New release 15.4.3

* Sat Jan 29 2011 Sandro Cazzaniga <kharec@mandriva.org> 0:15.4.2-1
+ Revision: 633843
- New version

* Sun Jan 23 2011 Sandro Cazzaniga <kharec@mandriva.org> 0:15.4.1-1
+ Revision: 632428
- update to 15.4.1

* Thu Jan 20 2011 Sandro Cazzaniga <kharec@mandriva.org> 0:15.4.0-1
+ Revision: 631826
- new version 15.4.0

* Mon Dec 27 2010 Funda Wang <fwang@mandriva.org> 0:15.3.7-1mdv2011.0
+ Revision: 625366
- update to new version 15.3.7

* Sun Dec 19 2010 Funda Wang <fwang@mandriva.org> 0:15.3.6-1mdv2011.0
+ Revision: 623140
- update to new version 15.3.6

* Mon Nov 29 2010 Sandro Cazzaniga <kharec@mandriva.org> 0:15.3.5-1mdv2011.0
+ Revision: 602968
- update to 15.3.5

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 0:15.3.4-1mdv2011.0
+ Revision: 598572
- new version 15.3.4

* Sun Oct 24 2010 Sandro Cazzaniga <kharec@mandriva.org> 0:15.3.1-1mdv2011.0
+ Revision: 587903
- new version

* Tue Oct 12 2010 Sandro Cazzaniga <kharec@mandriva.org> 0:15.3.0-1mdv2011.0
+ Revision: 585071
- update to 15.3.0

* Wed Sep 29 2010 Funda Wang <fwang@mandriva.org> 0:15.2.2-1mdv2011.0
+ Revision: 581956
- update to new version 15.2.2

* Thu Sep 02 2010 Sandro Cazzaniga <kharec@mandriva.org> 0:15.2.1-1mdv2011.0
+ Revision: 575257
- update to 15.2.1

* Tue Aug 24 2010 Funda Wang <fwang@mandriva.org> 0:15.2.0-1mdv2011.0
+ Revision: 572566
- update to new version 15.2.0

* Mon Aug 09 2010 Funda Wang <fwang@mandriva.org> 0:15.1.6-1mdv2011.0
+ Revision: 568155
- update to new version 15.1.6

* Tue Jul 20 2010 Funda Wang <fwang@mandriva.org> 0:15.1.5-1mdv2011.0
+ Revision: 555496
- update to new version 15.1.5

* Sun Jul 11 2010 Sandro Cazzaniga <kharec@mandriva.org> 0:15.1.4-1mdv2011.0
+ Revision: 551163
- update to 15.1.4

* Thu Apr 22 2010 Sandro Cazzaniga <kharec@mandriva.org> 0:15.0.7-1mdv2010.1
+ Revision: 537809
- update to 15.0.7

* Sun Mar 28 2010 Sandro Cazzaniga <kharec@mandriva.org> 0:15.0.6-1mdv2010.1
+ Revision: 528507
- update to 15.0.6
- remove com

* Wed Jan 27 2010 Frederik Himpe <fhimpe@mandriva.org> 0:15.0.5-1mdv2010.1
+ Revision: 497376
- update to new version 15.0.5

* Mon Jan 18 2010 Frederik Himpe <fhimpe@mandriva.org> 0:15.0.4-1mdv2010.1
+ Revision: 493270
- update to new version 15.0.4

* Fri Jan 15 2010 Jérôme Brenier <incubusss@mandriva.org> 0:15.0.3-1mdv2010.1
+ Revision: 491851
- new version 15.0.3

* Sun Dec 27 2009 Frederik Himpe <fhimpe@mandriva.org> 0:15.0.2-1mdv2010.1
+ Revision: 482903
- update to new version 15.0.2

* Thu Dec 17 2009 Frederik Himpe <fhimpe@mandriva.org> 0:15.0.1-1mdv2010.1
+ Revision: 479812
- update to new version 15.0.1

* Sun Dec 06 2009 Funda Wang <fwang@mandriva.org> 0:15.0.0-1mdv2010.1
+ Revision: 474005
- new version 15.0.0

* Sat Nov 28 2009 Funda Wang <fwang@mandriva.org> 0:14.6.3-1mdv2010.1
+ Revision: 470837
- new version 14.6.3

* Sun Nov 08 2009 Frederik Himpe <fhimpe@mandriva.org> 0:14.6.0-1mdv2010.1
+ Revision: 462837
- update to new version 14.6.0

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 0:14.5.7-1mdv2010.1
+ Revision: 462144
- update to new version 14.5.7

* Wed Sep 16 2009 Frederik Himpe <fhimpe@mandriva.org> 0:14.5.5-1mdv2010.0
+ Revision: 443608
- update to new version 14.5.5

* Sun Aug 30 2009 Frederik Himpe <fhimpe@mandriva.org> 0:14.5.4-1mdv2010.0
+ Revision: 422658
- update to new version 14.5.4

* Sat Jul 18 2009 Frederik Himpe <fhimpe@mandriva.org> 0:14.5.2-1mdv2010.0
+ Revision: 397209
- update to new version 14.5.2

* Mon Jul 06 2009 Frederik Himpe <fhimpe@mandriva.org> 0:14.5.1-1mdv2010.0
+ Revision: 393058
- update to new version 14.5.1

* Thu Jun 25 2009 Frederik Himpe <fhimpe@mandriva.org> 0:14.5.0-1mdv2010.0
+ Revision: 389179
- update to new version 14.5.0

* Sun Jun 14 2009 Frederik Himpe <fhimpe@mandriva.org> 0:14.4.5-1mdv2010.0
+ Revision: 385892
- update to new version 14.4.5

* Wed Jun 03 2009 Frederik Himpe <fhimpe@mandriva.org> 0:14.4.4-1mdv2010.0
+ Revision: 382485
- update to new version 14.4.4

* Wed May 13 2009 Frederik Himpe <fhimpe@mandriva.org> 0:14.4.2-1mdv2010.0
+ Revision: 375513
- update to new version 14.4.2

* Mon May 04 2009 Frederik Himpe <fhimpe@mandriva.org> 0:14.4.1-1mdv2010.0
+ Revision: 371862
- update to new version 14.4.1

* Wed Mar 18 2009 Frederik Himpe <fhimpe@mandriva.org> 0:14.3.5-1mdv2009.1
+ Revision: 357426
- update to new version 14.3.5

* Thu Mar 05 2009 Frederik Himpe <fhimpe@mandriva.org> 0:14.3.4-1mdv2009.1
+ Revision: 349095
- update to new version 14.3.4

* Fri Feb 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0:14.3.3-2mdv2009.1
+ Revision: 345416
- rebuild against new readline

* Mon Feb 16 2009 Frederik Himpe <fhimpe@mandriva.org> 0:14.3.3-1mdv2009.1
+ Revision: 341046
- update to new version 14.3.3

* Mon Feb 09 2009 Frederik Himpe <fhimpe@mandriva.org> 0:14.3.2-1mdv2009.1
+ Revision: 338871
- update to new version 14.3.2

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 0:14.3.0-1mdv2009.1
+ Revision: 332766
- New upstream release

* Sun Jan 04 2009 Frederik Himpe <fhimpe@mandriva.org> 0:14.2.8-1mdv2009.1
+ Revision: 324532
- update to new version 14.2.8

* Sat Dec 20 2008 Frederik Himpe <fhimpe@mandriva.org> 0:14.2.7-1mdv2009.1
+ Revision: 316427
- update to new version 14.2.7

* Sun Dec 07 2008 Frederik Himpe <fhimpe@mandriva.org> 0:14.2.5-1mdv2009.1
+ Revision: 311515
- update to new version 14.2.5

* Mon Nov 24 2008 David Walluck <walluck@mandriva.org> 0:14.2.3-1mdv2009.1
+ Revision: 306127
- 14.2.3

* Tue Nov 11 2008 Frederik Himpe <fhimpe@mandriva.org> 0:14.2.2-1mdv2009.1
+ Revision: 302314
- update to new version 14.2.2

* Sat Oct 18 2008 Frederik Himpe <fhimpe@mandriva.org> 0:14.2.1-1mdv2009.1
+ Revision: 295039
- update to new version 14.2.1

* Fri Oct 10 2008 Frederik Himpe <fhimpe@mandriva.org> 0:14.2.0-1mdv2009.1
+ Revision: 291655
- update to new version 14.2.0

* Sun Sep 07 2008 Frederik Himpe <fhimpe@mandriva.org> 0:14.1.6-1mdv2009.0
+ Revision: 282324
- update to new version 14.1.6

* Mon Aug 25 2008 Frederik Himpe <fhimpe@mandriva.org> 0:14.1.5-1mdv2009.0
+ Revision: 275991
- update to new version 14.1.5

* Sat Aug 16 2008 Frederik Himpe <fhimpe@mandriva.org> 0:14.1.4-1mdv2009.0
+ Revision: 272765
- update to new version 14.1.4

* Wed Aug 13 2008 Frederik Himpe <fhimpe@mandriva.org> 0:14.1.3-1mdv2009.0
+ Revision: 271539
- update to new version 14.1.3

* Mon Aug 11 2008 Frederik Himpe <fhimpe@mandriva.org> 0:14.1.2-1mdv2009.0
+ Revision: 270846
- update to new version 14.1.2

* Thu Jul 31 2008 Frederik Himpe <fhimpe@mandriva.org> 0:14.1.1-1mdv2009.0
+ Revision: 257950
- update to new version 14.1.1

* Sun Jul 27 2008 David Walluck <walluck@mandriva.org> 0:14.1.0-1mdv2009.0
+ Revision: 250495
- 14.1.0

* Mon May 05 2008 Funda Wang <fwang@mandriva.org> 0:14.0.2-1mdv2009.0
+ Revision: 201442
- New version 14.0.2

* Fri Apr 25 2008 David Walluck <walluck@mandriva.org> 0:14.0.0-1mdv2009.0
+ Revision: 197337
- 14.0.0

* Sun Apr 20 2008 David Walluck <walluck@mandriva.org> 0:12.9.2-1mdv2009.0
+ Revision: 196003
- 12.9.2

* Mon Feb 25 2008 Frederik Himpe <fhimpe@mandriva.org> 0:12.8.8-1mdv2008.1
+ Revision: 174954
- New upstream version
- New license policy

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Fri Feb 01 2008 David Walluck <walluck@mandriva.org> 0:12.8.6-1mdv2008.1
+ Revision: 161274
- 12.8.6

* Wed Jan 23 2008 David Walluck <walluck@mandriva.org> 0:12.8.5-1mdv2008.1
+ Revision: 156969
- 12.8.5

* Tue Jan 08 2008 David Walluck <walluck@mandriva.org> 0:12.8.4-1mdv2008.1
+ Revision: 146900
- 12.8.4

* Sun Dec 30 2007 David Walluck <walluck@mandriva.org> 0:12.8.3-1mdv2008.1
+ Revision: 139387
- fix build
- 12.8.3

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 David Walluck <walluck@mandriva.org> 0:12.8.2-1mdv2008.1
+ Revision: 119061
- BuildRequires: desktop-file-utils
- 12.8.2

* Sat Nov 17 2007 David Walluck <walluck@mandriva.org> 0:12.8.0-1mdv2008.1
+ Revision: 109187
- 12.8.0

* Fri Nov 02 2007 David Walluck <walluck@mandriva.org> 0:12.7.9-1mdv2008.1
+ Revision: 105305
- 12.7.9

* Sat Oct 13 2007 David Walluck <walluck@mandriva.org> 0:12.7.7-1mdv2008.1
+ Revision: 97840
- 12.7.7

* Fri Sep 07 2007 David Walluck <walluck@mandriva.org> 0:12.7.6-1mdv2008.0
+ Revision: 81513
- 12.7.6

* Mon Aug 20 2007 David Walluck <walluck@mandriva.org> 0:12.7.5-1mdv2008.0
+ Revision: 68037
- 12.7.5

* Sat Jun 23 2007 David Walluck <walluck@mandriva.org> 0:12.7.3-1mdv2008.0
+ Revision: 43423
- 12.7.3

* Mon May 14 2007 David Walluck <walluck@mandriva.org> 0:12.7.0-1mdv2008.0
+ Revision: 26604
- 12.7.0


* Fri Dec 15 2006 David Walluck <walluck@mandriva.org> 12.6.8-1mdv2007.0
+ Revision: 97387
- 12.6.8
- Import mathomatic

* Mon Sep 18 2006 David Walluck <walluck@mandriva.org> 0:12.6.3-1
- 12.6.3

* Mon Aug 28 2006 David Walluck <walluck@mandriva.org> 0:12.6.1-1mdv2007.0
- 12.6.1

* Sat Aug 12 2006 David Walluck <walluck@mandriva.org> 0:12.5.19-1mdv2007.0
- 12.5.19

* Tue Aug 08 2006 David Walluck <walluck@mandriva.org> 0:12.5.18-1mdv2007.0
- 12.5.18

* Tue Jul 11 2006 David Walluck <walluck@mandriva.org> 0:12.5.17-1mdv2007.0
- 12.5.17

* Mon Jun 05 2006 David Walluck <walluck@mandriva.org> 0:12.5.16-1mdv2007.0
- 12.5.16

* Tue Mar 28 2006 David Walluck <walluck@mandriva.org> 0:12.5.12-1mdk
- 12.5.12

* Thu Mar 09 2006 Lenny Cartier <lenny@mandriva.com> 0:12.5.11-1mdk
- 12.5.11

* Thu Mar 02 2006 David Walluck <walluck@mandriva.org> 0:12.5.10-1mdk
- 12.5.10

* Wed Feb 22 2006 David Walluck <walluck@mandriva.org> 0:12.5.8-1mdk
- 12.5.8

* Fri Jan 20 2006 David Walluck <walluck@mandriva.org> 0:12.5.6-1mdk
- 12.5.6

* Thu Dec 29 2005 David Walluck <walluck@mandriva.org> 0:12.5.5-1mdk
- 12.5.5

* Sat Dec 17 2005 David Walluck <walluck@mandriva.org> 0:12.5.4-1mdk
- 12.5.4

* Sun Oct 23 2005 David Walluck <walluck@mandriva.org> 0:12.5.0-1mdk
- 12.5.0

* Mon Oct 10 2005 David Walluck <walluck@mandriva.org> 0:12.4.12-1mdk
- release

