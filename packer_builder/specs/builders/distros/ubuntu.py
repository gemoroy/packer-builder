"""packer_builder/specs/builder/distros/ubuntu.py"""


# pylint: disable=line-too-long
def ubuntu_spec(**kwargs):
    """Ubuntu specs."""

    # Setup vars from kwargs
    builder_spec = kwargs['data']['builder_spec']
    distro = kwargs['data']['distro']
    version = kwargs['data']['version']

    bootstrap_cfg = 'preseed.cfg'
    builder_spec.update(
        {
            'boot_command': [
                '<enter><wait><f6><esc>',
                '<bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs>',
                '<bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs>',
                '<bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs>',
                '<bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs>',
                '<bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs>',
                '<bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs>',
                '<bs><bs><bs><bs><bs><bs>',
                '<wait>',
                '/install/vmlinuz',
                '<wait>',
                ' initrd=/install/initrd.gz',
                '<wait>',
                ' auto=true',
                '<wait>',
                ' priority=critical',
                '<wait>',
                ' url=http://{{ .HTTPIP }}:{{ .HTTPPort }}/'f'{distro}-{version}-{bootstrap_cfg}',  # noqa: E501
                '<wait>',
                '<enter>'
            ],
            'boot_wait': '30s',
            'shutdown_command': 'sudo /sbin/halt -h -p'
        }
    )

    return bootstrap_cfg, builder_spec
