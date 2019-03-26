# Created by pyp2rpm-3.3.2
%global pypi_name rst2ansi

Name:           python-%{pypi_name}
Version:        0.1.5
Release:        1%{?dist}
Summary:        A rst converter to ansi-decorated console output

License:        MIT
URL:            https://github.com/Snaipe/python-rst-to-ansi
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
|build| |downloads| |pyversions| |format|A python module dedicated to rendering
RST (reStructuredText) documents to ansi-escaped strings suitable for display
in a terminal.|asciicast|Installation Requirements Python 3.3+PyPi package ..
code:: bash pip install rst2ansiUsage As a CLI utility: .. code:: bash usage:
rst2ansi [-h] [file] Prints a reStructuredText input in an ansi-decorated
format...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
|build| |downloads| |pyversions| |format|A python module dedicated to rendering
RST (reStructuredText) documents to ansi-escaped strings suitable for display
in a terminal.|asciicast|Installation Requirements Python 3.3+PyPi package ..
code:: bash pip install rst2ansiUsage As a CLI utility: .. code:: bash usage:
rst2ansi [-h] [file] Prints a reStructuredText input in an ansi-decorated
format...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/rst2ansi
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 0.1.5-1
- Initial package.