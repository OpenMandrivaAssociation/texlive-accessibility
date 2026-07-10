%global tl_name accessibility
%global tl_revision 55777

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.3
Release:	%{tl_revision}.1
Summary:	Create tagged and structured PDF files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/accessibility
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/accessibility.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/accessibility.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/accessibility.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The accessibility package is intended to create tagged, structured PDF
documents from LaTeX source code. It allows to produce tagged PDF output
following Adobe's PDF-1.5 and 1.6 specifications. This package is
predominantly targeted at documents produced using the KOMA-Script
document classes. However, the author told us towards the end of June
2020: "Based on feedback to the 'accessibility' package and discussions
with a few folks, I'd like to discourage people from using the package
any more. It's evident that it's not going to work in it's current form,
and I don't have the skills or time to update it. I know the general
concept is very important, and so I'm looking at getting support from
various funding agencies to employ someone to completely refactor the
code in a more future-proof fashion. I'll coordinate this with the core
LaTeX Team once I have more solid ideas."

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/accessibility
%dir %{_datadir}/texmf-dist/source/latex/accessibility
%dir %{_datadir}/texmf-dist/tex/latex/accessibility
%doc %{_datadir}/texmf-dist/doc/latex/accessibility/CHANGELOG.md
%doc %{_datadir}/texmf-dist/doc/latex/accessibility/README.md
%doc %{_datadir}/texmf-dist/doc/latex/accessibility/accessibility-Anleitung-DE.pdf
%doc %{_datadir}/texmf-dist/doc/latex/accessibility/accessibility.pdf
%doc %{_datadir}/texmf-dist/source/latex/accessibility/accessibility.dtx
%doc %{_datadir}/texmf-dist/source/latex/accessibility/accessibility.ins
%{_datadir}/texmf-dist/tex/latex/accessibility/accessibility.sty
