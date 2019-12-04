from ldap3 import Server, Connection, ALL

server = Server('deltaldap.deltaww.com', get_info=ALL)
conn = Connection(server, 'CN=SERVICE.DMSAUTH,OU=Service,OU=Users,OU=TWTP1,OU=TW,OU=Delta,DC=delta,DC=corp', 'pwd', auto_bind=True)
entries = conn.extend.standard.paged_search('OU=Delta,DC=delta,DC=corp', '(objectCategory=CN=Person,CN=Schema,CN=Configuration,DC=delta,DC=corp)', attributes=['cn'], paged_size=1000)
size = 0
f = open("account.txt", "w", encoding='UTF-8')
for entry in entries:
    size+=1
    print(entry['attributes']['cn'])
    f.write("%s\n" % (entry['attributes']['cn']))
print(size)
f.close()