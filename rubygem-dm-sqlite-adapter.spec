# Generated from dm-sqlite-adapter-1.2.0.gem by gem2rpm5 0.6.5 -*- rpm-spec -*-
%define	rbname	dm-sqlite-adapter

Summary:	Sqlite3 Adapter for DataMapper
Name:		rubygem-%{rbname}

Version:	1.2.0
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/datamapper/dm-sqlite-adapter
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Sqlite3 Adapter for DataMapper

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-sqlite-adapter
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-sqlite-adapter/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-sqlite-adapter/spec
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-sqlite-adapter/spec/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
