%define		commit 1a46825a7d8734f4d1315455e4de8dfc9813f716

Name:		nm-separate-dns
Version:	20141225
Release:	1%{?dist}
Summary:	Generate dnsmasq config files per connection to separate dns queries

Group:		System Environment/Base
License:	GPLv2
URL:		https://github.com/nixpanic/nm-separate-dns
Source0:	https://github.com/nixpanic/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

Requires:	NetworkManager, dnsmasq

%description
Automatically configure `dnsmasq` to separate DNS queries based on the domain
name. This is helpful if you have a local private LAN with its own DNS server,
and need to connect to a VPN which serves a different private domain.


%prep
%setup -qn %{name}-%{commit}


%build


%install
install -D -m 0644 resolv.conf.dnsmasq %{buildroot}/etc/resolv.conf.dnsmasq
install -D -m 0755 90-update-resolv.conf %{buildroot}/etc/NetworkManager/dispatcher.d/90-update-resolv.conf


%files
%doc README.md LICENSE
%config(noreplace) /etc/resolv.conf.dnsmasq
/etc/NetworkManager/dispatcher.d/90-update-resolv.conf


%changelog
* Thu Dec 25 2014 Niels de Vos <niels@nixpanic.net> - 20141225-1
- Initial packaging
