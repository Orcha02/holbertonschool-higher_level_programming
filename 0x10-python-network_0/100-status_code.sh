#!/bin/bash
# Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response
curl -sI "$1" -w "%{http_code}" -o /dev/null

# -w-> What to output after completion
# "%{http_code}"-> Prints the HTTP_CODE to stdout
# -o-> Write output to <file> instead of stdout
# /dev/null-> Instead of reading, it’s used to write. Whatever you write to
#             /dev/null will be discarded, forgotten into the void.
