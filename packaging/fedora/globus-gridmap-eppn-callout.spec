%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		globus-gridmap-eppn-callout
%global _name %(echo %{name} | tr - _)
Version:	2.2
Release:	1%{?dist}
Summary:	Grid Community Toolkit - Globus gridmap ePPN callout

Group:		System Environment/Libraries
License:	%{?suse_version:Apache-2.0}%{!?suse_version:ASL 2.0}
URL:		https://github.com/gridcf/gct/
Source:		%{_name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 14
BuildRequires:	globus-gsi-sysconfig-devel >= 5
BuildRequires:	globus-gssapi-gsi-devel >= 9
BuildRequires:	globus-gss-assist-devel >= 8
BuildRequires:	globus-gridmap-callout-error-devel
BuildRequires:	globus-gsi-credential-devel >= 6
BuildRequires:	globus-gsi-cert-utils-devel >= 8
BuildRequires:	globus-gsi-openssl-error-devel >= 2
BuildRequires:	globus-gssapi-error-devel >= 4
%if %{?suse_version}%{!?suse_version:0}
BuildRequires:	libopenssl-devel
%else
BuildRequires:	openssl-devel
%endif

%if %{?suse_version}%{!?suse_version:0}
%global mainpkg lib%{_name}
%global nmainpkg -n %{mainpkg}
%else
%global mainpkg %{name}
%endif

%if %{?nmainpkg:1}%{!?nmainpkg:0}
%package %{?nmainpkg}
Summary:	Grid Community Toolkit - Globus gridmap ePPN callout
Group:		System Environment/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < %{version}-%{release}
%endif

%if %{?nmainpkg:1}%{!?nmainpkg:0}
%description %{?nmainpkg}
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{mainpkg} package contains:
Globus gridmap eduPersonPrincipalName (ePPN) callout
%endif

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus gridmap eduPersonPrincipalName (ePPN) callout

%prep
%setup -q -n %{_name}-%{version}

%build
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir}

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Remove libtool archives (.la files)
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%post %{?nmainpkg} -p /sbin/ldconfig

%postun %{?nmainpkg} -p /sbin/ldconfig

%files %{?nmainpkg}
%defattr(-,root,root,-)
# This is a loadable module (plugin)
%{_libdir}/libglobus_gridmap_eppn_callout.so
%config(noreplace) %{_sysconfdir}/gridmap_eppn_callout-gsi_authz.conf
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/GLOBUS_LICENSE

%changelog
* Wed Aug 21 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.2-1
- Add environment variable GLOBUS_EPPN_FORCE_GRIDMAP to return mapped
  identity from gridmap lookup based on the ePPN

* Tue Mar 05 2019 Globus Toolkit <support@globus.org> - 2.1-1
- add environment variable GLOBUS_EPPN_KEEP_DOMAIN to return full
  userid@domain from eppn

* Sat Mar 31 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.0-1
- First Grid Community Toolkit release
- Remove support for openssl101e (RHEL5 is EOL)

* Thu Sep 08 2016 Globus Toolkit <support@globus.org> - 1.13-1
- Update for el.5 openssl101e

* Mon Aug 29 2016 Globus Toolkit <support@globus.org> - 1.12-2
- Updates for SLES 12

* Sat Aug 20 2016 Globus Toolkit <support@globus.org> - 1.12-1
- Update bug report URL

* Tue May 03 2016 Globus Toolkit <support@globus.org> - 1.11-1
- Missing dependency

* Tue May 03 2016 Globus Toolkit <support@globus.org> - 1.10-1
- Missing dependency

* Mon Dec 14 2015 Globus Toolkit <support@globus.org> - 1.9-1
- GT-373: add support for proxies to eppn callout

* Thu Aug 06 2015 Globus Toolkit <support@globus.org> - 1.8-2
- Add vendor

* Wed Jul 01 2015 Globus Toolkit <support@globus.org> - 1.8-1
- remove unused variable

* Thu Sep 25 2014 Globus Toolkit <support@globus.org> - 1.7-1
- Fix dependency version
- Quiet some autoconf/automake warnings

* Fri Aug 22 2014 Globus Toolkit <support@globus.org> - 1.6-1
- Merge fixes from ellert-globus_6_branch

* Wed Aug 20 2014 Globus Toolkit <support@globus.org> - 1.5-2
- Fix Source path

* Mon Jun 09 2014 Globus Toolkit <support@globus.org> - 1.5-1
- Merge changes from Mattias Ellert

* Fri Apr 18 2014 Globus Toolkit <support@globus.org> - 1.4-1
- Version bump for consistency

* Thu Feb 27 2014 Globus Toolkit <support@globus.org> - 1.3-1
- Packaging fixes, Warning Cleanup

* Tue Feb 25 2014 Globus Toolkit <support@globus.org> - 1.2-1
- Packaging fixes

* Fri Feb 14 2014 Globus Toolkit <support@globus.org> - 1.1-1
- Packaging fixes

* Wed Jan 22 2014 Globus Toolkit <support@globus.org> - 1.0-1
- Repackage for GT6 without GPT

* Mon Oct 28 2013 Globus Toolkit <support@globus.org> - 0.6-1
- Update dependencies for new credential functions

* Mon Oct 28 2013 Globus Toolkit <support@globus.org> - 0.5-2
- Update dependencies for new credential functions

* Fri Oct 25 2013 Globus Toolkit <support@globus.org> - 0.5-1
- Missing configure dependency on OpenSSL

* Wed Jun 26 2013 Globus Toolkit <support@globus.org> - 0.4-2
- GT-424: New Fedora Packaging Guideline - no %%_isa in BuildRequires

* Mon Apr 15 2013 Globus Toolkit <support@globus.org> - 0.4-1
- verify sharing cert chain

* Tue Mar 19 2013 Globus Toolkit <support@globus.org> - 0.3-2
- Update sharing to support a full cert chain at logon

* Tue Mar 12 2013 Globus Toolkit <support@globus.org> - 0.3-1
- Improve error message handling

* Tue Mar 05 2013 Globus Toolkit <support@globus.org> - 0.2-1
- Initial version
