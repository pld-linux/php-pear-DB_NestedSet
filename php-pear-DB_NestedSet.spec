# ToDo:
# - pl description
%include	/usr/lib/rpm/macros.php
%define         _class          DB
%define         _subclass       NestedSet
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - API to build and query nested sets
Summary(pl):	%{_pearname} - API to tworzenia i wykonywania zagnie�dzonych zapyta�
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	718e2084f0abfb48898d595cf016c5ca
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB_NestedSet let's you create trees with infinite depth inside a
relational database. The package provides a way to o
create/update/delete nodes o query nodes, trees and subtrees o copy
(clone) nodes, trees and subtrees o move nodes, trees and subtrees o
call event handlers on specific events like on node deletion o output
the tree with
- PEAR::HTML_TreeMenu
- TigraMenu (http://www.softcomplex.com/products/tigra_menu/) o It
  also features caching of SQL queries using PEAR::Cache

This class has in PEAR status: %{_status}.

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
