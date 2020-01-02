# Cisco-CUCM-find-local-users
CUCM Find Local Users via AXL SQL

This is a small example of how to find users created in Cisco CUCM locally verses LDAP synched.  This is helpful since the current 12.5 admin GUI option to find enabled local users does not actually filter on LDAP synchronization.

This uses executeSQLQuery against the CUCM AXL interface and was tested on a 12.5 cluster and was created in Python 3.6.2
