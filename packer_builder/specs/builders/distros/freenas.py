"""packer_builder/specs/builder/distros/freenas.py"""


# pylint: disable=line-too-long
def freenas_spec(self):
    """FreeNAS specs."""
    self.bootstrap_cfg = None
    self.builder_spec.update(
        {
            'boot_command': [
                '<enter>',
                '<wait30>1<enter>',
                'y',
                '<wait5><spacebar>o<enter>',
                '<enter>',
                '{{ user `password` }}<tab>{{ user `password` }}<tab><enter>',
                '<enter>',
                '<wait60><wait60><wait60>',
                '<enter>',
                '3<enter>',
                '<wait60><wait60><wait60><wait60><wait60>',
                '9<enter>',
                'curl -X PUT -u {{ user `username` }}:{{ user `password` }} -H \'Content-Type: application/json\' -d \'{\"ssh_rootlogin\": true}\' http://localhost/api/v1.0/services/ssh/<enter>',  # noqa: E501
                'curl -X PUT -u {{ user `username` }}:{{ user `password` }} -H \'Content-Type: application/json\' -d \'{\"srv_enable\": true}\' http://localhost/api/v1.0/services/services/ssh/<enter>'  # noqa: E501
            ],
            'boot_wait': '30s',
            'shutdown_command': 'shutdown -p now',
        }
    )
