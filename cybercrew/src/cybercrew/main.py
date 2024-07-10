#!/usr/bin/env python
import sys
from cybercrew.crew import CyberSecCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'Alerts analysis'
    }
    CyberSecCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    try:
        CyberSecCrew().crew().train(n_iterations=int(sys.argv[1]))

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
