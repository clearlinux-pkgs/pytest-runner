#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-runner
Version  : 5.3.1
Release  : 68
URL      : https://files.pythonhosted.org/packages/2a/04/c3223812b3427ffa95110c5781eae7fe8bc3e9e1fe4e2328bee17b9e5820/pytest-runner-5.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/2a/04/c3223812b3427ffa95110c5781eae7fe8bc3e9e1fe4e2328bee17b9e5820/pytest-runner-5.3.1.tar.gz
Summary  : Invoke py.test as distutils command with dependency resolution
Group    : Development/Tools
License  : MIT
Requires: pytest-runner-license = %{version}-%{release}
Requires: pytest-runner-python = %{version}-%{release}
Requires: pytest-runner-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/pytest-runner.svg
:target: `PyPI link`_

%package license
Summary: license components for the pytest-runner package.
Group: Default

%description license
license components for the pytest-runner package.


%package python
Summary: python components for the pytest-runner package.
Group: Default
Requires: pytest-runner-python3 = %{version}-%{release}

%description python
python components for the pytest-runner package.


%package python3
Summary: python3 components for the pytest-runner package.
Group: Default
Requires: python3-core
Provides: pypi(pytest_runner)

%description python3
python3 components for the pytest-runner package.


%prep
%setup -q -n pytest-runner-5.3.1
cd %{_builddir}/pytest-runner-5.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621449609
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest-runner
cp %{_builddir}/pytest-runner-5.3.1/LICENSE %{buildroot}/usr/share/package-licenses/pytest-runner/8e6689d37f82d5617b7f7f7232c94024d41066d1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytest-runner/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
