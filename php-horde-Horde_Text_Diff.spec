%define		status		stable
%define		pearname	Horde_Text_Diff
Summary:	%{pearname} - Engine for performing and rendering text diffs
Name:		php-horde-Horde_Text_Diff
Version:	1.0.2
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	3b4c1891e0501b77605d89948bc909bc
URL:		https://github.com/horde/horde/tree/master/framework/Text_Diff/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php(xdiff)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(xdiff.*)

%description
This package provides a text-based diff engine and renderers for
multiple diff output formats.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%doc docs/Horde_Text_Diff/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Text/Diff.php
%{php_pear_dir}/Horde/Text/Diff
