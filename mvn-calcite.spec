#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-calcite
Version  : 1.2.0.incubating
Release  : 3
URL      : https://github.com/apache/calcite/archive/calcite-1.2.0-incubating.tar.gz
Source0  : https://github.com/apache/calcite/archive/calcite-1.2.0-incubating.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/calcite/calcite-core/1.17.0/calcite-core-1.17.0.jar
Source2  : https://repo1.maven.org/maven2/org/apache/calcite/calcite-core/1.17.0/calcite-core-1.17.0.pom
Source3  : https://repo1.maven.org/maven2/org/apache/calcite/calcite-core/1.2.0-incubating/calcite-core-1.2.0-incubating.jar
Source4  : https://repo1.maven.org/maven2/org/apache/calcite/calcite-core/1.2.0-incubating/calcite-core-1.2.0-incubating.pom
Source5  : https://repo1.maven.org/maven2/org/apache/calcite/calcite-linq4j/1.17.0/calcite-linq4j-1.17.0.jar
Source6  : https://repo1.maven.org/maven2/org/apache/calcite/calcite-linq4j/1.17.0/calcite-linq4j-1.17.0.pom
Source7  : https://repo1.maven.org/maven2/org/apache/calcite/calcite-linq4j/1.2.0-incubating/calcite-linq4j-1.2.0-incubating.jar
Source8  : https://repo1.maven.org/maven2/org/apache/calcite/calcite-linq4j/1.2.0-incubating/calcite-linq4j-1.2.0-incubating.pom
Source9  : https://repo1.maven.org/maven2/org/apache/calcite/calcite/1.17.0/calcite-1.17.0.pom
Source10  : https://repo1.maven.org/maven2/org/apache/calcite/calcite/1.2.0-incubating/calcite-1.2.0-incubating.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-calcite-data = %{version}-%{release}
Requires: mvn-calcite-license = %{version}-%{release}

%description
Apache Calcite release 1.2.0 (incubating)
This is a source or binary distribution of Apache Calcite.

%package data
Summary: data components for the mvn-calcite package.
Group: Data

%description data
data components for the mvn-calcite package.


%package license
Summary: license components for the mvn-calcite package.
Group: Default

%description license
license components for the mvn-calcite package.


%prep
%setup -q -n calcite-calcite-1.2.0-incubating

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-calcite
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-calcite/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/mvn-calcite/NOTICE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.17.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.17.0/calcite-core-1.17.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.17.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.17.0/calcite-core-1.17.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.2.0-incubating
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.2.0-incubating/calcite-core-1.2.0-incubating.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.2.0-incubating
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.2.0-incubating/calcite-core-1.2.0-incubating.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-linq4j/1.17.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-linq4j/1.17.0/calcite-linq4j-1.17.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-linq4j/1.17.0
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-linq4j/1.17.0/calcite-linq4j-1.17.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-linq4j/1.2.0-incubating
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-linq4j/1.2.0-incubating/calcite-linq4j-1.2.0-incubating.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-linq4j/1.2.0-incubating
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite-linq4j/1.2.0-incubating/calcite-linq4j-1.2.0-incubating.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite/1.17.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite/1.17.0/calcite-1.17.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite/1.2.0-incubating
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/calcite/calcite/1.2.0-incubating/calcite-1.2.0-incubating.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.17.0/calcite-core-1.17.0.jar
/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.17.0/calcite-core-1.17.0.pom
/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.2.0-incubating/calcite-core-1.2.0-incubating.jar
/usr/share/java/.m2/repository/org/apache/calcite/calcite-core/1.2.0-incubating/calcite-core-1.2.0-incubating.pom
/usr/share/java/.m2/repository/org/apache/calcite/calcite-linq4j/1.17.0/calcite-linq4j-1.17.0.jar
/usr/share/java/.m2/repository/org/apache/calcite/calcite-linq4j/1.17.0/calcite-linq4j-1.17.0.pom
/usr/share/java/.m2/repository/org/apache/calcite/calcite-linq4j/1.2.0-incubating/calcite-linq4j-1.2.0-incubating.jar
/usr/share/java/.m2/repository/org/apache/calcite/calcite-linq4j/1.2.0-incubating/calcite-linq4j-1.2.0-incubating.pom
/usr/share/java/.m2/repository/org/apache/calcite/calcite/1.17.0/calcite-1.17.0.pom
/usr/share/java/.m2/repository/org/apache/calcite/calcite/1.2.0-incubating/calcite-1.2.0-incubating.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-calcite/LICENSE
/usr/share/package-licenses/mvn-calcite/NOTICE
