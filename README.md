# Jinja2 Repo
This Repo will be able store for all the Jinja2 templates, that can be referenced to quickly without
having to think about too much :D

To use this Repo you will need to have the following as a miniuium:
 - Python 3.6+
 - pip

## Getting Started
It is recommended to run this within a dev environment, to protect your host system. 

I use `virtualenv` but there plenty of over ways methods can be googled! To install virtualenv and activate your dev environment, please check the docs [here](https://virtualenv.pypa.io/en/stable/installation/)

**Note: I set my environment, so python 3 is default, if is not default then you will need to `python3` and `pip3`**

The necessay modules to run this renderer can be installed by running:
```
(env)$ pip install -r requirements.txt
```
## Renderer 
Once your environment is set, jinja2 template and YMAL data have been created. You will need to run the command below:
```
python3 renderer.py yaml_file j2_template
```

The python script will render YAML data and Jinja2 template and print the output to screen.
```
(env)$ python3 renderer.py  network/junos/vlan/data.yml network/junos/vlan/vlan.j2
set vlans Second_Floor description "VLAN SECOND FLOOR"
set vlans Second_Floor vlan-id 2
set vlans Fourth_Floor description "VLAN FOURTH FLOOR"
set vlans Fourth_Floor vlan-id 4
set vlans Management description "VLAN MANAGEMENT"
set vlans Management vlan-id 10
set vlans First_Floor description "VLAN FIRST FLOOR"
set vlans First_Floor vlan-id 1
set vlans Third_Floor description "VLAN THIRD FLOOR"
set vlans Third_Floor vlan-id 3
```
