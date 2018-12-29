#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-runner
Version  : 4.2
Release  : 41
URL      : https://files.pythonhosted.org/packages/9e/b7/fe6e8f87f9a756fd06722216f1b6698ccba4d269eac6329d9f0c441d0f93/pytest-runner-4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/9e/b7/fe6e8f87f9a756fd06722216f1b6698ccba4d269eac6329d9f0c441d0f93/pytest-runner-4.2.tar.gz
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
:target: https://pypi.org/project/pytest-runner

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

%description python3
python3 components for the pytest-runner package.


%prep
%setup -q -n pytest-runner-4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541271787
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest-runner
cp LICENSE %{buildroot}/usr/share/package-licenses/pytest-runner/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytest-runner/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
