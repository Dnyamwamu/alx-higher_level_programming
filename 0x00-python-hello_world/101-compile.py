#!/bin/bash

# Check if PYFILE environment variable is set
if [ -z "$PYFILE" ]; then
    echo "Error: PYFILE environment variable is not set."
    exit 1
fi

# Compile the Python file
python3 -m py_compile "$PYFILE"

# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful: $PYFILEc"
else
    echo "Compilation failed."
fi
