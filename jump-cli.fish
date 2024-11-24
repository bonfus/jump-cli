#!/bin/fish
# Usage example: ./jump-cli.fish ssh certificate "your-user" --force --insecure --no-password --no-agent --provisioner your-prov ~./ssh/your-shiny-new-keys


test -f config/info.cfg || { echo "No config! Run ./gen_config.py first" ; exit -1 }

read -s -P 'Config pass: ' JCLI_CONFIG_PASS

while true

PATH=$(pwd):$PATH JCLI_CONFIG_PASS=$JCLI_CONFIG_PASS step-cli $argv

sleep 2h
end
