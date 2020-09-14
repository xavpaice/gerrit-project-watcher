# Add watched projects to Gerrit

Quick and dirty script to list out projects in a Gerrit host, and add them to the
 watched projects list.
 
 Usage:
 
 ```
usage: watch_project.py [-h] [--prefix PREFIX] [--url URL] username password

Gerrit API tool

positional arguments:
  username         Gerrit username
  password         HTTP password

optional arguments:
  -h, --help       show this help message and exit
  --prefix PREFIX  Prefix to match when listing projects
  --url URL        URL of Gerrit host

```