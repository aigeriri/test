import psycopg2

def delete_contact():
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

        # Taking user input for deleting a contact
        name = input("Enter the person's name to delete: ")

        # Deleting the contact from the table
        cur.execute('''
            DELETE FROM phone_book
            WHERE "PersonName" = %s;
        ''', (name,))

        # Commit the transaction
        conn.commit()

        if cur.rowcount > 0:
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"No contact found with the name {name}.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Closing the connection
        cur.close()
        conn.close()

# Example call
delete_contact()
