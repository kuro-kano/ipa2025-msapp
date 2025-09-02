"""Client to connect to routers and fetch interface information."""
import ntc_templates
import os

from netmiko import ConnectHandler
from database import save_interface_status


def get_interfaces(ip, username, password):
    """Connects to a router and retrieves interface information."""
    os.environ["NET_TEXTFSM"] = os.path.join(
        os.path.dirname(ntc_templates.__file__), "templates"
    )

    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password,
    }

    with ConnectHandler(**device) as conn:
        conn.enable()
        result = conn.send_command("show ip interface brief", use_textfsm=True)
        conn.disconnect()

    save_interface_status(ip, result)


if __name__ == "__main__":
    get_interfaces()
