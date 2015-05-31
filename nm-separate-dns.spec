%define		date 20150531
%define		gittag v%{date}

Name:		nm-separate-dns
Version:	%{date}
Release:	1%{?dist}
Summary:	Generate dnsmasq config files per connection to separate dns queries

Group:		System Environment/Base
License:	GPLv2
URL:		https://github.com/nixpanic/nm-separate-dns
Source0:	https://github.com/nixpanic/%{name}/archive/%{gittag}/%{name}-%{gittag}.tar.gz

Requires:	NetworkManager, dnsmasq

%description
Automatically configure `dnsmasq` to separate DNS queries based on the domain
name. This is helpful if you have a local private LAN with its own DNS server,
and need to connect to a VPN which serves a different private domain.


%prep
%setup -qn %{name}-%{date}


%build


%install
install -D -m 0755 90-update-resolv.conf %{buildroot}/etc/NetworkManager/dispatcher.d/90-update-resolv.conf
install -D -m 0644 nm-separate-dns.conf %{buildroot}/etc/dnsmasq.d/nm-separate-dns.conf


%files
%doc README.md LICENSE
/etc/NetworkManager/dispatcher.d/90-update-resolv.conf
%config(noreplace) /etc/dnsmasq.d/nm-separate-dns.conf


%changelog
* Sun May 31 2015 Niels de Vos <niels@nixpanic.net> - 20150530-1
- Make this work on Fedora 22

* Sat May 30 2015 Niels de Vos <niels@nixpanic.net> - 20150530-1
- Correct building from the git-tag

* Tue Mar 24 2015 Niels de Vos <niels@nixpanic.net> - 20150324-1
- Add nm-separate-dns.conf as dnsmasq config file

* Sat Jan 17 2015 Harald Jensas <hjensas@redhat.com> - 20150117-1
- Removed /etc/resolv.conf.dnsmasq, replace by cat << EOF in 90-update-resolv.conf

* Thu Dec 25 2014 Niels de Vos <niels@nixpanic.net> - 20141225-1
- Initial packaging
