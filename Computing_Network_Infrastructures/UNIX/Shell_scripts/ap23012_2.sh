#!/bin/bash

# Μετατροπή σε τοπική ώρα 
TZ='Europe/Athens'; export TZ >> ~/.profile
date

# Θα φτιάξω μια Function για την μετατροπή της τοπικής ώρας στην επιλεγμένη χώρα.
time_converter() {
    
    # Βάζω τιμές στα δύο ορίσματα τις παραμέτρους $1, $2

    local_time="$1"
    target_country="$2"

    # Χρήση της μεταβλητής TZ για να ορίσω την μετατροπή.

    target_time=$(
        
        TZ="$target_country" 

        date -d "$local_time" "+%d-%m-%Y %H:%M:%S %Z" 
    )

    if [ $# -eq 2 ]; 
    
        then
        echo " Η Ωρα σε $target_country είναι: $target_time"
        else
        echo "Μη έγκυρη εισαγωγή!. Εισάγετε τοπική ώρα σε μορφή 'DD-MM-YYYY HH:MM:SS'."
    fi
}

# Στοιχεία που θα πρέπει να εισάγει ο χρήστης 
echo  -n "Παρακαλώ εισάγετε Ώρα Ελλάδος (DD-MM-YYYY HH:MM:SS): " 
read local_time_input

echo -n "Παρακαλώ εισαγετε τη χώρα επιλογής (π.χ., Europe/Paris): " 
read target_country_input

time_converter "$local_time_input" "$target_country_input"
