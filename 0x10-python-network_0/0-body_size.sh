#!/bin/bash
# Take url, send request, display size of body (The size must be displayed in bytes)
curl -s "$1" | wc -c
