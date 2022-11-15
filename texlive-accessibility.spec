Name:		texlive-accessibility
Version:	55777
Release:	1
Summary:	Create tagged and structured PDF files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/accessibility
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/accessibility.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/accessibility.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/accessibility.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The accessibility package is intended to create tagged,
structured PDF documents from LaTeX source code. It allows to
produce tagged PDF output following Adobe's PDF-1.5 and 1.6
specifications. This package is predominantly targeted at
documents produced using the KOMA-Script document classes.
However, the author told us towards the end of June 2020:
"Based on feedback to the 'accessibility' package and
discussions with a few folks, I'd like to discourage people
from using the package any more. It's evident that it's not
going to work in it's current form, and I don't have the skills
or time to update it. I know the general concept is very
important, and so I'm looking at getting support from various
funding agencies to employ someone to completely refactor the
code in a more future-proof fashion. I'll coordinate this with
the core LaTeX Team once I have more solid ideas."

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/accessibility
%{_texmfdistdir}/tex/latex/accessibility
%doc %{_texmfdistdir}/doc/latex/accessibility

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
