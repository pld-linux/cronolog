Summary:	A flexible log file rotation program for Apache
Summary(pl.UTF-8):   Program do elastycznej rotacji logów serwera Apache
Name:		cronolog
Version:	1.6.2
Release:	4
License:	Apache license
Group:		Networking/Daemons
Source0:	http://www.cronolog.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	a44564fd5a5b061a5691b9a837d04979
Patch0:		http://cronolog.org/patches/%{name}-jumbo-patch.txt
URL:		http://www.cronolog.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"cronolog" is a simple program that reads log messages from its input
and writes them to a set of output files, the names of which are
constructed using template and the current date and time. The template
uses the same format specifiers as the Unix date command (which are
the same as the standard C strftime library function).

%description -l pl.UTF-8
"cronolog" jest prostym programem czytającym logi i zapisującym je do
plików wyjściowych, których nazwy można tworzyć używając szablonu oraz
bieżącego czasu i daty. Szablony korzystają z tego samego formatu co
polecenie date systemu Unix (który jest taki sam jak dla standardowej
funkcji C strftime). Dzięki użyciu mechanizmu "piped logs", program
ten może być stosowany do rotacji logów, która nie wymaga
restartowania serwera Apache.

%prep
%setup -q
%patch0 -p1

%build
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS TODO
%attr(755,root,root) %{_sbindir}/cronolog
%attr(755,root,root) %{_sbindir}/cronosplit
%{_mandir}/man1/*.1*
%{_infodir}/*.info*
