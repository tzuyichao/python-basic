from ldap3 import Server, Connection, ALL

server = Server('deltaldap.deltaww.com', get_info=ALL)
conn = Connection(server, 'CN=SERVICE.DMSAUTH,OU=Service,OU=Users,OU=TWTP1,OU=TW,OU=Delta,DC=delta,DC=corp', 'pwd', auto_bind=True)
conn.search('OU=Delta,DC=delta,DC=corp', '(cn=TERENCE.CHAO 趙子儀)')
print(conn.entries)