# Copyright (c) 2026, kalisakelly and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class BookingaTrip(Document):
    
    def validate(self):
        self.add_booked_trip()
        
    def on_cancel(self):
        self.remove_booked_trip()



    def  add_booked_trip(self):
        trip = frappe.get_doc("Trips", self.trip)
        number_of_people = trip.number_of_people
        places_available = trip.number_of_booked_places
  
        if number_of_people > places_available:
            trip.number_of_booked_places = places_available + 1
            trip.save()
        else:
            frappe.throw("Not enough places available for this trip.")
   
   
    def remove_booked_trip(self):
        trip = frappe.get_doc("Trips", self.trip)
        places_available = trip.number_of_booked_places
        
        if places_available > 0:
            trip.number_of_booked_places = places_available - 1
            trip.save()
        else:
            frappe.throw("No booked places to remove for this trip.")	

        
            
     
     