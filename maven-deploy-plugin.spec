Name:           maven-deploy-plugin
Version:        2.7
Release:        11%{?dist}
Summary:        Maven Deploy Plugin

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-deploy-plugin/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch: noarch

# Basic stuff
BuildRequires: jpackage-utils
BuildRequires: java-devel >= 1:1.6.0

# Maven and its dependencies
BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-archiver
BuildRequires: mvn(org.apache.maven:maven-artifact:2.0.6)
BuildRequires: mvn(org.apache.maven:maven-model:2.0.6)
# The following maven packages haven't updated yet
BuildRequires: maven-changes-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-invoker-plugin

# autorequires support for compat packages not finished yet
Requires: mvn(org.apache.maven:maven-artifact:2.0.6)
Requires: mvn(org.apache.maven:maven-model:2.0.6)

%description
Uploads the project artifacts to the internal remote repository.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q

%pom_xpath_inject pom:project "<build><plugins/></build>"
%pom_add_plugin :maven-plugin-plugin . "
        <configuration>
          <helpPackageName>org.apache.maven.plugin.deploy</helpPackageName>
        </configuration>"

%build
# A test class doesn't compile
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc DEPENDENCIES LICENSE NOTICE
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.7-11
- Mass rebuild 2013-12-27

* Mon Aug 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.7-10
- Migrate away from mvn-rpmbuild (#997454)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.7-9
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.7-8
- Remove unneeded BR: maven-idea-plugin

* Mon Mar 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.7-7
- Drop patch for maven-compat
- Add missing requires on maven2 artifact and model
- Explictly set helpPackageName in maven-plugin-plugin configuration
- Resolves: rhbz#914167

* Tue Feb 26 2013 Weinan Li <weli@redhat.com> - 2.7-6
- bz915609
- Remove doxia dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.7-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 20 2011 Tomas Radej <tradej@redhat.com> - 2.7-1
- Update to upstream 2.7
- Guidelines fixes

* Tue May 17 2011 Alexander Kurtakov <akurtako@redhat.com> 2.6-1
- Update to upstream 2.6.
- Adapt to current guidelines.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 10 2010 Weinan Li <weli@redhat.com> - 0:2.5-5
- skip test during building

* Wed Jun 2 2010 Weinan Li <weli@redhat.com> - 0:2.5-4
- remove the Epoch section

* Wed Jun 2 2010 Weinan Li <weli@redhat.com> - 0:2.5-3
- Fix URL
- Add Epoch

* Wed Jun 2 2010 Weinan Li <weli@redhat.com> - 2.5-2
- depmap removed
- Use new BRs for some already updated maven components
- obsolete/provide maven2-plugin-deploy
- Remove the empty line between changelog and the changelog entry

* Mon May 31 2010 Weinan Li <weli@redhat.com> - 2.5-1
- Initial Package
