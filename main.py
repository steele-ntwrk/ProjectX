
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
        sites_response = requests.get(f"{env.variables['netbox_url']}/api/dcim/sites/?name={site_name}", headers=headers)
        site_id = sites_response.json()['results'][0]['id']

        vlans_response = requests.get(f"{env.variables['netbox_url']}/api/ipam/vlans/?site_id={site_id}", headers=headers)
        return vlans_response.json()['results']
                # Placeholder data
        #return [
        #    {'id': 1, 'name': 'VLAN 1', 'description': 'Example VLAN 1'},
        #    {'id': 2, 'name': 'VLAN 2', 'description': 'Example VLAN 2'}
        #]
