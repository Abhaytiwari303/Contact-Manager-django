import streamlit as st
import requests



# Set backend URL
AUTH_URL = "http://localhost:8000/api/token/"  # separate from contacts
BASE_URL = "http://localhost:8000/api/contacts"  # for contacts only

def login_user(username, password):
    response = requests.post(AUTH_URL, data={"username": username, "password": password})
    if response.status_code == 200:
        return response.json().get("access")
    else:
        return None

def get_auth_data():
    from auth.auth_page import auth_page 
# Function to fetch contacts
def fetch_contacts(token):
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(BASE_URL, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch contacts. Check your token or server.")
        return []

# UI starts here
st.title("📇 My Contacts")

# Input field to paste token
token = st.text_input("Enter your JWT Access Token", type="password")

if token:
    contacts = fetch_contacts(token)
    if contacts:
        st.success(f"Found {len(contacts)} contact(s)")
        for contact in contacts:
            with st.expander(contact['name']):
                st.write(f"**Email:** {contact['email']}")
                st.write(f"**Phone:** {contact['phone']}")
                st.write(f"**Address:** {contact['address']}")
    else:
        st.warning("No contacts found.")


def add_contact(token, name, email, phone):
    headers = {"Authorization": f"Bearer {token}"}
    data = {"name": name, "email": email, "phone": phone}
    requests.post(f"{BASE_URL}/", headers=headers, json=data)

def delete_contact(token, contact_id):
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{BASE_URL}/{contact_id}/"  # exactly one slash between parts
    response = requests.delete(url, headers=headers)
    return response

def update_contact(token, contact_id, name, email, phone):
    headers = {"Authorization": f"Bearer {token}"}
    data = {"name": name, "email": email, "phone": phone}
    requests.put(f"{BASE_URL}/{contact_id}/", headers=headers, json=data)

def register_user(username, email, password):
    url = "http://localhost:8000/api/register/"
    payload = {
        "username": username,
        "email": email,
        "password": password
    }
    try:
        response = requests.post(url, json=payload)
        return response
    except Exception as e:
        return None


