#!/bin/bash

echo "$(sysctl -n sysctl.proc_translated)"

if [[ "$(sysctl -n sysctl.proc_translated)" == "sysctl: unknown oid 'sysctl.proc_translated'" ]]; then
  echo "intel"
else
  echo "M1"
fi
