import requests


def test_server(host_ip, http_port):
    resp = requests.get('http://{0}:{1}'.format(host_ip, http_port), headers={'Host': 'blog.manfred.io'})
    assert resp.status_code == 200


def test_wordpress_url(host_ip, http_port):
    resp = requests.get('http://{0}:{1}'.format(host_ip, http_port), headers={'Host': 'blog.manfred.io'})
    assert 'blog.manfred.io' in resp.text
