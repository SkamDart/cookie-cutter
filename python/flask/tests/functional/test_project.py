class TestProject:
    def test_health_check(self, client):
        res = client.get('/')
        assert b'Alive' in res.data
