Summary:        A flexible log file rotation program for Apache
Summary(pl):	Program do elastycznej rotacji log�w serwera Apache
Name:           cronolog
Version:	1.6.2
Release:	1
License:	Apache license
Group:		Networking/Daemons
Source0:	http://www.ford-mason.co.uk/resources/cronolog/cronolog-%version.tar.gz
URL:		http://www.ford-mason.co.uk/resources/cronolog/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"cronolog" is a simple program that reads log messages from its input
and writes them to a set of output files, the names of which are
constructed using template and the current date and time. The template
uses the same format specifiers as the Unix date command (which are
the same as the standard C strftime library function).

%description -l pl
"cronolog" jest prostym programem czytaj�cym logi i zapisuj�cym
je do plik�w wyj�ciowych, kt�rych nazwy mo�na tworzy� u�ywaj�c
szablonu oraz bie��cego czasu i daty. Szablony korzystaj� z tego
samego formatu co polecenie date systemu Unix (kt�ry jest taki
sam jak dla standardowej funkcji C strftime).
Dzi�ki u�yciu mechanizmu "piped logs", program ten mo�e by� stosowany
do rotacji log�w, kt�ra nie wymaga restartowania serwera Apache.

%prep
%setup -q -n %{name}-%{version}

%build
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/cronolog
%attr(755,root,root) %{_sbindir}/cronosplit
%attr(644,root,root) %{_mandir}/man1/*.1*
