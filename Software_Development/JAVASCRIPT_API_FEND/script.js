// REFS **  https://developer.mozilla.org/en-US/  **


// GET request function
function appendData() {
    // Create a XMLHttpRequest object
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {

            //if successful, request parse to JSON
            let response = JSON.parse(xhr.responseText);

            // Inserting data to tables (populates)
            let table = document.getElementById("data-table").getElementsByTagName('tbody')[0];
            let dropdown = document.getElementById("data-dropdown");
            table.innerHTML = "";
            dropdown.innerHTML = '<option value="">Select ID</option>';

            // This part is for Display the results containing the table and the dropdown menu
            response.products.forEach(product => {
                let row = table.insertRow();
                row.insertCell(0).textContent = product.id;
                row.insertCell(1).textContent = product.title;
                row.insertCell(2).textContent = product.description;
                row.insertCell(3).textContent = product.price;

                let option = document.createElement("option");
                option.value = product.id;
                option.textContent = product.id;
                dropdown.appendChild(option);
            });
                                                                                            // GIA NA DW TI ERXETAI STO CONSOLE
                                                                                            console.log(xhr.status, response);

            document.getElementById("results").style.display = "block";
        } else if (xhr.readyState === 4) {
            console.error("Error: " + xhr.status);
        }
    };
    xhr.open("GET", "https://dummyjson.com/products", true);
    xhr.send();
}

/* Summer holiday Easter egg
 Code responsibly! Your bugs are not invited to my beach party!
🌞🏖️🐛 */


// POST request function

function postData(event) {

    // Prevent the default form submission behavior
    event.preventDefault();

    // Read the values
    const title = document.getElementById("title").value;
    const company = document.getElementById("company").value;

    // ! Checks if fields are empty and alerts the user if they are. This is for not inserting empty entries
    if (title.trim() === "" || company.trim() === "") {
        alert("Both fields are required.");
        return;
    }

    const data = {
        title: title,
        company: company
    };


    // Create a XMLHttpRequest object
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {


        // So now the msg status must be 201!
        if (xhr.readyState === 4 && xhr.status === 201) {
            let response1 = JSON.parse(xhr.responseText);
            alert("Data posted successfully: " + JSON.stringify(response1));
        } else if (xhr.readyState === 4) {
            console.error("Error: " + xhr.status);
        }
    };

                                                                                            // GIA NA DW TI ERXETAI STO CONSOLE
                                                                                            console.log(data);


    // Sends a POST request
    xhr.open("POST", "https://dummyjson.com/products/add", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify(data));
}




// Function to handle dropdown change

function handleDropdownChange() {

    const dropdown = document.getElementById("data-dropdown");
    const selectedId = dropdown.value;

    if (selectedId) {
        // Create a XMLHttpRequest object
        const xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {

            //Defines a callback function to handle state changes.
            if (xhr.readyState === 4 && xhr.status === 200) {
                let product = JSON.parse(xhr.responseText);
                const modalContent = document.getElementById("modal-content");
                modalContent.innerHTML = `
                    <p>ID: ${product.id}</p>
                    <p>Title: ${product.title}</p>
                    <p>Description: ${product.description}</p>
                    <p>Price: ${product.price}</p>
                `;
                document.getElementById("modal").style.display = "block";
            }
        };

        //Sends a GET request to fetch details of the selected product.
        xhr.open("GET", `https://dummyjson.com/products/${selectedId}`, true);
        xhr.send();
    }
}

// Close modal, this is the modal that has the product details and need to be closed when the close button pressed
function closeModal() {
    document.getElementById("modal").style.display = "none";
}

// Event listeners
document.addEventListener("DOMContentLoaded", () => {
    const fetchDataButton = document.getElementById("fetchData");
    const submitDataButton = document.getElementById("submitData");
    const dropdown = document.getElementById("data-dropdown");
    const modalClose = document.getElementById("modal-close");

    if (fetchDataButton) {fetchDataButton.addEventListener("click", appendData);}

    if (submitDataButton) {submitDataButton.addEventListener("click", postData);}

    if (dropdown) {dropdown.addEventListener("change", handleDropdownChange);}

    if (modalClose) {modalClose.addEventListener("click", closeModal);}

});

