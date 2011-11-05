# revision 24147
# category Package
# catalog-ctan /macros/xetex/latex/xgreek
# catalog-date 2011-09-27 17:21:55 +0200
# catalog-license lppl
# catalog-version 2.3
Name:		texlive-xgreek
Version:	2.3
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/xgreek/xgreek.sty
%doc %{_texmfdistdir}/doc/xelatex/xgreek/README
%doc %{_texmfdistdir}/doc/xelatex/xgreek/xgreek.pdf
#- source
%doc %{_texmfdistdir}/source/xelatex/xgreek/xgreek.dtx
%doc %{_texmfdistdir}/source/xelatex/xgreek/xgreek.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
