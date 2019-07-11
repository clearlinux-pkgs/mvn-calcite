PKG_NAME := mvn-calcite
URL = https://github.com/apache/calcite/archive/calcite-1.2.0-incubating.tar.gz
ARCHIVES = https://repo1.maven.org/maven2/org/apache/calcite/calcite/1.2.0-incubating/calcite-1.2.0-incubating.pom : https://repo1.maven.org/maven2/org/apache/calcite/calcite-core/1.2.0-incubating/calcite-core-1.2.0-incubating.jar : https://repo1.maven.org/maven2/org/apache/calcite/calcite-core/1.2.0-incubating/calcite-core-1.2.0-incubating.pom : 

include ../common/Makefile.common
