%define name iwlwifi-6030-ucode
%define tarname iwlwifi-6000g2b-ucode
%define version 17.168.5.1
%define release %mkrel 1

Summary: Intel PRO/Wireless 6030AGN microcode
Name:	 %{name}
Version: %{version}
Release: %{release}
Source0: http://www.intellinuxwireless.org/iwlwifi/downloads/%{tarname}-%{version}.tgz
License: Proprietary
Group:	 System/Kernel and hardware
Url:	 http://intellinuxwireless.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
The file iwlwifi-6000g2b-*.ucode provided in this package is required to be
present on your system in order for the Intel PRO/Wireless 6030AGN Network
Connection Adapter driver for Linux (iwlagn) to be able to operate on
your system.

%prep
%setup -q -n %{tarname}-%{version}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/firmware
install -m644 *.ucode %{buildroot}/lib/firmware/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE.* README.*
/lib/firmware/*.ucode
