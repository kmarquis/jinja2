#! /usr/bin/env/python
import os
import sys
import yaml
from passlib.hash import pbkdf2_sha1, md5_crypt
from huepy import *
import socket
import ipaddress
import netaddr
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import *


def ipad(network):
    net = ipaddress.ip_network(network)
    return net


def ipaddr(network, attr=None):
    netw = netaddr.IPNetwork(network)
    if attr is not None:
        return getattr(netw, attr)
    else:
        return netw


def md5(password):
    md5 = md5_crypt.hash(password)
    return md5


def sha(password):
    pwd = pbkdf2_sha1.hash(password)
    return pwd


def debugging():
    err = "This an error is here"
    return err


def main():
    try:
        data = yaml.safe_load(open(sys.argv[1]))
        template_dir = FileSystemLoader(os.path.dirname(os.path.realpath(__file__)))
        env = Environment(
            loader=template_dir,
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
            newline_sequence='\n',
        )
        env.filters['ipaddr'] = ipaddr
        env.filters['sha'] = sha
        env.filters['md5'] = md5
        env.filters['ipad'] = ipad
        env.filters['debugging'] = debugging
        tpl = env.get_template(sys.argv[2])
        print(tpl.render(data))
    except (TemplateSyntaxError, UndefinedError) as e:
        print('An Error has occured: {0}'.format(e))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(
            info(
                lightred(
                    'Please provide the following: "python3 {0} yaml_file j2_template"'
                    .format(sys.argv[0])
                )
            )
        )
        sys.exit(1)
    main()
