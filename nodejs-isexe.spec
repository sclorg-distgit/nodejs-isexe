%{?scl:%scl_package nodejs-isexe}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global packagename isexe
%global enable_tests 0

Name:		%{?scl_prefix}nodejs-isexe
Version:    1.1.2
Release:    2%{?dist}
Summary:	Minimal module to check if a file is executable

License:	ISC
URL:		https://github.com/isaacs/isexe
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	%{?scl_prefix}nodejs-devel
%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(tap)
%endif

%description
Minimal module to check if a file is executable.

%prep
%setup -q -n package

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

#%check
#%nodejs_symlink_deps --check
#%{__nodejs} -e 'require("./")'
#%if 0%{?enable_tests}
#%{_bindir}/tap test/*.js
#%else
#%{_bindir}/echo "Tests disabled..."
#%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Fri Sep 23 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.2-2
- Built for RHSCL

* Tue Sep 13 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.2-1
- Updated with script

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-2
- Add missing build requirements

* Mon Jan 18 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Initial packaging
