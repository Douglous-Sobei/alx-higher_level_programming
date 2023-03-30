#!/bin/bash

# Get URL from command line argument
url="$1"

# Send GET request with curl, only display body for 200 status code
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

if [ $response -eq 200 ]; then
  curl -s "$url"
else
  echo "Error: $response status code returned"
fi
