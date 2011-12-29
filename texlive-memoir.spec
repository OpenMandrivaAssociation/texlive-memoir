# revision 21638
# category Package
# catalog-ctan /macros/latex/contrib/memoir
# catalog-date 2011-03-06 22:53:00 +0100
# catalog-license lppl
# catalog-version 3.6j patch 6.0g
Name:		texlive-memoir
Version:	3.6j.6.0g
Release:	1
Summary:	Typeset fiction, non-fiction and mathematical books
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/memoir
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memoir.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memoir.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memoir.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The memoir class is for typesetting poetry, fiction, non-
fiction, and mathematical works. Permissible document 'base'
font sizes range from 9 to 60pt. There is a range of page-
styles and well over a dozen chapter-styles to choose from, as
well as methods for specifying your own layouts and designs.
The class also provides the functionality of over thirty of the
more popular packages, thus simplifying document sources. The
class automatically loads an associated patch file mempatch;
the patch file may be updated from time to time, between
releases of the class itself. (The patch file stays around even
when there are no extant patches.) Users who wish to use the
hyperref package, in a document written with the memoir class,
should also use the memhfixc package (part of this bundle).
Note, however, that current versions of hyperref actually load
the package automatically if they detect that they are running
under memoir.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/memoir/basic.gst
%{_texmfdistdir}/tex/latex/memoir/mem10.clo
%{_texmfdistdir}/tex/latex/memoir/mem11.clo
%{_texmfdistdir}/tex/latex/memoir/mem12.clo
%{_texmfdistdir}/tex/latex/memoir/mem14.clo
%{_texmfdistdir}/tex/latex/memoir/mem17.clo
%{_texmfdistdir}/tex/latex/memoir/mem20.clo
%{_texmfdistdir}/tex/latex/memoir/mem25.clo
%{_texmfdistdir}/tex/latex/memoir/mem30.clo
%{_texmfdistdir}/tex/latex/memoir/mem36.clo
%{_texmfdistdir}/tex/latex/memoir/mem48.clo
%{_texmfdistdir}/tex/latex/memoir/mem60.clo
%{_texmfdistdir}/tex/latex/memoir/mem9.clo
%{_texmfdistdir}/tex/latex/memoir/memhfixc.sty
%{_texmfdistdir}/tex/latex/memoir/memoir.cls
%{_texmfdistdir}/tex/latex/memoir/mempatch.sty
%doc %{_texmfdistdir}/doc/latex/memoir/Makeidxglo
%doc %{_texmfdistdir}/doc/latex/memoir/README
%doc %{_texmfdistdir}/doc/latex/memoir/anvil2.mps
%doc %{_texmfdistdir}/doc/latex/memoir/memfonts.sty
%doc %{_texmfdistdir}/doc/latex/memoir/memlays.sty
%doc %{_texmfdistdir}/doc/latex/memoir/memman.gst
%doc %{_texmfdistdir}/doc/latex/memoir/memman.ist
%doc %{_texmfdistdir}/doc/latex/memoir/memman.pdf
%doc %{_texmfdistdir}/doc/latex/memoir/memman.tex
%doc %{_texmfdistdir}/doc/latex/memoir/memnoidxnum.tex
%doc %{_texmfdistdir}/doc/latex/memoir/memsty.sty
%doc %{_texmfdistdir}/doc/latex/memoir/titlepages.sty
%doc %{_texmfdistdir}/doc/latex/memoir/trims-example.tex
#- source
%doc %{_texmfdistdir}/source/latex/memoir/memoir.dtx
%doc %{_texmfdistdir}/source/latex/memoir/memoir.ins
%doc %{_texmfdistdir}/source/latex/memoir/mempatch.dtx
%doc %{_texmfdistdir}/source/latex/memoir/mempatch.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
