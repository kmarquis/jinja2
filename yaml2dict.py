import yaml
import os
import sys
import json

"""
Prints out a YAML file as pretty print json output

YAML
---
firewall:
  family:
    - name: inet
      acl:
        - name: web
          term:
            - name: web
              dest:
                - webservers
              protocol:
                - tcp
              port:
                - 80
                - 443
              action: accept

$ python yaml2dict.py test.yml
{
    "firewall": {
        "family": [
            {
                "name": "inet",
                "acl": [
                    {
                        "name": "web",
                        "term": [
                            {
                                "name": "web",
                                "dest": [
                                    "webservers"
                                ],
                                "protocol": [
                                    "tcp"
                                ],
                                "port": [
                                    80,
                                    443
                                ],
                                "action": "accept"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
"""

yaml_file = sys.argv[1]

with open(yaml_file, "r") as file:
    try:
        parsed_yaml = yaml.safe_load(file)
        print(json.dumps(parsed_yaml, indent=4))
    except yaml.YAMLError as exc:
        print(exc)
