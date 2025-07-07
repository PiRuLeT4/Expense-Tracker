import argparse
from json_handler import write_json, read_json, check_json, create_json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument("--description", help="Add a description to the expense", metavar="")
    parser.add_argument("--amount", help="Add an amount to the expense", metavar="")
    parser.add_argument("--id", help="id of the expense", metavar="")
    parser.add_argument("--date", help="date of the expense", metavar="")



    args = parser.parse_args()


    def add_expense(desc, amount):       
        data = read_json()

        #.. create a unique ID for the expense
        id = len(data) + 1
        if data:
            for exp in data:
                if exp["ID"] == id:
                    id += 1

        #.. expense to add
        expense = {
        "descr": desc,
        "amount": amount,
        "ID": id,
        "Date": None,
    }


        data.append(expense)
        print(f"Expend added successfully (ID: {id})")
        write_json(data)

    def delete_expense(id):
        data = read_json()

        for exp in data:
            if exp["ID"] == id:
                data.remove(exp)
                print("Expense deleted successfully")
                write_json(data)
            else:
                print(f"No expense found with ID {id}. List expenses so you can check the Ids")


    def update_expense(id, new_descr=None, new_amount=None, new_date=None):
        data = read_json()
        for exp in data:
            if exp["ID"] == id:
                if new_descr != None:
                    exp["descr"] = new_descr
                if new_amount != None:
                    exp["amount"] = new_amount
                if new_date != None:
                    exp["Date"] = new_date
                write_json(data)
                print(f"Expense with ID {id} updated successfully")
                return
        print(f"No expense found with ID {id}")
        


    
    def list_expenses():
        data = read_json()
        #.. header of the list of expenses
        print(f"{"ID":<5} {"Date":<12} {"Description":<18} {"Amount":<8}")

        #.. to align items we use format with a fixed width
        for exp in data:
            id_str = str(exp.get("ID", ""))
            date_str = str(exp.get("Date", "") if exp.get("Date") is not None else "--")
            description = str(exp.get("descr", ""))
            amount_str = f"${str(exp.get("amount", "") if exp.get("amount") is not None else "--")}"

            #.. here if the descr is too large we cut it and add "..."
            if len(description) > 12:
                description = description[:12] + "..."
            print(f"{id_str:<5} {date_str:<12} {description:<18} {amount_str:<8}")

    def sum_expenses():
        data = read_json()
        if data == []:
            print("No expenses to sum")
            return
        result = 0
        for exp in data:
            result += float(exp["amount"])
        print(f"Total expenses: ${result}")


    #.. RUN CODE ..#

    def run_code():

        #.. create the json file where we'll store the expenses
        if not check_json("data.json"):
            create_json()
        
        command = args.command

        if command.lower() == "add":
            description = args.description
            amount = args.amount
            date = args.date
            add_expense(description, amount)
        elif command.lower() == "delete":
            id = int(args.id)
            delete_expense(id)
        elif command.lower() == "list":
            list_expenses()
        elif command.lower() == "summary":
            sum_expenses()
        elif command.lower() == "update":
            #.. user must type the id of the expense he wants to update
            id = int(args.id)
            #.. user must indicate at least 1 of the parameters to update. Could be just 1 to update
            description = args.description
            amount = args.amount
            date = args.date

            update_expense(id, new_descr=description, new_amount=amount, new_date=date)

    

    run_code()


    

if __name__ == "__main__":
    main()