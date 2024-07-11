#!/usr/bin/env python
import sys
import json
import glob
import os
from cybercrew.tools.thehive_alerts_tools_save import thehive_alerts
from cybercrew.crew import CyberSecCrew


def run():
    # Call the thehive_alerts function to retrieve and save alerts
    # thehive_alerts()

    # Find the most recent alerts file
    # list_of_files = glob.glob('projects/crewai_cybersoc/cybercrew/src/cybercrew/tools/thehive_alerts_20240711_085957.json')
    # if not list_of_files:
    #     raise FileNotFoundError("No alerts file found. Make sure thehive_alerts() function is saving the file correctly.")
    
    # latest_file = max(list_of_files, key=os.path.getctime)

    # Read the contents of the latest file
    with open('/Users/kapenge/Laboratories/_ai/projects/crewai_cybersoc/cybercrew/src/cybercrew/tools/thehive_alerts_20240711_101312.json', 'r') as file:
        file_contents = json.load(file)

    # Define the chunk size (adjust as needed)
    chunk_size = 100

    # Process alerts in chunks
    for i in range(0, len(file_contents), chunk_size):
        chunk = file_contents[i:i + chunk_size]
        
        # Convert the chunk back to a JSON string
        chunk_json = json.dumps(chunk)

        # Execute the crew with the chunk as input
        inputs = {
            'topic': 'Alerts analysis',
            'alerts': chunk_json,
            'chunk_number': i // chunk_size + 1,
            'total_chunks': (len(file_contents) + chunk_size - 1) // chunk_size
        }
        
        # Kick off the CyberSecCrew with the inputs
        CyberSecCrew().crew().kickoff(inputs=inputs)

        print(f"Analysis completed for chunk {inputs['chunk_number']} of {inputs['total_chunks']}")

   # print(f"All chunks processed from {latest_file}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    try:
        CyberSecCrew().crew().train(n_iterations=int(sys.argv[1]))

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
