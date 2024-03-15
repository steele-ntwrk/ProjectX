
import requests

def define_env(env):

    # Define global variables
    env.variables['netbox_url'] = 'http://netbox.com'
    env.variables['netbox_api_token'] = '0123456789abcdef0123456789abcdef01234567'

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
