#!/bin/bash



# fresh setup
launchctl unload ~/Library/LaunchAgents/fn.plist
rm -rf ~/Library/LaunchAgents/fn.plist

# load the plist

cp -R fn.plist ~/Library/LaunchAgents/

loggedInUser=$( ls -l /dev/console | awk '{print $3}' )
userID=$( id -u $loggedInUser )
service_name="gui/$userID/fn"

# fyi, removal of new service can be done via:
# sudo launchctl bootout $service_name

# bootstrap (install) as necessary
sudo launchctl print $service_name >> /dev/null 2>&1 || sudo launchctl bootstrap gui/$userID ~/Library/LaunchAgents/fn.plist

sudo launchctl enable $service_name

# kickstart -k will RESTART process, using any updated code
sudo launchctl kickstart -k $service_name
echo "The service \"$service_name\" has been installed and started"