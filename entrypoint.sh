#!/bin/bash
set -e
# Start the SSH server in the background
/usr/sbin/sshd

# Execute the original command of your container
# (replace this with the command to build/run your vortex source code)
exec "$@"
