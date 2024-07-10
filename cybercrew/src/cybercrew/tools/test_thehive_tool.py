from thehive_tool import TheHiveAlertsTool
import json

def test_thehive_alerts_tool():
    tool = TheHiveAlertsTool()
    result = tool._run()
    
    # Parse the JSON string result
    alerts = json.loads(result)
    
    # Check if we got a list of alerts
    assert isinstance(alerts, list), "Result should be a list of alerts"
    
    # Print the number of alerts retrieved
    print(f"Retrieved {len(alerts)} alerts")
    
    # Print details of the first alert (if any)
    if alerts:
        first_alert = alerts[0]
        print("\nFirst alert details:")
        print(f"Title: {first_alert.get('title', 'N/A')}")
        print(f"Description: {first_alert.get('description', 'N/A')}")
        print(f"Severity: {first_alert.get('severity', 'N/A')}")
        print(f"Status: {first_alert.get('status', 'N/A')}")
    else:
        print("No alerts retrieved")

if __name__ == "__main__":
    test_thehive_alerts_tool()