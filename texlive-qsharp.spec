Name:		texlive-qsharp
Version:	49722
Release:	1
Summary:	Syntax highlighting for the Q# language
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/qsharp
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qsharp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qsharp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qsharp.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides syntax highlighting for the Q# language, a
domain-specific language for quantum programming.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/qsharp
%{_texmfdistdir}/tex/latex/qsharp
%doc %{_texmfdistdir}/doc/latex/qsharp

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
