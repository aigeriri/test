import psycopg2

def search_contact():
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

        # Taking user input for search criteria
        search_choice = input("Search by (1) Name or (2) Phone Number? Enter 1 or 2: ")

        if search_choice == "1":
            name = input("Enter the name to search: ")
            cur.execute('''
                SELECT "PersonName", "PhoneNumber" FROM phone_book
                WHERE "PersonName" ILIKE %s;
            ''', (f'%{name}%',))  # ILIKE is case-insensitive
        elif search_choice == "2":
            phone_number = input("Enter the phone number to search: ")
            cur.execute('''
                SELECT "PersonName", "PhoneNumber" FROM phone_book
                WHERE "PhoneNumber" = %s;
            ''', (phone_number,))
        else:
            print("Invalid choice. Please select 1 or 2.")
            return

        # Fetching and displaying the results
        result = cur.fetchall()

        if result:
            for contact in result:
                print(f"Name: {contact[0]}, Phone: {contact[1]}")
        else:
            print("No matching contacts found.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Closing the connection
        cur.close()
        conn.close()

# Example call
search_contact()
