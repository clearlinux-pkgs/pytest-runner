#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-runner
Version  : 2.12.1
Release  : 24
URL      : https://pypi.debian.net/pytest-runner/pytest-runner-2.12.1.tar.gz
Source0  : https://pypi.debian.net/pytest-runner/pytest-runner-2.12.1.tar.gz
Summary  : Invoke py.test as distutils command with dependency resolution
Group    : Development/Tools
License  : MIT
Requires: pytest-runner-legacypython
Requires: pytest-runner-python3
Requires: pytest-runner-python
Requires: Sphinx
Requires: pytest
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/pytest-runner.svg
:target: https://pypi.org/project/pytest-runner

%package legacypython
Summary: legacypython components for the pytest-runner package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pytest-runner package.


%package python
Summary: python components for the pytest-runner package.
Group: Default
Requires: pytest-runner-legacypython
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
%setup -q -n pytest-runner-2.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507169966
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507169966
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
