#!/bin/bash

# File to store contacts
contacts_file="contacts_list.txt"

# Check if the contacts file exists, if not create it
if [ ! -e "$contacts_file" ]; then
    touch "$contacts_file"
fi

# **********************************************************************************************************************************************
#Αφού έχει γίνει το αρχείο για την αποθήκευση και διαχείριση των επαφών τωρα θα πρέπει να φτιάξω τις μεταβλητές που αντιστοιχούν στο μενού:
                                          # *****MAIN MENU*************
                                            #1.Insert Contact
                                            #2.Delete Contact
                                            #3.Modify Contact
                                            #4.Search Contact
                                            #5.Sort Contacts by LastName
                                            #6.Sort Contacts by FirstName
                                            #7.Quit
                                          #****************************
                                            #What you want me to do?
                                            #Please make your choice: 
# **********************************************************************************************************************************************

# Μεταβλητή για την εισαγωγή νέων επαφών (Insert Contact)
Insert_Contact() 
{
    while true; do  
        read -e -p "Enter First Name: " first_name

        #Επικύρωση ονόματος- να επιτρέπονται μόνο γράμματα
        if [[ ! $first_name =~ ^[A-Za-z]+$ ]]; then
        echo "Invalid First Name. Please enter letters only."
        read -p "Press Enter to continue..."
        else
            break  
        fi
    done

    while true; do
    read -e -p "Enter Last Name: " last_name

        # Επικύρωση Επιθέτου για να επιτρέπονται μόνο γράμματα 
        if [[ ! $last_name =~ ^[A-Za-z]+$ ]]; then
            echo "Invalid Last Name. Please enter letters only."
            read -p "Press Enter to continue..."
        else
            break  
        fi
    done

    while true; do
        read -e -p "Enter Phone Number: " phone_number1

        # Επικύρωση 1ου αριθμού τηλεφώνου- να επιτρέπονται μόνο αριθμοί = 10
        if [[ ! $phone_number1 =~ ^[0-9]+$ || ${#phone_number1} -ne 10 ]]; then
            echo "Invalid Phone Number. Please enter numbers only, and equal to 10 digits."
        else
            break  
        fi
    done

    while true; do
        read -e -p "Enter home telephone number: " phone_number2

        # Επικύρωση 2ου αριθμού τηλεφώνου- να επιτρέπονται μόνο αριθμοί = 10
        if [[ ! $phone_number2 =~ ^[0-9]+$ || ${#phone_number2} -ne 10 ]]; then
        echo "Invalid Phone Number. Please enter numbers only, and equal to 10 digits."
        read -p "Press Enter to continue..."
        else
            break  
        fi
    done

    echo "${first_name} ${last_name}: ${phone_number1} ${phone_number2}" >> "$contacts_file"
    echo "Contact inserted successfully!"
    read -p "Press Enter to continue..."
}

# Μεταβλητή για τη διαγραφή επαφών (Delete Contact)
Delete_Contact() 
{
    read -e -p "Enter First Name of the contact to delete: " first_name
    grep -i -v "^${first_name}" "$contacts_file" > "temp_file"
    mv "temp_file" "$contacts_file"
    echo "Contact deleted successfully!"
    read -p "Press Enter to continue..."
}

# Μεταβλητή για την τροποποίηση των επαφών (Modify Contact)
Modify_Contact() 
{
    read -e -p "Enter First Name of the contact to modify: " first_name
    read -e -p "Enter new Phone Number: " new_phone_number
    sed -i "s/^${first_name}.*/${first_name}: ${new_phone_number}/i" "$contacts_file"
    echo "Contact modified successfully!"
    read -p "Press Enter to continue..."
}

# Μεταβλητή για την αναζήτηση τω επαφών (Search Contact)
Search_Contact() 
{
    read -e -p "Enter First Name to search: " first_name
    grep -i "^${first_name}" "$contacts_file" || echo "Contact not found"
    read -p "Press Enter to continue..."
}

# Μεταβλητή για την κατανομή της λίστας επαφών βάσει Επθέτου (Sort by L_name Contact)
Sort_By_LastName() 
{
    sort -k 2 "$contacts_file" > "temp_file"
    mv "temp_file" "$contacts_file"
    echo "Contacts sorted by Last Name!"
    read -p "Press Enter to continue..."
   
}
# Μεταβλητή για την κατανομή της λίστας επαφών βάσει Ονόματος (Sort by F_name Contact)
Sort_By_FirstName() 
{
    sort -k 1 "$contacts_file" > "temp_file"
    mv "temp_file" "$contacts_file"
    echo "Contacts sorted by First Name!"
    read -p "Press Enter to continue..."
}


while [ true ]
do
  echo "  "
  echo "*****MAIN MENU*************"
  echo " "
  echo "1.Insert Contact"
  echo "2.Delete Contact"
  echo "3.Modify Contact"
  echo "4.Search Contact"
  echo "5.Sort Contacts by LastName"
  echo "6.Sort Contacts by FirstName"
  echo "7.Quit"
  echo " "
  echo "****************************"
  echo "What you want me to do?"
  echo " "
  read -e -p "Please make your choice: " selection

  case ${selection} in 
        1) Insert_Contact;;
        2) Delete_Contact;;
        3) Modify_Contact;;
        4) Search_Contact;;
        5) Sort_By_LastName;;
        6) Sort_By_FirstName;;
        7) echo "Goodbye..."; exit 0;;
        *) echo "Wrong Choice!";;
    esac
done

