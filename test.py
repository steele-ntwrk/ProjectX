import requests

def get_vlans_for_site(site_name, netbox_url, netbox_api_token):
    headers = {
        'Authorization': f'Token {netbox_api_token}',
        'Accept': 'application/json',
    }
    
    sites_response = requests.get(f"{netbox_url}/api/dcim/sites/?name={site_name}", headers=headers, verify=False)
    if sites_response.json()['results']:
        site_id = sites_response.json()['results'][0]['id']
        vlans_response = requests.get(f"{netbox_url}/api/ipam/vlans/?site_id={site_id}", headers=headers, verify=False)
        return vlans_response.json()['results']
    else:
        return []

if __name__ == "__main__":
    netbox_url = 'https://192.168.40.163'
    netbox_api_token = 'd9ad849f860d24b653c6a2072fff1afb3d8cf49f'
    site_name = 'TEST'
    
    vlans = get_vlans_for_site(site_name, netbox_url, netbox_api_token)
    print(vlans)
