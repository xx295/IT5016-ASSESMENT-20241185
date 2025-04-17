# requisitionsystem.py

# Global counter to create unique IDs
requisition_counter = 0

# List to store all requisitions
all_requisitions = []

class RequisitionSystem:
    def __init__(self):
        global requisition_counter
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.requisition_id = 10000 + requisition_counter
        requisition_counter += 1
        self.items = {}
        self.total = 0
        self.status = "Not Submitted"
        self.approval_number = "None"

    def staff_info(self):
        self.date = input("Enter Date: ")
        self.staff_id = input("Enter Staff ID: ")
        self.staff_name = input("Enter Staff Name: ")

    def requisitions_details(self):
        self.items = {}
        self.total = 0
        print("Enter items and their prices (enter 'done' when finished):")
        while True:
            name = input("Item name: ")
            if name.lower() == 'done':
                break
            try:
                cost = float(input(f"Price for {name}: "))
                self.items[name] = cost
                self.total += cost
            except ValueError:
                print("Invalid price. Please enter a number.")
        print("Total Cost: $", self.total)

    def requisition_approval(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_number = self.staff_id + str(self.requisition_id)[-3:]
        else:
            self.status = "Pending"
            self.approval_number = "Not available"
        all_requisitions.append(self)

    def respond_requisition(self):
        if self.status == "Pending":
            response = input(f"Respond to Requisition ID {self.requisition_id} (Approve/Not approved): ").strip().lower()
            if response == "approve":
                self.status = "Approved"
                self.approval_number = self.staff_id + str(self.requisition_id)[-3:] + "-A" # Added '-A' to distinguish manager approval
                print(f"Requisition ID {self.requisition_id} Approved.")
            elif response == "not approved":
                self.status = "Not approved"
                self.approval_number = "Not available"
                print(f"Requisition ID {self.requisition_id} Not approved.")
            else:
                print("Invalid response. Requisition status remains Pending.")
        else:
            print(f"Requisition ID {self.requisition_id} is not pending and cannot be responded to.")

    def display_requisitions(self):
        print("\n--- Requisition Info ---")
        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Name:", self.staff_name)
        print("Items:", self.items)
        print("Total: $", self.total)
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_number)

def requisition_statistic():
    total = len(all_requisitions)
    approved = sum(1 for r in all_requisitions if r.status == "Approved")
    pending = sum(1 for r in all_requisitions if r.status == "Pending")
    not_approved = sum(1 for r in all_requisitions if r.status == "Not approved")
    print("\n--- Requisition Statistics ---")
    print("The total number of requisitions submitted:", total)
    print("The total number of approved requisitions:", approved)
    print("The total number of pending requisitions:", pending)
    print("The total number of not approved requisitions:", not_approved)

# MAIN CODE
print("--- Submitting Requisitions ---")
for i in range(5):
    print(f"\n--- Requisition {i+1} ---")
    r = RequisitionSystem()
    r.staff_info()
    r.requisitions_details()
    r.requisition_approval()

print("\--- Displaying All Requisitions (Initial Status) ---")
for r in all_requisitions:
    r.display_requisitions()

print("\--- Requisition Statistics (Initial) ---")
requisition_statistic()

print("\--- Responding to Pending Requisitions (if any) ---")
for r in all_requisitions:
    if r.status == "Pending":
        r.respond_requisition()

print("\--- Displaying All Requisitions (After Response) ---")
for r in all_requisitions:
    r.display_requisitions()

print("\--- Requisition Statistics (Final) ---")
requisition_statistic()