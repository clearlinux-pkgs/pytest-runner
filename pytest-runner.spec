#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-runner
Version  : 4.2
Release  : 33
URL      : https://pypi.debian.net/pytest-runner/pytest-runner-4.2.tar.gz
Source0  : https://pypi.debian.net/pytest-runner/pytest-runner-4.2.tar.gz
Summary  : Invoke py.test as distutils command with dependency resolution
Group    : Development/Tools
License  : MIT
Requires: pytest-runner-python3
Requires: pytest-runner-python
Requires: Sphinx
Requires: pytest
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/pytest-runner.svg
:target: https://pypi.org/project/pytest-runner

%package python
Summary: python components for the pytest-runner package.
Group: Default
Requires: pytest-runner-python3

%description python
python components for the pytest-runner package.


%package python3
Summary: python3 components for the pytest-runner package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pytest-runner package.


%prep
%setup -q -n pytest-runner-4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522378191
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
