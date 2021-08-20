#!/bin/bash
# Script that do a POST request and sent two values/variables
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
