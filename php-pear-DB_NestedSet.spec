%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	NestedSet
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - API to build and query nested sets
Summary(pl):	%{_pearname} - API to tworzenia i wykonywania zagnie¿d¿onych zapytañ
Name:		php-pear-%{_pearname}
Version:	1.3.6
Release:	2.2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	556e7afbf740c0f18b35bfd820fd75b9
URL:		http://pear.php.net/package/DB_NestedSet/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	sed >= 4.0
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

%description -l pl
DB_NestedSet pozwala na tworzenie drzew nieskoñczonej d³ugo¶ci
wewn±trz relacyjnych baz danych. Pakiet umo¿liwia:
- tworzenie/modyfikowanie/usuwanie wêz³ów
- odpytywanie wêz³ów, drzew i poddrzew
- kopiowanie (klonowanie) wêz³ów, drzew i poddrzew
- przenoszenie wêz³ów, drzew i poddrzew
- wywo³ywanie procedur obs³ugi dla okre¶lonych zdarzeñ typu usuwanie
  wêz³a
- pokazanie drzewa przy u¿yciu:
  - PEAR::HTML_TreeMenu
  - TigraMenu (http://www.softcomplex.com/products/tigra_menu/)
- mo¿e tak¿e buforowaæ zapytania SQL przy u¿yciu PEAR::Cache.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

# fix tests
cd ./%{php_pear_dir}/tests/%{_pearname}/tests
# mac line endings!
sed -i -e 's,\r,\n,g' index.php

# make it suitable after install
sed -i -e 's,NestedSet.php,DB/NestedSet.php,' *.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

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

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
