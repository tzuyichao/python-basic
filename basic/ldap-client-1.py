import ldap

con = ldap.initialize('ldap://deltaldap.deltaww.com:389', bytes_mode=False)
username = "CN=SERVICE.DMSAUTH,OU=Service,OU=Users,OU=TWTP1,OU=TW,OU=Delta,DC=delta,DC=corp"
password  = "pwd"
con.simple_bind_s(username, password)
print(con)
results = con.search_s(u'OU=Delta,DC=delta,DC=corp', ldap.SCOPE_SUBTREE, u"(cn=TERENCE.CHAO 趙子儀)")
print(results)