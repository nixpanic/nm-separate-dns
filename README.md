# Generate dnsmasq config files per connection to separate dns queries

Automatically configure `dnsmasq` to separate DNS queries based on the domain
name. This is helpful if you have a local private LAN with its own DNS server,
and need to connect to a VPN which serves a different private domain.

## Environment where this script can be used

The following network environment benefits from this script:
- local (home) LAN with its own recursive DNS server (`example.net`)
- remote VPN (work) with its own non-recursive DNS (`example.com`)

Sending a DNS query for `example.com` to the `example.net` DNS server will not
return a useful address. Neither will sending an `example.net` request to the
`example.com` DNS server get anything. The configuration in `/etc/resolv.conf`
is limited, and it is not possible to specify a dedicated DNS server for a
specific domain.

[`dnsmasq`][dnsmasq] is a caching DNS server that has a very flexible
configuration. Because many workstations have `dnsmasq` installed already (it
is a dependency for `libvirt`), using `dnsmasq` for configuring a local DNS
server should (mostly) not require additional dependencies.

## Installation

1. Copy the `90-update-resolv.conf` script to
   `/etc/NetworkManager/dispatcher.d/` and make it executable.

2. Create the `/etc/dnsmasq.d/localhost.conf` with the following content

   ```
   no-resolv
   no-poll
   interface=lo
   no-dhcp-interface=lo
   bind-interfaces
   ```

3. Install and enable `dnsmasq`:

   ```
   # yum install dnsmasq
   # systemctl enable dnsmasq
   # systemctl start dnsmasq
   ```

4. (Re)Connect your LAN, WiFi and VPN.

## Previous versions and upstream repository

The script was [initially posted][blogpost] for RHEL-6, but it seems that
NetworkManager (mainly `nmcli`) is a moving target and requires to some changes
for this script to keep working.

The latest version of this script is available in its [github
repository][gitrepo].

[dnsmasq]: http://www.thekelleys.org.uk/dnsmasq/doc.html
[blogpost]: http://blog.nixpanic.net/2013/03/use-dnsmasq-for-separating-dns-queries.html
[gitrepo]: https://github.com/nixpanic/nm-separate-dns
