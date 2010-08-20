%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	NestedSet
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - API to build and query nested sets
Summary(pl.UTF-8):	%{_pearname} - API to tworzenia i wykonywania zagnieżdżonych zapytań
Name:		php-pear-%{_pearname}
Version:	1.4.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b906275511a6f4d1e9b1ed95ac6d7546
Patch0:		includepath.patch
URL:		http://pear.php.net/package/DB_NestedSet/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-12
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# included in tests
%define		_noautoreq 'pear(TestBase.php)' 'pear(UnitTest.php)'

%description
DB_NestedSet lets you create trees with infinite depth inside a
relational database. The package provides a way to:
- create/update/delete nodes
- query nodes, trees and subtrees
- copy (clone) nodes, trees and subtrees
- move nodes, trees and subtrees
- call event handlers on specific events like on node deletion
- output the tree with
  - PEAR::HTML_TreeMenu
  - TigraMenu (http://www.softcomplex.com/products/tigra_menu/)
- It also features caching of SQL queries using PEAR::Cache.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
DB_NestedSet pozwala na tworzenie drzew nieskończonej długości
wewnątrz relacyjnych baz danych. Pakiet umożliwia:
- tworzenie/modyfikowanie/usuwanie węzłów
- odpytywanie węzłów, drzew i poddrzew
- kopiowanie (klonowanie) węzłów, drzew i poddrzew
- przenoszenie węzłów, drzew i poddrzew
- wywoływanie procedur obsługi dla określonych zdarzeń typu usuwanie
  węzła
- pokazanie drzewa przy użyciu:
  - PEAR::HTML_TreeMenu
  - TigraMenu (http://www.softcomplex.com/products/tigra_menu/)
- może także buforować zapytania SQL przy użyciu PEAR::Cache.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
%patch0 -p1

install -d examples
mv docs/%{_pearname}/docs/*example.php examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php

%{_examplesdir}/%{name}-%{version}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
