%if 0%{?rhel} >= 7
%global with_python3 1
%{!?python3_version: %global python3_version %(%{__python3} -c "import sys; sys.stdout.write(sys.version[:3])")}
%else
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

%global upstream_name Sphinx

Name:       python-sphinx
Version:    1.2.3
Release:    5%{?dist}
Summary:    Python documentation generator

Group:      Development/Tools

# Unless otherwise noted, the license for code is BSD
# sphinx/util/stemmer.py Public Domain
# sphinx/pycode/pgen2 Python
# jquery (MIT or GPLv2)
License:    BSD and Public Domain and Python and (MIT or GPLv2)
URL:        http://sphinx.pocoo.org/
Source0:    http://pypi.python.org/packages/source/S/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
Patch0:     Sphinx-1.2.1-mantarget.patch
Patch1:     Sphinx-1.2.2-verbosetests.patch

BuildArch:     noarch
BuildRequires: python2-devel >= 2.4
BuildRequires: python-setuptools
BuildRequires: python-docutils
BuildRequires: python-jinja2
BuildRequires: python-pygments

# for fixes
BuildRequires: dos2unix

# for testing
BuildRequires: python-nose
BuildRequires: gettext
BuildRequires: texinfo
BuildRequires: python-sqlalchemy
BuildRequires: python-whoosh
# note: no Python3 xapian binding yet
BuildRequires: xapian-bindings-python
BuildRequires: texlive-collection-fontsrecommended
BuildRequires: texlive-collection-latex
BuildRequires: tex(cmap.sty)
BuildRequires: tex(ecrm1000.tfm)
BuildRequires: tex(fancybox.sty)
BuildRequires: tex(footnote.sty)
BuildRequires: tex(framed.sty)
BuildRequires: tex(multirow.sty)
BuildRequires: tex(parskip.sty)
BuildRequires: tex(titlesec.sty)
BuildRequires: tex(threeparttable.sty)
BuildRequires: tex(upquote.sty)
BuildRequires: tex(wrapfig.sty)


%if 0%{?with_python3}
BuildRequires: python34-devel
BuildRequires: python34-setuptools
BuildRequires: python34-docutils
BuildRequires: python34-jinja2
BuildRequires: python34-pygments
BuildRequires: python34-nose
BuildRequires: python34-sqlalchemy
BuildRequires: python34-whoosh
%endif # with_python3

Requires:      python-docutils
Requires:      python-jinja2
Requires:      python-pygments

%description
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

Sphinx uses reStructuredText as its markup language, and many of its
strengths come from the power and straightforwardness of
reStructuredText and its parsing and translating suite, the Docutils.

Although it is still under constant development, the following
features are already present, work fine and can be seen "in action" in
the Python docs:

    * Output formats: HTML (including Windows HTML Help) and LaTeX,
      for printable PDF versions
    * Extensive cross-references: semantic markup and automatic links
      for functions, classes, glossary terms and similar pieces of
      information
    * Hierarchical structure: easy definition of a document tree, with
      automatic links to siblings, parents and children
    * Automatic indices: general index as well as a module index
    * Code handling: automatic highlighting using the Pygments highlighter
    * Various extensions are available, e.g. for automatic testing of
      snippets and inclusion of appropriately formatted docstrings.


%package latex
Summary:       LaTeX builder dependencies for %{name}
Requires:      %{name} = %{version}-%{release}
Requires:      texlive-collection-fontsrecommended
Requires:      texlive-collection-latex
Requires:      tex(cmap.sty)
Requires:      tex(ecrm1000.tfm)
Requires:      tex(fancybox.sty)
Requires:      tex(footnote.sty)
Requires:      tex(framed.sty)
Requires:      tex(multirow.sty)
Requires:      tex(parskip.sty)
Requires:      tex(titlesec.sty)
Requires:      tex(threeparttable.sty)
Requires:      tex(upquote.sty)
Requires:      tex(wrapfig.sty)

%description latex
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

This package pulls in the TeX dependencies needed by Sphinx's LaTeX
builder.


%if 0%{?with_python3}
%package -n python34-sphinx
Summary:       Python documentation generator
Group:         Development/Tools
Requires:      python34-docutils
Requires:      python34-jinja2
Requires:      python34-pygments

%description -n python34-sphinx
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

Sphinx uses reStructuredText as its markup language, and many of its
strengths come from the power and straightforwardness of
reStructuredText and its parsing and translating suite, the Docutils.

Although it is still under constant development, the following
features are already present, work fine and can be seen "in action" in
the Python docs:

    * Output formats: HTML (including Windows HTML Help) and LaTeX,
      for printable PDF versions
    * Extensive cross-references: semantic markup and automatic links
      for functions, classes, glossary terms and similar pieces of
      information
    * Hierarchical structure: easy definition of a document tree, with
      automatic links to siblings, parents and children
    * Automatic indices: general index as well as a module index
    * Code handling: automatic highlighting using the Pygments highlighter
    * Various extensions are available, e.g. for automatic testing of
      snippets and inclusion of appropriately formatted docstrings.

%package -n python34-sphinx-latex
Summary:       LaTeX builder dependencies for %{name}
Requires:      python3-sphinx = %{version}-%{release}
Requires:      texlive-collection-fontsrecommended
Requires:      texlive-collection-latex
Requires:      tex(cmap.sty)
Requires:      tex(ecrm1000.tfm)
Requires:      tex(fancybox.sty)
Requires:      tex(footnote.sty)
Requires:      tex(framed.sty)
Requires:      tex(multirow.sty)
Requires:      tex(parskip.sty)
Requires:      tex(titlesec.sty)
Requires:      tex(threeparttable.sty)
Requires:      tex(upquote.sty)
Requires:      tex(wrapfig.sty)

%description -n python34-sphinx-latex
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

This package pulls in the TeX dependencies needed by Sphinx's LaTeX
builder.
%endif # with_python3


%package doc
Summary:    Documentation for %{name}
Group:      Documentation
License:    BSD
Requires:   %{name} = %{version}-%{release}

%description doc
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

This package contains documentation in reST and HTML formats.


%prep
%setup -q -n %{upstream_name}-%{version}%{?prerel}
%patch0 -p1 -b .mantarget
# not backing up since every executable file in tests/ results in
# an additional "skipped" test
%patch1 -p1
sed '1d' -i sphinx/pycode/pgen2/token.py

# fix line encoding of bundled jquery.js
dos2unix -k ./sphinx/themes/basic/static/jquery.js

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3


%build
%{__python} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3

pushd doc
make html
make man
rm -rf _build/html/.buildinfo
mv _build/html ..
popd


%install
rm -rf %{buildroot}

# Must do the python3 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
for f in %{buildroot}%{_bindir}/sphinx-*;
do
    mv $f $f-%{python3_version}
    ln -s %{_bindir}/`basename $f-%{python3_version}` $f-3
done
popd
%endif # with_python3

%{__python} setup.py install --skip-build --root %{buildroot}

pushd doc
# Deliver man pages
install -d %{buildroot}%{_mandir}/man1
mv _build/man/sphinx-*.1 %{buildroot}%{_mandir}/man1/
%if 0%{?with_python3}
for f in %{buildroot}%{_mandir}/man1/sphinx-*.1;
do
    cp -p $f $(echo $f | sed -e "s|.1$|-%{python3_version}.1|")
done

# Remove language files, they're identical to the ones from the
# Python 2 build that will be moved to /usr/share below
find %{buildroot}%{python3_sitelib}/sphinx/locale -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -exec rm -rf '{}' \;
%endif # with_python3
popd

# Deliver rst files
rm -rf doc/_build
sed -i 's|python ../sphinx-build.py|/usr/bin/sphinx-build|' doc/Makefile
mv doc reST

# Move language files to /usr/share;
# patch to support this incorporated in 0.6.6
pushd %{buildroot}%{python_sitelib}

for lang in `find sphinx/locale -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -printf "%f "`;
do
  install -d %{buildroot}%{_datadir}/sphinx/locale/$lang
  install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mv sphinx/locale/$lang/LC_MESSAGES/sphinx.js \
     %{buildroot}%{_datadir}/sphinx/locale/$lang/
  mv sphinx/locale/$lang/LC_MESSAGES/sphinx.mo \
    %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
  rm -rf sphinx/locale/$lang
done
popd
%find_lang sphinx

# Language files; Since these are javascript, it's not immediately obvious to
# find_lang that they need to be marked with a language.
(cd %{buildroot} && find . -name 'sphinx.js') | sed -e 's|^.||' | sed -e \
  's:\(.*/locale/\)\([^/_]\+\)\(.*\.js$\):%lang(\2) \1\2\3:' \
  >> sphinx.lang


%check
LANG=en_US.UTF-8 make test ||:
%if 0%{?with_python3}
pushd %{py3dir}
LANG=en_US.UTF-8 PYTHON=python3 make test ||:
popd
%endif # with_python3


%files -f sphinx.lang
%license LICENSE
%doc AUTHORS CHANGES EXAMPLES README.rst TODO
%exclude %{_bindir}/sphinx-*-3
%exclude %{_bindir}/sphinx-*-%{python3_version}
%{_bindir}/sphinx-*
%{python_sitelib}/*
%dir %{_datadir}/sphinx/
%dir %{_datadir}/sphinx/locale
%dir %{_datadir}/sphinx/locale/*
%exclude %{_mandir}/man1/sphinx-*-%{python3_version}.1*
%{_mandir}/man1/*

%files latex
%license LICENSE

%if 0%{?with_python3}
%files -n python34-sphinx -f sphinx.lang
%license LICENSE
%doc AUTHORS CHANGES EXAMPLES README.rst TODO
%{_bindir}/sphinx-*-3
%{_bindir}/sphinx-*-%{python3_version}
%{python3_sitelib}/*
%dir %{_datadir}/sphinx/
%dir %{_datadir}/sphinx/locale
%dir %{_datadir}/sphinx/locale/*
%{_mandir}/man1/sphinx-*-%{python3_version}.1*

%files -n python34-sphinx-latex
%license LICENSE
%endif # with_python3

%files doc
%doc html reST


%changelog
