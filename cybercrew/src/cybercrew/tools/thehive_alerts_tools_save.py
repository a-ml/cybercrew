import json
import requests
import logging
import configparser
from datetime import datetime

def thehive_alerts():
    """
    This tool is an API call, useful to retrieve alerts from TheHive Platform and save them to a JSON file.
    You DON'T need to provide the URL as it is already added in the tool. Just call this function.
    """
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Read TheHive instance URL from the config file
    thehive_url = config['DEFAULT']['thehive_url']
    # Read TheHive API key from the config file
    thehive_api_key = config['DEFAULT']['thehive_api_key']

    severities = [2, 3, 4]
    alerts = []

    for severity in severities:
        if severity not in [1, 2, 3, 4]:
            raise ValueError("Invalid severity level. Allowed values: 1 (low), 2 (medium), 3 (high), 4 (critical)")

        query_params = {
            "query": [
                {"_name": "listAlert"},
                {"_name": "filter", "_field": "severity", "_value": severity},
                {"_name": "filter", "_field": "status", "_value": "New"},  # Filter for "New" status
                {"_name": "sort", "_fields": [{"date": "desc"}]},
                {"_name": "page", "from": 0, "to": 15, "extraData": ["importDate", "caseNumber"]}
            ]
        }

        try:
            response = requests.post(
                f'{thehive_url}/v1/query?name=alerts',
                json=query_params,
                headers={'Authorization': f'Bearer {thehive_api_key}'}
            )
            response.raise_for_status()  # Raise for non-200 status codes
            alerts += response.json()  # Convert response to JSON and append to the list
        except requests.exceptions.HTTPError as err:
            logging.error(f"HTTP Error: {err}")
        except requests.exceptions.Timeout as err:
            logging.error(f"Request timed out: {err}")
        except requests.exceptions.RequestException as err:
            logging.error(f"General TheHive request error: {err}")

    # Generate a timestamp for the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"thehive_alerts_{timestamp}.json"

    # Save alerts to a JSON file
    with open(filename, 'w') as file:
        json.dump(alerts, file, indent=4)

    print(f"Alerts saved to {filename}")

    return json.dumps(alerts)

# If you want to run this function directly
if __name__ == "__main__":
    thehive_alerts()
