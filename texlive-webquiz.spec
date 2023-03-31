Name:		texlive-webquiz
Version:	58808
Release:	2
Summary:	Write interactive web based quizzes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/webquiz
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/webquiz.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/webquiz.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
WebQuiz makes it possible to use LaTeX to write interactive web
based quizzes. The quizzes are first written in LaTeX and then
converted into HTML files using WebQuiz, which is written in
Python3. The conversion from LaTeX to HTML is done behind the
scenes using TeX4ht.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/tex/latex/webquiz
%{_texmfdistdir}/texmf-dist/scripts/webquiz
%doc %{_texmfdistdir}/texmf-dist/doc/latex/webquiz
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/webquiz.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/webquiz.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
