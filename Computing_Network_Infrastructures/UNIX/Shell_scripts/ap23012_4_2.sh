#!/bin/bash

# 4.2 Για τις IP του ερωτήματος 4.1 εμφανίστε τη χώρα καλώντας κάποιο geolocation api.
IP_LIST=("193.198.18.254" "86.242.42.176" "148.81.193.146" "62.1.222.72" "91.208.57.69" "176.58.227.164" "101.191.7.251" "154.16.105.25" "191.96.227.224" "176.58.227.164")

for ip in "${IP_LIST[@]}"; do
    response=$(curl -s "https://ipapi.co/${ip}/json/")

    # Check if the request was successful (HTTP status 200)
    if [[ $(echo "$response" | jq -r '.ip') != "null" ]]; then
        # Print the geolocation information
        country=$(echo "$response" | jq -r '.country_name')
        echo "IP Address: $ip, Country: $country"
    else
        # Print an error message
        echo "Error: Unable to retrieve geolocation information for $ip."
    fi
done
