Name:		texlive-memoir
Version:	69600
Release:	1
Summary:	Typeset fiction, non-fiction and mathematical books
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/memoir
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memoir.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memoir.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memoir.source.r%{version}.tar.xz
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
%{_texmfdistdir}/makeindex/memoir
%{_texmfdistdir}/tex/latex/memoir
%doc %{_texmfdistdir}/doc/latex/memoir
#- source
%doc %{_texmfdistdir}/source/latex/memoir

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
