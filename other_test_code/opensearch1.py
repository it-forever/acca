from opensearchpy import OpenSearch

host = {'host': '192.168.51.20', 'port': 9200}
auth = ('admin', 'admin')
ca_certs_path = ''


client = OpenSearch(
          hosts=host,
          http_compress=True,
          http_auth=auth,
          use_ssl=True,
          verify_certs=True,
          ssl_assert_hostname=False,
          ssl_show_warn=False
         )

# Create an index with non-default settings.
index_name = 'python-test-index'
index_body = {    
    'settings': {        
        'index': {            
            'number_of_shards': 2        
         }    
    }
}

response = client.indices.create(index_name, body=index_body)
print('\nCreating index:')
print(response)

document = {    
    'title': 'Moneyball',    
    'director': 'Bennett Miller',    
    'year': '2011'
}
id = '1'

response = client.index(    
    index=index_name,
    body=document,
    id=id,
    refresh=True
)

print('\nAdding document:')
print(response)