%define version 5.7.2

Name: strongswan
Version: %{version}
Release: 1%{?dist}
Summary: OpenSource IPsec-based VPN solution
License: GPLv2+
Url: https://www.strongswan.org/
Source0: https://dist.kanga.org/packages/strongswan-%{version}.tar.bz2
BuildRequires: gmp-devel
BuildRequires: iptables-devel
BuildRequires: python3-devel
Requires: gmp
Requires: iptables
Requires: python3
