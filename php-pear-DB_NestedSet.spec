%include	/usr/lib/rpm/macros.php
%define         _class          DB
%define         _subclass       NestedSet
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - API to build and query nested sets
Summary(pl):	%{_pearname} - API to tworzenia i wykonywania zagnie¿dzonych zapytañ
Name:		php-pear-%{_pearname}
Version:	1.2.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e674dc272482436e075dfb119a22680d
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

This class has in PEAR status: %{_status}.

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

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
