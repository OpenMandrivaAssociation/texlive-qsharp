%global tl_name qsharp
%global tl_revision 49722

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3.1901.1401
Release:	%{tl_revision}.1
Summary:	Syntax highlighting for the Q# language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/qsharp
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/qsharp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/qsharp.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/qsharp.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides syntax highlighting for the Q# language, a domain-
specific language for quantum programming.

