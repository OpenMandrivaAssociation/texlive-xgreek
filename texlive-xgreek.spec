# revision 31170
# category Package
# catalog-ctan /macros/xetex/latex/xgreek
# catalog-date 2012-07-21 23:51:26 +0200
# catalog-license lppl
# catalog-version 2.4
Name:		texlive-xgreek
Version:	2.4
Release:	3
Summary:	XeLaTeX package for typesetting Greek language documents (beta release)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/xgreek
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xgreek.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xgreek.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xgreek.source.tar.xz
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
%{_texmfdistdir}/tex/xelatex/xgreek/xgreek.sty
%doc %{_texmfdistdir}/doc/xelatex/xgreek/README
%doc %{_texmfdistdir}/doc/xelatex/xgreek/xgreek.pdf
#- source
%doc %{_texmfdistdir}/source/xelatex/xgreek/xgreek.dtx
%doc %{_texmfdistdir}/source/xelatex/xgreek/xgreek.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
