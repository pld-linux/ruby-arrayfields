%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
Summary:	Hashlike access to arrays
Name:		ruby-arrayfields
Version:	3.4.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.codeforpeople.com/lib/ruby/arrayfields/arrayfields-%{version}.tgz
# Source0-md5:	537e835998e20d019ac33e1bb5503f64
Source1:	setup.rb
URL:		http://raa.ruby-lang.org/project/arrayfields/
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hash-like access to arrays.

%prep
%setup -q -n arrayfields-%{version}

%build
%{__install} %SOURCE1 setup.rb
ruby setup.rb config \
	--rb-dir=%{ruby_rubylibdir}

ruby setup.rb setup

rdoc -o rdoc/ --main README README lib/arrayfields.rb --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/arrayfields.rb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{_examplesdir}/%{name}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/* README
%{ruby_rubylibdir}/arrayfields.rb
%{ruby_ridir}/FieldedArray
%{ruby_ridir}/Fieldable
%{ruby_ridir}/ArrayFields
