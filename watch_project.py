#!/usr/bin/env python3
"""Add watched projects to a user in Gerrit."""

import argparse
import json
import requests
from requests.auth import HTTPDigestAuth


def parse_args():
    """Setup args."""
    parser = argparse.ArgumentParser(description="Gerrit API tool")
    parser.add_argument("username", type=str, help="Gerrit username")
    parser.add_argument("password", type=str, help="HTTP password")
    parser.add_argument("--prefix", type=str, default="openstack%2Fcharm-",
                        help="Prefix to match when listing projects")
    parser.add_argument("--url", type=str, default="https://review.opendev.org",
                        help="URL of Gerrit host")
    return parser.parse_args()


def main():
    """List projects and add to watched."""
    args = parse_args()
    list_url = "{}/projects/?p={}".format(args.url, args.prefix)
    # TODO exception handling
    response = requests.get(list_url)
    if response.status_code == 200:
        # TODO this is ugly
        projects_string = " ".join(response.content.decode().split("\n")[1:])
        projects = json.loads(projects_string).keys()
        watch_projects = []
        for project in projects:
            watch_projects.append({"project": project})
        watch_url = "{}/a/accounts/self/watched.projects".format(args.url)
        requests.post(
            watch_url,
            json=watch_projects,
            auth=HTTPDigestAuth(args.username, args.password)
        )


if __name__ == '__main__':
    main()
