# Generated by go2rpm
%ifnarch s390x
%bcond_without check
%endif

%global builddate $(date +"%%Y%%m%%d-%%T")
%global commit_version "e4487274853c587717006eeda8804e597d120340"

# https://github.com/prometheus/prometheus
%global goipath         github.com/prometheus/prometheus
Version:                2.24.1

%gometa

%global common_description %{expand:
The Prometheus monitoring system and time series database.}

%global golicenses      LICENSE NOTICE
%global godocs          docs CHANGELOG.md MAINTAINERS.md CODE_OF_CONDUCT.md\\\
                        CONTRIBUTING.md README.md RELEASE.md\\\
                        documentation

Name:           %{goname}
Release:        3%{?dist}
Summary:        Prometheus monitoring system and time series database

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# unzip Source0
# run 'make assets' in it
# rm -rf web/ui/react-app
# tar czvf web-ui-2.24.1.tar.gz web/ui
Source10:       web-ui-%{version}.tar.gz
Source1:        prometheus.service
Source2:        prometheus
Source3:        prometheus.yml
Source4:        prometheus.conf
Source5:        prometheus.logrotate

# Debian patch for default settings
Patch0:         02-Default_settings.patch

BuildRequires:  systemd-rpm-macros
BuildRequires:  golang(github.com/alecthomas/units)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials/stscreds)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/ec2)
BuildRequires:  golang(github.com/Azure/azure-sdk-for-go/services/compute/mgmt/2018-10-01/compute)
BuildRequires:  golang(github.com/Azure/azure-sdk-for-go/services/network/mgmt/2018-10-01/network)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/adal)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/azure)
BuildRequires:  golang(github.com/cespare/xxhash/v2)
BuildRequires:  golang(github.com/digitalocean/godo)
BuildRequires:  golang(github.com/docker/docker/api/types)
BuildRequires:  golang(github.com/docker/docker/api/types/filters)
BuildRequires:  golang(github.com/docker/docker/api/types/swarm)
BuildRequires:  golang(github.com/docker/docker/client)
BuildRequires:  golang(github.com/edsrzf/mmap-go)
BuildRequires:  golang(github.com/go-kit/kit/log)
BuildRequires:  golang(github.com/go-kit/kit/log/level)
BuildRequires:  golang(github.com/go-logfmt/logfmt)
BuildRequires:  golang(github.com/go-openapi/strfmt)
BuildRequires:  golang(github.com/gogo/protobuf/gogoproto)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/golang/snappy)
BuildRequires:  golang(github.com/google/pprof/profile)
BuildRequires:  golang(github.com/gophercloud/gophercloud)
BuildRequires:  golang(github.com/gophercloud/gophercloud/openstack)
BuildRequires:  golang(github.com/gophercloud/gophercloud/openstack/compute/v2/extensions/floatingips)
BuildRequires:  golang(github.com/gophercloud/gophercloud/openstack/compute/v2/extensions/hypervisors)
BuildRequires:  golang(github.com/gophercloud/gophercloud/openstack/compute/v2/servers)
BuildRequires:  golang(github.com/gophercloud/gophercloud/pagination)
BuildRequires:  golang(github.com/hashicorp/consul/api)
BuildRequires:  golang(github.com/hetznercloud/hcloud-go/hcloud)
# BuildRequires:  golang(github.com/influxdata/influxdb/client/v2)
BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(github.com/miekg/dns)
BuildRequires:  golang(github.com/mwitkow/go-conntrack)
BuildRequires:  golang(github.com/oklog/run)
BuildRequires:  golang(github.com/oklog/ulid)
BuildRequires:  golang(github.com/opentracing-contrib/go-stdlib/nethttp)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/ext)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/prometheus/alertmanager/api/v2/models)
BuildRequires:  golang(github.com/prometheus/client_golang/api)
BuildRequires:  golang(github.com/prometheus/client_golang/api/prometheus/v1)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promauto)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/testutil/promlint)
BuildRequires:  golang(github.com/prometheus/client_model/go)
BuildRequires:  golang(github.com/prometheus/common/config)
BuildRequires:  golang(github.com/prometheus/common/expfmt)
BuildRequires:  golang(github.com/prometheus/common/model)
BuildRequires:  golang(github.com/prometheus/common/promlog)
BuildRequires:  golang(github.com/prometheus/common/promlog/flag)
BuildRequires:  golang(github.com/prometheus/common/route)
BuildRequires:  golang(github.com/prometheus/common/server)
BuildRequires:  golang(github.com/prometheus/common/version)
BuildRequires:  golang(github.com/prometheus/exporter-toolkit/web)
BuildRequires:  golang(github.com/prometheus/exporter-toolkit/web/kingpinflag)
BuildRequires:  golang(github.com/samuel/go-zookeeper/zk)
BuildRequires:  golang(github.com/shurcooL/httpfs/filter)
BuildRequires:  golang(github.com/shurcooL/httpfs/union)
BuildRequires:  golang(github.com/shurcooL/vfsgen)
BuildRequires:  golang(github.com/simonpasquier/klog-gokit)
BuildRequires:  golang(github.com/simonpasquier/klog-gokit/v2)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/uber/jaeger-client-go)
BuildRequires:  golang(github.com/uber/jaeger-client-go/config)
BuildRequires:  golang(github.com/uber/jaeger-lib/metrics/prometheus)
BuildRequires:  golang(go.uber.org/atomic)
BuildRequires:  golang(go.uber.org/goleak)
BuildRequires:  golang(golang.org/x/net/netutil)
BuildRequires:  golang(golang.org/x/oauth2/google)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/time/rate)
BuildRequires:  golang(google.golang.org/api/compute/v1)
BuildRequires:  golang(google.golang.org/api/option)
BuildRequires:  golang(gopkg.in/alecthomas/kingpin.v2)
BuildRequires:  golang(gopkg.in/fsnotify/fsnotify.v1)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(gopkg.in/yaml.v3)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/api/discovery/v1beta1)
BuildRequires:  golang(k8s.io/api/networking/v1beta1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/fields)
BuildRequires:  golang(k8s.io/apimachinery/pkg/labels)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/watch)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/client-go/tools/cache)
BuildRequires:  golang(k8s.io/client-go/tools/metrics)
BuildRequires:  golang(k8s.io/client-go/util/workqueue)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/testutil)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/client-go/kubernetes/fake)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%autosetup -N -T -D -a 10 -n prometheus-%{version}
sed -i "s|klog \"k8s.io/klog\"|klog \"github.com/simonpasquier/klog-gokit\"|" $(find . -iname "*.go" -type f)
sed -i "s|klogv2 \"k8s.io/klog/v2\"|klogv2 \"github.com/simonpasquier/klog-gokit/v2\"|" $(find . -iname "*.go" -type f)
%patch0 -p1


%build
export LDFLAGS="-X github.com/prometheus/common/version.Version=%{version} \
                -X github.com/prometheus/common/version.Revision=%{commit_version} \
                -X github.com/prometheus/common/version.Branch=master \
                -X github.com/prometheus/common/version.BuildUser=mockbuild \
                -X github.com/prometheus/common/version.BuildDate=%{builddate} "
export BUILDTAGS="netgo builtinassets"
for cmd in cmd/* ; do
    %gobuild  -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

# Unit file
install -m 0755 -vd                     %{buildroot}%{_unitdir}
install -m 0644 -vp %{SOURCE1}          %{buildroot}%{_unitdir}/

install -m 0755 -vd                     %{buildroot}%{_sysconfdir}
install -m 0755 -vd                     %{buildroot}%{_sysconfdir}/prometheus
install -m 0644 -vp %{SOURCE3}          %{buildroot}%{_sysconfdir}/prometheus/
install -m 0755 -vd                     %{buildroot}%{_sysconfdir}/sysconfig
install -m 0644 -vp %{SOURCE2}          %{buildroot}%{_sysconfdir}/sysconfig/
install -m 0755 -vd                     %{buildroot}%{_sysconfdir}/logrotate.d
install -m 0644 -vp %{SOURCE5}          %{buildroot}%{_sysconfdir}/logrotate.d/prometheus
install -m 0755 -vd                     %{buildroot}%{_sysusersdir}
install -m 0644 -vp %{SOURCE4}          %{buildroot}%{_sysusersdir}/

mkdir -p %{buildroot}%{_sysconfdir}/prometheus/consoles
mkdir -p %{buildroot}%{_sysconfdir}/prometheus/console_libraries
mkdir -p %{buildroot}%{_sharedstatedir}/prometheus

%pre
%sysusers_create_package prometheus %{SOURCE4}

%post
%systemd_post prometheus.service

%preun
%systemd_preun prometheus.service

%postun
%systemd_postun_with_restart prometheus.service

%if %{with check}
%check
# scrape: needs network
# tsdb: https://github.com/prometheus/prometheus/issues/8393
%gocheck -t cmd -d scrape -d discovery/kubernetes -d web -d tsdb -d tsdb/chunks
%endif

%files
%license LICENSE NOTICE
%doc docs CHANGELOG.md MAINTAINERS.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%doc README.md RELEASE.md documentation
%dir %{_sysconfdir}/prometheus/
%dir %{_sysconfdir}/prometheus/consoles
%dir %{_sysconfdir}/prometheus/console_libraries
%config(noreplace) %{_sysconfdir}/sysconfig/prometheus
%config(noreplace) %{_sysconfdir}/prometheus/prometheus.yml
%config(noreplace) %{_sysconfdir}/logrotate.d/prometheus
%{_bindir}/*
%{_unitdir}/prometheus.service
%{_sysusersdir}/prometheus.conf
%attr(0755,prometheus,prometheus) %{_sharedstatedir}/prometheus

%gopkgfiles

%changelog
* Tue Jan 26 22:05:24 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.24.1-3
- Set default settings in main.go
- Embedded assets in the binary
- Added a logrotate file
- Fix: rhbz#1902496

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 19:43:35 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.24.1-1
- Update to 2.24.1
- Close: rhbz#1918532

* Thu Jan  7 17:40:17 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.24.0-1
- Update to 2.24.0
- Close: rhbz#1911731

* Sat Dec 05 22:54:14 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.23.0-2
- Add new React based UI
- Fix rhbz#1902496

* Thu Dec 03 13:12:59 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.23.0-1
- Update to 2.23.0
- Add configuration
- Close rhbz#1866613
- Fix rhbz#1894089
- Fix rhbz#1902496

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 30 22:32:01 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.20.0-1
- Update to 2.20.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.11.0-4
- Rebuilt for GHSA-jf24-p9p9-4rjh

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 19:29:38 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.11.0-1
- Release 2.11.0

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.9.2-2
- Add Obsoletes for old names

* Wed May 15 03:08:50 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.9.2-1
- Release 2.9.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.8.0-1
- Update to 1.8.0
  resolves: #1495180

* Tue Aug 22 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.15.0-8
- Polish the spec file

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.0-4
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.0-3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 23 2015 jchaloup <jchaloup@redhat.com> - 0.15.0-1
- Update to 0.15.0
  resolves: #1246058

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 jchaloup <jchaloup@redhat.com> - 0.13.3-2
- Add debug info
  related: #1190426

* Tue May 12 2015 jchaloup <jchaloup@redhat.com> - 0.13.3-1
- Update to 0.13.3
  related: #1190426

* Sat May 09 2015 jchaloup <jchaloup@redhat.com> - 0.13.2-1
- Update to 0.13.2
  related: #1190426

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git4e6a807
- First package for Fedora
  resolves: #1190426
