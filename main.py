
import requests

def define_env(env):

    # Define global variables
    env.variables['netbox_url'] = 'https://192.168.40.163'
    env.variables['netbox_api_token'] = 'd9ad849f860d24b653c6a2072fff1afb3d8cf49f'

    # Define a macro to get VLANs for a given site
    @env.macro
    def get_vlans_for_site(site_name):
        headers = {
            'Authorization': f'Token {env.variables["netbox_api_token"]}',
            'Accept': 'application/json',
        }
        sites_response = requests.get(f"{env.variables['netbox_url']}/api/dcim/sites/?name={site_name}", headers=headers, verify=False)
        site_id = sites_response.json()['results'][0]['id']

        vlans_response = requests.get(f"{env.variables['netbox_url']}/api/ipam/vlans/?site_id={site_id}", headers=headers, verify=False)
        return vlans_response.json()['results']

    @env.macro
    def get_device_interface_details(device_id):
        headers = {
            'Authorization': f'Token {env.variables["netbox_api_token"]}',
            'Accept': 'application/json',
        }
        interfaces_response = requests.get(
            f"{env.variables['netbox_url']}/api/dcim/interfaces/?device_id={device_id}", 
            headers=headers, 
            verify=False
        )
        if interfaces_response.status_code == 200:
            return interfaces_response.json()['results']
        else:
            print(f"Failed to fetch interfaces for device ID {device_id}. Status Code: {interfaces_response.status_code}")
            return []

    @env.macro
    def get_interfaces_for_site(site_name):
        headers = {
            'Authorization': f'Token {env.variables["netbox_api_token"]}',
            'Accept': 'application/json',
        }
        
        site_response = requests.get(
            f"{env.variables['netbox_url']}/api/dcim/sites/?name={site_name}", 
            headers=headers, 
            verify=False
        )
        if site_response.status_code == 200 and site_response.json()['results']:
            site_id = site_response.json()['results'][0]['id']
        else:
            print("Error fetching site or no site found.")
            return []

        devices_response = requests.get(
            f"{env.variables['netbox_url']}/api/dcim/devices/?site_id={site_id}", 
            headers=headers, 
            verify=False
        )
        if devices_response.status_code != 200:
            print("Error fetching devices for site.")
            return []

        all_interfaces = []
        for device in devices_response.json()['results']:
            device_interfaces = get_device_interface_details(env.variables.netbox_url, env.variables.netbox_api_token, device['id'], headers)
            all_interfaces.extend(device_interfaces)

        return all_interfaces
