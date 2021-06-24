import pygit2


class CustomOdbBackend(pygit2.OdbBackend):
    def __init__(self):
        super().__init__()
        self.objects = {}

    def write_cb(self, oid, data, otype):
        print(f'write {type(oid)}:{oid} {data} {otype}')
        oid = str(oid)
        self.objects[oid] = {'data': data, 'type': otype}
        return True

    def read_cb(self, oid):
        print(f'read {type(oid)}:{oid}')
        oid = str(oid)
        return self.objects[oid]['type'], self.objects[oid]['data']

    def read_prefix_cb(self, oid: str):
        print(f'read_prefix {type(oid)}:{oid}')
        obj = self.objects[oid]
        return obj['type'], obj['data'], oid

    def read_header_cb(self, oid):
        print(f'read_header {type(oid)}:{oid}')
        obj = self.objects[oid]
        return obj['type'], len(obj['data'])

    def exists_cb(self, oid):
        print(f'exists {type(oid)}:{oid}')
        oid = str(oid)
        return oid in self.objects

    def exists_prefix_cb(self, oid):
        print(f'exists_prefix {type(oid)}:{oid}')
        return oid

    def refresh_cb(self):
        print(f'refresh')
        return


repo = pygit2.Repository()
odb = pygit2.Odb()
odb.add_backend(CustomOdbBackend(), 1)
repo.set_odb(odb)

print('Writing blob')
test_blob_id = repo.create_blob(b'Hello, World!\n')
print(f'Got hash {type(test_blob_id)}:{test_blob_id}')
print('=====')
print('Read-back', repo[test_blob_id].data)
