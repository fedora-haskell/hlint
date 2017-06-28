# nothing to see here
%global debug_package %{nil}

%global pkg_name hlint
%global pkgver %{pkg_name}-%{version}

Name:           hlint
Version:        2.0.9
Release:        1%{?dist}
Summary:        Haskell source code suggestions

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
#BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cmdargs-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cpphs-devel
BuildRequires:  ghc-directory-devel
#BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-haskell-src-exts-devel
BuildRequires:  ghc-hscolour-devel
BuildRequires:  ghc-process-devel
#BuildRequires:  ghc-refact-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-uniplate-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-yaml-devel
# End cabal-rpm deps
BuildRequires:  cabal-install > 1.18
%if 0%{?fedora} < 26
# for h-s-e
BuildRequires:  happy
%endif


%description
HLint gives suggestions on how to improve your source code.


%prep
%setup -q


%build
%global cabal cabal
[ -d "$HOME/.cabal" ] || %cabal update
%cabal sandbox init
%cabal install


%install
mkdir -p %{buildroot}%{_bindir}
install -p .cabal-sandbox/bin/%{name} %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man1
cp -p .cabal-sandbox/share/*/%{pkgver}/hlint.1 %{buildroot}%{_mandir}/man1

cp -pr .cabal-sandbox/share/*/%{pkgver} %{buildroot}%{_datadir}


%files
%license .cabal-sandbox/share/doc/*/*
%doc CHANGES.txt README.md
%{_bindir}/%{name}
%{_datadir}/%{name}-%{version}
%{_mandir}/man1/%{name}*


%changelog
* Wed Jun 28 2017 Jens Petersen <petersen@redhat.com> - 2.0.9-1
- update to 2.0.9

* Sun Jun 11 2017 Jens Petersen <petersen@redhat.com> - 2.0.8-1
- initial copr package
