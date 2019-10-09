def test_info(client):

    url = "/"
    resp = client.get(url)

    assert resp.status_code == 200

    resp = resp.get_json()
    assert resp == {"version": "0.1.0.dev"}


def test_list_repositories(client):

    url = '/list_repositories'
    resp = client.get(url)

    assert resp.status_code == 200

    resp = resp.get_json()
    assert isinstance(resp, list)
    assert len(resp) == 5
    assert isinstance(resp[0], dict)
