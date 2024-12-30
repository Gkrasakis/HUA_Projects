#!/bin/bash
# 4.1 Εμφανίστε τις 10  IPv4 με τις περισσότερες επισκέψεις καθώς και το πλήθος τους
Log_file_ip="/home/f/Shell_scripts/access.log"

#Εξαγωγή διευθύνσεων IPv4 από το αρχείο ταξινόμηση, μέτρηση εμφανίσεων και εμφάνιση των 10 πιο δημοφιλης IP
awk '{print $1}' "$Log_file_ip" | uniq -c | sort -nr | head -n 10 >> IP_list




