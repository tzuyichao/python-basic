import ldap

con = ldap.initialize('ldap://deltaldap.deltaww.com:389', bytes_mode=False)
username = "CN=SERVICE.DMSAUTH,OU=Service,OU=Users,OU=TWTP1,OU=TW,OU=Delta,DC=delta,DC=corp"
password  = "pwd"
con.simple_bind_s(username, password)
print(con)
# size limit exceeding
results = con.search_s(u'OU=Delta,DC=delta,DC=corp', ldap.SCOPE_SUBTREE, u"(objectCategory=CN=Person,CN=Schema,CN=Configuration,DC=delta,DC=corp)")
print(results)