#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-calcite
Version  : 1.2.0.incubating
Release  : 1
URL      : https://github.com/apache/calcite/archive/calcite-1.2.0-incubating.tar.gz
Source0  : https://github.com/apache/calcite/archive/calcite-1.2.0-incubating.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/calcite/calcite-core/1.2.0-incubating/calcite-core-1.2.0-incubating.jar
Source2  : https://repo1.maven.org/maven2/org/apache/calcite/calcite-core/1.2.0-incubating/calcite-core-1.2.0-incubating.pom
Source3  : https://repo1.maven.org/maven2/org/apache/calcite/calcite/1.2.0-incubating/calcite-1.2.0-incubating.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-calcite-data = %{version}-%{release}

%description
Apache Calcite release 1.2.0 (incubating)
This is a source or binary distribution of Apache Calcite.

%package data
Summary: data components for the mvn-calcite package.
Group: Data

%description data
data components for the mvn-calcite package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.2.0-incubating
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.2.0-incubating

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.2.0-incubating
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.2.0-incubating

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite/1.2.0-incubating
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite/1.2.0-incubating


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.2.0-incubating/calcite-core-1.2.0-incubating.jar
/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.2.0-incubating/calcite-core-1.2.0-incubating.pom
/usr/share/java/.m2/repository/org/apache/calcite/calcite/1.2.0-incubating/calcite-1.2.0-incubating.pom
