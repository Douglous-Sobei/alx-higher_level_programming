#!/bin/bash
# Sends a JSON POST request to a URL with a given JSON file
curl -s -H "Content-Type: appliation/json" -d "$(cat "$2")" "$1"
