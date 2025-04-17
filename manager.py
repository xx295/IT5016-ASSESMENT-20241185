from datetime import date
from logging import critical


class ticket:
    ticket_counter = 1
    tickets = []
    def __init__(self,date, employee_id , employee_name, issue_date ):
        self.ticket_id = ticket.ticket_counter
        ticket.ticket_counter+=1
        self.date = date
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.issue_desp = issue_desp
        self.status = "in progress"
        self.priority = self.assign_priority()
        self.resolution_message= None
        if "password_reset" in self.issue_desp.lower():
            self.auto_password_reset()
        ticket.tickets.append(self)
    def assign_priority(self)
        issues = ["system outage", "network fsilure"]
        if desp in issues:
            if desp in self.issue_desp.lower():
                return "high"
        return "low"
    def auto_password_reset(self):
        password = self.employee_id[:2] + self.employee_name [:2]
        self.status ="resolved"
        self.resolution_message = f"password reset completed, your new password{new_password}"
    @classmethod
    def ticket_statisitcs(cls):
        total_submitted = len(ticket.tickets)
        resolved_ticket = 0
        total_in_progress =0
        total_closed = 0
        for each_ticket in ticket.tickets:
            if each_ticket.status =="resolved":
                resolved_ticket+=1
            elif each_ticket.status == "in progess":
                total_in_progress+=1
            elif each_ticket.status == "closed":
                total_closed +=1
        print ("------------statistics------------")
        print ("total tickets:", total_submitted)
        print ("total in progress :", total_in_progress)
        print ("total closed:", total_closed)
        print ("total tickets resolved:", total_tickets_resolved)
    @classmethod
    def display_tickets(cls):
        for ticket in  ticket.tickets:
         print ("date:", ticket.date)
         print("ticket id:", ticket.ticket_id)
         print("employee id", ticket.employee_id)
         print ("name:", ticket.employee_name)
         print("issue:",ticket.issue_desp)
         print ("priority:",ticket.priority)
         print ("status:",ticket.status)
         print ("resolution:", ticket.resolution_message)

