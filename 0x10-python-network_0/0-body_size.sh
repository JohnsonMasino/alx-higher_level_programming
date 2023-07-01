#!/usr/bin/env bash
# A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -I "$1" | grep "Content-Length" | awk '{print $2}'
