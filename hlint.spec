# https://fedoraproject.org/wiki/Packaging:Haskell

%global ghc_without_dynamic 1
%global ghc_without_shared 1
%global without_prof 1
%global without_haddock 1

%global pkg_name hlint
%global pkgver %{pkg_name}-%{version}

# nothing to see here
%global debug_package %{nil}

Name:           %{pkg_name}
Version:        2.1.6
Release:        1%{?dist}
Summary:        Haskell source code suggestions

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
#BuildRequires:  chrpath
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cmdargs-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cpphs-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-haskell-src-exts-devel
%if 0%{?fedora} >= 27
BuildRequires:  ghc-haskell-src-exts-util-devel
%endif
BuildRequires:  ghc-hscolour-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-refact-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-uniplate-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-yaml-devel
# End cabal-rpm deps
BuildRequires:  cabal-install > 1.18
# for h-s-e
BuildRequires:  happy

%description
HLint gives suggestions on how to improve your source code.


%prep
%setup -q


%build
[ -d "$HOME/.cabal" ] || cabal update
%global cabal cabal
%cabal sandbox init
%cabal install --only-dependencies
%ghc_bin_build


%install
%ghc_bin_install

mkdir -p %{buildroot}%{_mandir}/man1
cp -p data/hlint.1 %{buildroot}%{_mandir}/man1

find %{buildroot}%{_libdir} -name "libHS%{pkg_name}-%{version}-*.so" -delete
rm -r %{buildroot}%{ghclibdir}


%files
%license LICENSE
%license .cabal-sandbox/share/doc/*/*
%doc CHANGES.txt README.md
%{_bindir}/%{name}
%{_datadir}/%{name}-%{version}
%{_mandir}/man1/%{name}*


%changelog
* Mon Jun 25 2018 Jens Petersen <petersen@redhat.com> - 2.1.6-1
- update to 2.1.6
- build better with macros to fix datadir path

* Fri Apr 20 2018 Jens Petersen <petersen@redhat.com> - 2.1.3-1
- 2.1.3
- --force-reinstalls needed for F26 and F27

* Wed Feb 21 2018 Jens Petersen <petersen@redhat.com> - 2.1-1
- update to 2.1

* Tue Dec  5 2017 Jens Petersen <petersen@redhat.com> - 2.0.11-1
- update to 2.0.11

* Wed Jun 28 2017 Jens Petersen <petersen@redhat.com> - 2.0.9-1
- update to 2.0.9

* Sun Jun 11 2017 Jens Petersen <petersen@redhat.com> - 2.0.8-1
- initial copr package
