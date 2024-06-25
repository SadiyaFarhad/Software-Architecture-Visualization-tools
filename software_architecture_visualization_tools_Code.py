
# software_crud.py
from software_db import get_software_database

# Function to display menu and get user choice
def display_menu():
    
    tools()
    print("\nSoftware Tools CRUD Operations Menu:")
    print("1. Create Tool")
    print("2. Read Tools")
    print("3. Update Tool")
    print("4. Delete Tool")
    print("5. Print Bill")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    return choice
def tools():
    database = get_software_database()
    print("\nSoftware Tools Details!!:")
    for key, tool in database.items():
        print(f"{key}. {tool['name']}, ${tool['price']}")
# Function to create a new software tool
def create_tool():
    name = input("Enter tool name: ")
    property_value = input("Enter tool property: ")
    price = int(input("Enter tool price: "))
    
    # Get the current software database
    database = get_software_database()
    
    # Find the next available key
    new_key = max(database.keys()) + 1
    
    # Add the new tool to the database
    database[new_key] = {'name': name, 'property': property_value, 'price': price}
    print(f"Tool '{name}' added successfully!")

# Function to read all software tools
def read_tools():
    database = get_software_database()
    print("\nSoftware Tools Database:")
    for key, tool in database.items():
        print("------------------------------------------------------------------------------------")
        print(f"{key}. {tool['name']} - Property: {tool['property']}, Price: ${tool['price']}")
        print("------------------------------------------------------------------------------------")
      
# Function to update an existing software tool
def update_tool():
    read_tools()
    tool_id = int(input("Enter the tool ID to update: "))
    
    # Check if the tool ID exists
    if tool_id in get_software_database():
        name = input("Enter new tool name (press Enter to keep the same): ")
        property_value = input("Enter new tool property (press Enter to keep the same): ")
        price = input("Enter new tool price(press Enter to keep the same): ")
        
        # Get the current software database
        database = get_software_database()
        
        # Update the tool information
        tool = database[tool_id]
        tool['name'] = name if name else tool['name']
        tool['property'] = property_value if property_value else tool['property']
        tool['price'] = price if price else tool['price']
        
        print(f"Tool ID {tool_id} updated successfully!")
    else:
        print("Tool ID not found!")

# Function to delete a software tool
def delete_tool():
    read_tools()
    tool_id = int(input("Enter the tool ID to delete: "))
    
    # Check if the tool ID exists
    if tool_id in get_software_database():
        # Get the current software database
        database = get_software_database()
        
        # Delete the tool
        del database[tool_id]
        
        print(f"Tool ID {tool_id} deleted successfully!")
    else:
        print("Tool ID not found!")

# Function to print a bill for selected software tools
def print_bill():
    read_tools()
    tool_ids = input("Enter the tool IDs for the bill (comma-separated): ").split(',')
    
    # Get the current software database
    database = get_software_database()
    ame=input("enter client name:")
    mail=input("enter your email id  :")
    total_price = 0
  
    print("\nBill:")
    for tool_id in tool_ids:
        tool_id = int(tool_id)
        if tool_id in database:
            tool = database[tool_id]
            print("***************************************************************")
            print("PURCHASED TOOL IS :")
            print("Client Name:",ame)
            print(f"TOOL NAME: {tool['name']} - ${tool['price']:.2f}")
            print("Mail ID :",mail)
            total_price += tool['price']
        else:
            print("***************************************************************")
            print(f"Tool ID {tool_id} not found!")
     
    print("\nTotal Price: ${:.2f}".format(total_price))
    print("***************************************************************")
# Main function to run the CRUD operations
def main():
    while True:
        choice = display_menu()

        if choice == '1':
            create_tool()
        elif choice == '2':
            read_tools()
        elif choice == '3':
            update_tool()
        elif choice == '4':
            delete_tool()
        elif choice == '5':
            print_bill()
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
