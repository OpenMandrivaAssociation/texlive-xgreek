Name:		texlive-xgreek
Version:	69268
Release:	1
Summary:	XeLaTeX package for typesetting Greek language documents (beta release)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/xgreek
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xgreek.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xgreek.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xgreek.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package has been designed so to allow people to typeset
Greek language documents using XeLaTeX. And it is released in
the hope that people will use it and spot errors, bugs,
features so to improve it. Practically, it provides all the
capabilities of the greek option of the babel package. The
package can be invoked with any of the following options:
monotonic (for typesetting modern monotonic Greek), polytonic
(for typesetting modern polytonic Greek), and ancient (for
typesetting ancient texts). The default option is monotonic.
The command \setlanguage{<lang>} to activate the hyphenation
patterns of the language <lang> This, however, can be done only
if the format file has not been built with the babel mechanism.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xgreek
%doc %{_texmfdistdir}/doc/latex/xgreek
#- source
%doc %{_texmfdistdir}/source/latex/xgreek

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
