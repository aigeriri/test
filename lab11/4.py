import psycopg2

def query_all_contacts():
    try:
        # Establishing the connection
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="aliya1907",
            port="5432"
        )
        cur = conn.cursor()

        # Query to fetch all contacts
        cur.execute('SELECT "PersonName", "PhoneNumber" FROM phone_book;')

        # Fetch all records
        contacts = cur.fetchall()

        # Displaying the contacts
        if contacts:
            print("Contacts in the phonebook:")
            for contact in contacts:
                print(f"Name: {contact[0]}, Phone: {contact[1]}")
        else:
            print("No contacts found in the phonebook.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Closing the connection
        cur.close()
        conn.close()

# Example call
query_all_contacts()
