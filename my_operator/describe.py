import os
import json
import argparse

def describe(deployment_name, deployment_spec):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("deployment_name", help="Name of the deployment")
    parser.add_argument(
        "config_json",
        help="Deployment spec file",
        default=os.path.join(os.getcwd(), "deployment_spec.json")
    )
    args = parser.parse_args()
    with open(args.deployment_spec_json, 'r') as file:
        deployment_spec = json.loads(file.read())
    describe(args.deployment_name, deployment_spec)