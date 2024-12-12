import psycopg2

def update_contact():
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

        # Taking user input for updating a contact
        name = input("Enter the person's name to update: ")
        new_phone_number = input("Enter the new phone number: ")

        # Updating the contact's phone number
        cur.execute('''
            UPDATE phone_book
            SET "PhoneNumber" = %s
            WHERE "PersonName" = %s;
        ''', (new_phone_number, name))

        # Commit the transaction
        conn.commit()

        if cur.rowcount > 0:
            print(f"Contact {name} updated successfully!")
        else:
            print(f"No contact found with the name {name}.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Closing the connection
        cur.close()
        conn.close()

# Example call
update_contact()
