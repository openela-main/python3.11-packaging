%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

%global pypi_name packaging

# Tests are disabled in RHEL because we don't have python-pretend.
# Specify --with tests to enable them.
%bcond_with tests

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        21.3
Release:        1%{?dist}
Summary:        Core utilities for Python packages

License:        BSD or ASL 2.0
URL:            https://github.com/pypa/packaging
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

# Correctly parse ELF for musllinux on Big Endian
# Merged upstream
Patch:          https://github.com/pypa/packaging/pull/538.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools

# Upstream uses nox for testing.
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pretend
%endif

# On RHEL8 we need to manually specify the runtime requirements.
# On RHEL9 they are auto-generated but we keep them for consistency.
Requires:       python%{python3_pkgversion}dist(pyparsing)

%global _description %{expand:
python-packaging provides core utilities for Python packages like utilities for
dealing with versions, specifiers, markers etc.}

%description %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
%pytest
%endif


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc README.rst CHANGELOG.rst CONTRIBUTING.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*-info/


%changelog
* Fri Nov 25 2022 Charalampos Stratakis <cstratak@redhat.com> - 21.3-1
- Initial package
- Fedora contributions by:
      # Charalampos Stratakis <cstratak@redhat.com>
      # Iryna Shcherbina <shcherbina.iryna@gmail.com>
      # Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com>
      # Lumir Balhar <lbalhar@redhat.com>
      # Miro Hrončok <miro@hroncok.cz>
      # Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl>
