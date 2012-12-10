%define		_state		stable
%define		orgname		kdewebdev
%define		qtver		4.8.0

Summary:	Web development tools for KDE
Summary(es.UTF-8):	Uno editor WEB para KDE
Summary(pl.UTF-8):	Narzędzia do tworzenia WWW dla KDE
Summary(pt_BR.UTF-8):	Um editor web para o KDE
Name:		kde4-kdewebdev
Version:	4.9.4
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	6104359726040087a5a87721476ad235
URL:		http://www.kde.org/
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	libgcrypt-devel
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	libxslt-devel >= 1.0.18
BuildRequires:	phonon-devel >= 4.4.1
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	ruby-devel
BuildRequires:	tidy-devel
BuildRequires:	zlib-devel
BuildConflicts:	quanta
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quanta Plus is a web development tool for the K Desktop Environment.
Quanta is designed for quick web development and is rapidly becoming a
mature editor with a number of great features.

%description -l es.UTF-8
Quanta Plus és una herramienta de desarrollo web para KDE. Es
projetado para rapido desarrollo web e es casi pronto com excelent
quantidad de caracteristicas.

%description -l pl.UTF-8
Quanta Plus to narzędzie do tworzenia WWW dla środowiska KDE. Służy do
szybkiego tworzenia stron i staje się dojrzałym edytorem z wieloma
przydatnymi możliwościami.

%description -l pt_BR.UTF-8
O Quanta Plus é uma ferramenta para desenvolvimento web para o KDE. É
projetado para desenvolvimento web rápido e está rapidamente se
tornando um editor maduro com um bom número de excelentes
características.

%package kfilereplace
Summary:	A powerful string replacer
Summary(pl.UTF-8):	Rozbudowane narzędzie do zamiany tekstu
Group:		X11/Development/Tools
Requires:	kde4-kdebase >= %{version}
Conflicts:	quanta < 1:3.2.90

%description kfilereplace
KFileReplace is a KDE utility which replace some strings with others
in a lot of files in an only operation.

%description kfilereplace -l pl.UTF-8
KFileReplace to narzędzie do masowej zmiany różnych tekstów w dużej
ilości plików, podczas jednej operacji.

%package kimagemapeditor
Summary:	An HTML image map editor
Summary(pl.UTF-8):	Edytor map obrazów w HTML
Group:		X11/Development/Tools
Requires:	kde4-kdebase >= %{version}

%description kimagemapeditor
An HTML image map editor.

%description kimagemapeditor -l pl.UTF-8
Edytor map obrazów w HTML.

%package klinkstatus
Summary:	Link checker for KDE
Summary(pl.UTF-8):	Program do sprawdzania odnośników pod KDE
Group:		X11/Development/Tools
Requires:	kde4-kdebase >= %{version}

%description klinkstatus
KLinkStatus is an Open Source tool for checking links in a web page.
It can search by depth, domain or both. On a domain search it's also
possible to choose the search depth of URLs with foreign domain. For
performance, it supports several simultaneous connections and try to
use the same connection for the same sequence of requests.

%description klinkstatus -l pl.UTF-8
KLinkStatus jest narzędziem do sprawdzania odnośników na stronie.
Obsługuje wyszukiwanie według głębokości, domeny lub obu naraz. W
wyszukiwaniu według domeny można również dodać maksymalną głębokość
dla pozostałych domen. Dla uzyskania jak najlepszej wydajności program
obsługuje symultaniczne połączenia oraz próbuje wykorzystać jedno
połączenie dla wszystkich sekwencji żądań.

%package klinkstatus-devel
Summary:	Development files for klinkstatus library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki klinkstatus
Group:		X11/Development/Tools
Requires:	kde4-kdewebdev-klinkstatus = %{version}-%{release}

%description klinkstatus-devel
Development files for klinkstatus library.

%description klinkstatus-devel -l pl.UTF-8
Pliki programistyczne biblioteki klinkstatus.

%package kommander
Summary:	A langauage independent visual dialog building tool
Summary(pl.UTF-8):	Niezależne od języka narzędzie do budowy okien dialogowych
Group:		X11/Development/Tools
Requires:	%{name}-kommander-executor = %{version}-%{release}
Requires:	kde4-kdebase >= %{version}
Conflicts:	quanta < 1:3.2.3

%description kommander
Kommander is a visual dialog building tool which may be expanded to
create full mainwindow applications. The primary objective is to
create as much functionality as possible without using any scripting
language. This is provided by the following features:
- Specials - these are prefaced with an "@" like @widgetText. They
  offer special features like the value of a widget, functions, aliases,
  global variables and such.
- DCOP integration - this allows Kommander dialogs to control and be
  controlled in interactions with other KDE applications.
- Signals and Slots - this is a little less intuitive to a new user.
  It is under review for how we process things in the first major
  release. These offer a limited event model for when a button is pushed
  or a widget is changed. Combined with "Population Text" it is rather
  powerful.

The central key feature of Kommander dialogs is that you can bind text
(Kommander Text) to a widget. So if you have @widget1 and @widget2 and
they are line edits you can set Kommander to show their contents by
entering @widgetText in their Kommander Text area. Then enter "hello"
in @widget1 and "world" in @widget2. A button can have the string "My
first @widget1 @widget2 program in Kommander". If you run this dialog
from a console it will output "My first hello world program in
Kommander".

Kommander also seeks to build on standards. It is built on the Qt
Designer framework and creates *.ui files which it renames to *.kmdr.
It can easily import any KDE widget and this can be done without
having to rebuild Kommander, by using plugins.

Kommander's other significant factor is being language neutral and
allowing a Kommander dialog to be extended by using any scripting
language. Kommander positions itself in a unique position for wide
spread adoption. Multiple script languages can be used in a single
dialog and applications can be taken over by people using a different
language than the original developer and gradually converting and
extending it. New widgets and features can be instantly leveraged by
all available languages.

%description kommander -l pl.UTF-8
Kommander to wizualne narzędzie do tworzenia okien dialogowych, które
można rozszerzać o tworzenie pełnych aplikacji z głównym oknem.
Podstawowym celem jest tworzenie jak największej funkcjonalności bez
używania żadnego języka skryptowego. Mają to umożliwić następujące
cechy:
- specjalne oznaczenia - poprzedzone znakiem "@", jak @widgetText.
  Oferują one specjalne możliwości, takie jak wartość widgetu, funkcje,
  aliasy, zmienne globalne itp.
- integracja DCOP - umożliwia oknom Kommandera sterowanie i bycie
  sterowanym w interakcji z innymi aplikacjami KDE.
- Sygnały i sloty - są nieco mniej intuicyjne dla nowego użytkownika.
  Jeszcze nie zostało ostatecznie ustalone, jak te rzeczy będą
  przetwarzane w pierwszym wydaniu. Oferują one ograniczony model
  zdarzeniowy dla sytuacji wciśnięcia przycisku czy zmiany widgetu. W
  połączeniu z "Population Text" są dosyć potężnym narzędziem.

Kluczową cechą okien dialogowych Kommandera jest to, że można
przywiązać tekst (Kommander Text) do widgetu. Jeśli mamy @widget1 i
@widget2, i są one liniami edycji, można ustawić Kommandera, by
pokazywał ich zawartość poprzez wpisanie @widgetText w ich polach
Kommander Text. Potem można wpisać "hello" w @widget1 i "world" w
@widget2. Przycisk może mieć łańcuch "Mój pierwszy program @widget1
@widget2 w Kommanderze". Jeśli uruchomimy to okno dialogowe z konsoli,
wypisze ono "Mój pierwszy program hello world w Kommanderze".

Kommander także usiłuje być oparty na standardach. Jest zbudowany na
środowisku Qt Designera i tworzy pliki *.ui, którym zmienia nazwy na
- *.kmdr. Może łatwo zaimportować dowolny widget KDE, co można łatwo
  zrobić poprzez użycie wtyczek, bez potrzeby przebudowywania
  Kommandera.

Kolejnym znaczącym czynnikiem Kommandera jest bycie niezależnym od
języka i możliwość rozszerzania poprzez użycie dowolnego języka
skryptowego. Konqueror plasuje się na unikalnej pozycji do szeroko
rozpowszechnionej adopcji. W jednym oknie dialogowym można użyć wiele
języków skryptowych, a aplikacje mogą być przejęte przez ludzi
używających innego języka niż oryginalny twórca, a później stopniowo
konwertowane i rozszerzane. Nowe widgety i możliwości mogą być
natychmiast poddane wszystkim dostępnym językom.

%package kommander-executor
Summary:	Kommander executor
Summary(pl.UTF-8):	Wykonawca Kommandera
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description kommander-executor
Executor of Kommander scripts.

%description kommander-executor -l pl.UTF-8
Wykonawca skryptów Kommandera.

%package kommander-devel
Summary:	Development files for kommander
Summary(pl.UTF-8):	Nagłówki dla kommandera
Group:		X11/Development/Libraries
Requires:	%{name}-kommander-executor = %{version}-%{release}
Provides:	quanta-devel = %{version}-%{release}
Obsoletes:	quanta-devel

%description kommander-devel
Development files for kommander.

%description kommander-devel -l pl.UTF-8
Nagłówki dla kommandera.

%package kxsldbg
Summary:	KXsldbg - graphical debugger and frontend to xsldbg
Summary(pl.UTF-8):	KXsldbg - graficzny debugger i frontend do xsldbg
Group:		X11/Development/Tools
Requires:	kde4-kdebase >= %{version}
Conflicts:	quanta < 1:3.2.3

%description kxsldbg
KXsldbg is a graphical debugger and a frontend to xsldbg. It allows
to:
- set and modify breakpoints
- display value of expressions
- display information about breakpoints, templates, variables,
  callstack, stylesheets and entities found
- move around XSL source and XML document via XPaths
- lookup PUBLIC and SYSTEM ID's in the current XML catalog

%description kxsldbg -l pl.UTF-8
KXsldbg to graficzny debugger i frontend do xsldbg. Pozwana na:
- ustawianie i modyfikowanie pułapek
- wyświetlanie wartości wyrażeń
- wyświetlanie informacji o znalezionych pułapkach, szablonach,
  zmiennych, stosie wywołań, arkuszach stylów i encjach
- przenoszenie źródła XSL i dokumentu XML poprzez XPaths
- wyszukiwanie identyfikatorów PUBLIC i SYSTEM w bieżącym katalogu XML

%package quanta
Summary:	Web development tool for KDE
Summary(es.UTF-8):	Uno editor WEB para KDE
Summary(pl.UTF-8):	Narzędzie do tworzenia WWW dla KDE
Summary(pt_BR.UTF-8):	Um editor web para o KDE
Group:		X11/Development/Tools
Requires:	kde4-kdebase >= %{version}
# Applications required for full functionality:
Requires:	kde4-kdesdk-kompare
Requires:	kde4-kdewebdev-kfilereplace
Requires:	kde4-kdewebdev-kimagemapeditor
Requires:	kde4-kdewebdev-klinkstatus
Requires:	kde4-kdewebdev-kommander
Requires:	kde4-kdewebdev-kxsldbg

%description quanta
Quanta Plus is a web development tool for the K Desktop Environment.
Quanta is designed for quick web development and is rapidly becoming a
mature editor with a number of great features.

%description quanta -l es.UTF-8
Quanta Plus és una herramienta de desarrollo web para KDE. Es
projetado para rapido desarrollo web e es casi pronto com excelent
quantidad de caracteristicas.

%description quanta -l pl.UTF-8
Quanta Plus to narzędzie do tworzenia WWW dla środowiska KDE. Służy do
szybkiego tworzenia stron i staje się dojrzałym edytorem z wieloma
przydatnymi możliwościami.

%description quanta -l pt_BR.UTF-8
O Quanta Plus é uma ferramenta para desenvolvimento web para o KDE. É
projetado para desenvolvimento web rápido e está rapidamente se
tornando um editor maduro com um bom número de excelentes
características.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-LIBTIDY_INCLUDE_DIR=%{_includedir} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang kfilereplace	--with-kde
%find_lang kimagemapeditor --with-kde
%find_lang klinkstatus	--with-kde
#%find_lang kommander	--with-kde
#%find_lang kxsldbg	--with-kde
#%find_lang quanta	--with-kde
#%find_lang xsldbg	--with-kde
#cat xsldbg.lang >> kxsldbg.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	kommander-executor -p /sbin/ldconfig
%postun	kommander-executor -p /sbin/ldconfig

%post	klinkstatus	-p /sbin/ldconfig
%postun	klinkstatus	-p /sbin/ldconfig

%files kfilereplace -f kfilereplace.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfilereplace
%attr(755,root,root) %{_libdir}/kde4/libkfilereplacepart.so
%{_datadir}/apps/kfilereplace
%{_datadir}/apps/kfilereplacepart
%{_datadir}/kde4/services/kfilereplacepart.desktop
%{_desktopdir}/kde4/kfilereplace.desktop
%{_iconsdir}/[!l]*/*/apps/kfilereplace.png

%files kimagemapeditor -f kimagemapeditor.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kimagemapeditor
%attr(755,root,root) %{_libdir}/kde4/libkimagemapeditor.so
%{_datadir}/apps/kimagemapeditor
%{_datadir}/kde4/services/kimagemapeditorpart.desktop
%{_desktopdir}/kde4/kimagemapeditor.desktop
%{_iconsdir}/[!l]*/*/apps/kimagemapeditor.png

%files klinkstatus -f klinkstatus.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klinkstatus
%attr(755,root,root) %{_libdir}/libklinkstatuscommon.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libklinkstatuscommon.so.4
%attr(755,root,root) %{_libdir}/kde4/klinkstatuspart.so
%attr(755,root,root) %{_libdir}/kde4/krossmoduleklinkstatus.so
%{_datadir}/apps/klinkstatus
%{_datadir}/apps/klinkstatuspart
%{_datadir}/kde4/services/klinkstatus_part.desktop
%{_datadir}/kde4/services/krossmoduleklinkstatus.desktop
%{_desktopdir}/kde4/klinkstatus.desktop
%{_iconsdir}/hicolor/*/apps/klinkstatus.png
%{_datadir}/dbus-1/interfaces/org.kde.kfilereplace.xml
%{_datadir}/dbus-1/interfaces/org.kde.kdewebdev.klinkstatus.SearchManager.xml
#%{_datadir}/dbus-1/interfaces/org.kde.kdewebdev.klinkstatus.SearchManagerAgent.xml
%{_iconsdir}/hicolor/22x22/actions/addpoint.png
%{_iconsdir}/hicolor/22x22/actions/arrow.png
%{_iconsdir}/hicolor/22x22/actions/circle.png
%{_iconsdir}/hicolor/22x22/actions/circle2.png
%{_iconsdir}/hicolor/22x22/actions/freehand.png
%{_iconsdir}/hicolor/22x22/actions/lower.png
%{_iconsdir}/hicolor/22x22/actions/polygon.png
%{_iconsdir}/hicolor/22x22/actions/raise.png
%{_iconsdir}/hicolor/22x22/actions/rectangle.png
%{_iconsdir}/hicolor/22x22/actions/removepoint.png

%files klinkstatus-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libklinkstatuscommon.so
%{_libdir}/kde4/automationklinkstatus.so
%{_datadir}/kde4/services/klinkstatus_automation.desktop
%{_datadir}/config/klinkstatus.knsrc

#%files kommander -f kommander.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kmdr-editor
#%attr(755,root,root) %{_bindir}/kmdr-plugins
#%{_datadir}/mimelnk/application/x-kommander.desktop
#%{_desktopdir}/kde/kmdr-editor.desktop
#%{_datadir}/apps/kommander
#%{_iconsdir}/crystalsvg/*/apps/kommander.png
#%{_datadir}/apps/katepart/syntax/kommander.xml

%files kommander-executor
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kommander
%attr(755,root,root) %ghost %{_libdir}/libkommandercore.so.?
%attr(755,root,root) %{_libdir}/libkommandercore.so.*.*.*
%{_datadir}/applnk/.hidden/kommander.desktop

##widgets
%attr(755,root,root) %ghost %{_libdir}/libkommanderwidgets.so.?
%attr(755,root,root) %{_libdir}/libkommanderwidgets.so.*.*.*

#%attr(755,root,root) %{_bindir}/kmdr-executor
#%attr(755,root,root) %{_libdir}/libkommanderplugin.so.*.*.*
#%attr(755,root,root) %{_libdir}/libkommanderwidget.so.*.*.*
#%attr(755,root,root) %{_libdir}/libkommanderwidgets.so.*.*.*
#%{_datadir}/applnk/.hidden/kmdr-executor.desktop

%files kommander-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkommanderwidgets.so
%attr(755,root,root) %{_libdir}/libkommandercore.so
%{_includedir}/kommanderwidget.h
%{_includedir}/kommandercore_export.h
%{_includedir}/kommanderplugin.h
%{_includedir}/specials.h

#%files kxsldbg -f kxsldbg.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kxsldbg
#%attr(755,root,root) %{_bindir}/xsldbg
#%attr(755,root,root) %{_libdir}/kde4/libkxsldbgpart.so
#%{_desktopdir}/kde4/kxsldbg.desktop
#%{_desktopdir}/kde4/xsldbg.desktop
#%{_datadir}/apps/kxsldbgpart
#%{_datadir}/apps/kxsldbg
#%{_datadir}/apps/xsldbg
#%{_datadir}/dbus-1/interfaces/org.kde.kxsldbg.kxsldbg.xml
#%{_iconsdir}/hicolor/*/apps/kxsldbg.png
#%{_datadir}/kde4/services/kxsldbg_part.desktop
#%{_iconsdir}/hicolor/*/actions/run.png
#%{_iconsdir}/hicolor/*/actions/xsldbg_*.png
#%{_iconsdir}/hicolor/*/actions/step.png
#%{_iconsdir}/hicolor/*/actions/next.png
#%{_iconsdir}/hicolor/*/actions/1downarrow.png
#%{_iconsdir}/hicolor/*/actions/exit.png
#%{_iconsdir}/hicolor/*/actions/configure.png
#%{_iconsdir}/hicolor/*/actions/mark.png
#%{_iconsdir}/hicolor/*/actions/hash.png
#%{_mandir}/man1/xsldbg.1*

#%files quanta -f quanta.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/quanta
#%attr(755,root,root) %{_libdir}/kde4/quantadebuggergubed.so
#%attr(755,root,root) %{_libdir}/kde4/quantadebuggerdbgp.so
#%{_datadir}/apps/kafkapart
#%{_datadir}/apps/quanta
#%{_datadir}/mimelnk/application/x-webprj.desktop
#%{_datadir}/services/quanta_preview_config.desktop
#%{_datadir}/services/quantadebuggergubed.desktop
#%{_datadir}/services/quantadebuggerdbgp.desktop
#%{_datadir}/servicetypes/quantadebugger.desktop
#%{_desktopdir}/kde/quanta.desktop
#%{_iconsdir}/[!l]*/*/apps/quanta.png
#%{_iconsdir}/[!l]*/*/actions/[!x]*.png
