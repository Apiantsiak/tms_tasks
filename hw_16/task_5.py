# Ex.4
# Реализовать дата-класс HostSettings.
# Должен иметь свойства ip_addr, port, hostname, username, password, auth_type


from pydantic import BaseModel


class HostSettings(BaseModel):
    ip_addr: str
    port: str
    hostname: str
    password: str
    auth_type: str


config_1 = HostSettings(ip_addr='127.0.0.1', port="5000", hostname='localhost', password='123', auth_type='root')
config_2 = HostSettings(ip_addr='127.0.0.1', port="5000", hostname='localhost', password='123', auth_type='root')


def test_equal_but_not_same_obj():
    assert config_1 == config_2
    assert config_1 is not config_2
