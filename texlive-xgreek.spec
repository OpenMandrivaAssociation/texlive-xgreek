%global tl_name xgreek
%global tl_revision 79601

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.5.1
Release:	%{tl_revision}.1
Summary:	Greek Language Support for XeLaTeX and LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/xgreek
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xgreek.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xgreek.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xgreek.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package has been designed so to allow people to typeset Greek
language documents using XeLaTeX or LuaLaTeX. It is released in the hope
that people will use it and spot errors, bugs, features so to improve
it. Practically, it provides all the capabilities of the greek option of
the babel package. The package can be invoked with any of the following
options: monotonic (for typesetting modern monotonic Greek), polytonic
(for typesetting modern polytonic Greek), and ancient (for typesetting
ancient texts). The default option is monotonic. The command
\setlanguage{<lang>} activates the hyphenation patterns of the language
<lang>. This, however, can only be done if the format file has not been
built with the babel mechanism.

