import requests

# Set the base URL for the JSONPlaceholder API
base_url = "https://jsonplaceholder.typicode.com"

def get_employee_data(employee_id):
    # Make a GET request to retrieve employee data
    response = requests.get(f"{base_url}/employees/{employee_id}")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        employee_data = response.json()
        print(employee_data)
        print(f"User Data for User ID {employee_id}:")
        print(f"Name: {employee_data['name']}")
        print(f"Email: {employee_data['email']}")
        print(f"Phone: {employee_data['phone']}")
    else:
        print(f"Failed to retrieve employee data. Status code: {response.status_code}")

def get_posts_by_employee(employee_id):
    # Make a GET request to retrieve posts by a specific employee
    response = requests.get(f"{base_url}/employees/{employee_id}/posts")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        posts = response.json()
        print(f"Posts by User ID {employee_id}:")
        for post in posts:
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}")
            print("------")
    else:
        print(f"Failed to retrieve posts. Status code: {response.status_code}")

if __name__ == "__main__":
    # Example: Get user data for employee with ID 1
    get_employee_data(1)

    # Example: Get posts by employee with ID 1
    get_posts_by_employee(1)
