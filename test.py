import requests
import json

def get_device_interface_details(netbox_url, api_token, device_id, headers):
    interfaces_response = requests.get(
        f"{netbox_url}/api/dcim/interfaces/?device_id={device_id}", 
        headers=headers, 
        verify=False
    )
    if interfaces_response.status_code == 200:
        return interfaces_response.json()['results']
    else:
        print(f"Failed to fetch interfaces for device ID {device_id}. Status Code: {interfaces_response.status_code}")
        return []

def get_interfaces_for_site(netbox_url, api_token, site_name):
    headers = {
        'Authorization': f'Token {api_token}',
        'Accept': 'application/json',
    }
    
    site_response = requests.get(
        f"{netbox_url}/api/dcim/sites/?name={site_name}", 
        headers=headers, 
        verify=False
    )
    if site_response.status_code == 200 and site_response.json()['results']:
        site_id = site_response.json()['results'][0]['id']
    else:
        print("Error fetching site or no site found.")
        return []

    devices_response = requests.get(
        f"{netbox_url}/api/dcim/devices/?site_id={site_id}", 
        headers=headers, 
        verify=False
    )
    if devices_response.status_code != 200:
        print("Error fetching devices for site.")
        return []

    all_interfaces = []
    for device in devices_response.json()['results']:
        device_interfaces = get_device_interface_details(netbox_url, api_token, device['id'], headers)
        all_interfaces.extend(device_interfaces)

    return all_interfaces

if __name__ == "__main__":
    netbox_url = 'https://192.168.40.163'
    api_token = 'd9ad849f860d24b653c6a2072fff1afb3d8cf49f'
    site_name = 'TEST'
    
    interfaces = get_interfaces_for_site(netbox_url, api_token, site_name)
    print(json.dumps(interfaces, indent=4))  # Pretty print the JSON
