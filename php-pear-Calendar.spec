%define		_class		Calendar
%define		_status		beta
%define		_pearname	Calendar
Summary:	%{_pearname} - building calendar data structures (irrespective of output)
Summary(pl.UTF-8):	%{_pearname} - tworzenie struktur danych kalendarza (niezależne od wyjścia)
Name:		php-pear-%{_pearname}
Version:	0.5.5
Release:	4
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	05d7ceec2efe834857f01963162a2399
URL:		http://pear.php.net/package/Calendar/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.0.5
Requires:	php-pear
Suggests:	php-pear-Date
Obsoletes:	php-pear-Calendar-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(Date/Calc.php)

%description
Calendar provides an API for building calendar data structures. Using
the simple iterator and it's "query" API, a user interface can easily
be built on top of the calendar data structure, at the same time
easily connecting it to some kind of underlying data store, where
"event" information is being held.

It provides different calculation "engines" the default being based on
Unix timestamps (offering fastest performance) with an alternative
using PEAR::Date which extends the calendar past the limitations of
Unix timestamps. Other engines should be implementable for other types
of calendar (e.g. a Chinese Calendar based on lunar cycles).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Calendar dostarcza API do tworzenia struktur danych kalendarza. Przy
użyciu prostego iteratora i jego API zapytań można łatwo zbudować
interfejs użytkownika w oparciu o strukturę danych kalendarza, a
jednocześnie połączyć ją z jakimś rodzajem przechowywania danych,
gdzie trzymane są informacje o zdarzeniach.

Klasa udostępnia różne "silniki" obliczeń; domyślny jest oparty na
uniksowych timestampach (i jest najszybszy), alternatywny używa klasy
PEAR::Date rozszerzającej kalendarz poza ograniczenia timestampów.
Powinno się dać zaimplementować inne silniki dla innych rodzajów
kalendarzy (np. kalendarza chińskiego opartego na fazach księżyca).

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/Calendar
