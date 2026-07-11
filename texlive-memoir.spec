%global tl_name memoir
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.8.4b
Release:	%{tl_revision}.1
Summary:	Typeset fiction, non-fiction and mathematical books
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/memoir
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/memoir.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/memoir.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/memoir.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The memoir class is for typesetting poetry, fiction, non-fiction, and
mathematical works. Permissible document 'base' font sizes range from 9
to 60pt. There is a range of page-styles and well over a dozen chapter-
styles to choose from, as well as methods for specifying your own
layouts and designs. The class also provides the functionality of over
thirty of the more popular packages, thus simplifying document sources.
Users who wish to use the hyperref package, in a document written with
the memoir class, should also use the memhfixc package (part of this
bundle). Note, however, that any current version of hyperref actually
loads the package automatically if it detects that it is running under
memoir.

