# Copyright (c) 2026, kalisakelly and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Trips(Document):
    
    global today
    today = frappe.utils.nowdate()
    
    def validate(self):
        # self.is_active()
        pass
    
    
    def is_active(self):
            
        if self.date_of_the_trip >= today:
            self.active=1
        else:
            self.active=0
        
  
    
