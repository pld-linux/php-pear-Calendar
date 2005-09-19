%include	/usr/lib/rpm/macros.php
%define		_class		Calendar
%define		_status		beta
%define		_pearname	%{_class}

Summary:	%{_pearname} - building calendar data structures (irrespective of output)
Summary(pl):	%{_pearname} - tworzenie struktur danych kalendarza (niezale¿ne od wyj¶cia)
Name:		php-pear-%{_pearname}
Version:	0.5.2
Release:	2.1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	26e2dedc175fd5056856b1fee6c0415a
URL:		http://pear.php.net/package/Calendar/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Date/Calc.php)'

%description
Calendar provides an API for building calendar data structures. Using
the simple iterator and it's "query" API, a user interface can easily be
built on top of the calendar data structure, at the same time easily
connecting it to some kind of underlying data store, where "event"
information is being held.

It provides different calculation "engines" the default being based on
Unix timestamps (offering fastest performance) with an alternative using
PEAR::Date which extends the calendar past the limitations of Unix
timestamps. Other engines should be implementable for other types of
calendar (e.g. a Chinese Calendar based on lunar cycles).

In PEAR status of this package is: %{_status}.

%description -l pl
Calendar dostarcza API do tworzenia struktur danych kalendarza. Przy
u¿yciu prostego iteratora i jego API zapytañ mo¿na ³atwo zbudowaæ
interfejs u¿ytkownika w oparciu o strukturê danych kalendarza, a
jednocze¶nie po³±czyæ j± z jakim¶ rodzajem przechowywania danych,
gdzie trzymane s± informacje o zdarzeniach.

Klasa udostêpnia ró¿ne "silniki" obliczeñ; domy¶lny jest oparty na
uniksowych timestampach (i jest najszybszy), alternatywny u¿ywa klasy
PEAR::Date rozszerzaj±cej kalendarz poza ograniczenia timestampów.
Powinno siê daæ zaimplementowaæ inne silniki dla innych rodzajów
kalendarzy (np. kalendarza chiñskiego opartego na fazach ksiê¿yca).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
