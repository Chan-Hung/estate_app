# Copyright (c) 2022, Hung DChan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Property(Document):
	#validate
	# def validate(self):
	# 	if(self.property_type == "Flat"):
	# 		for amenity in self.amenities:
	# 			if(amenity.amenity == "Outdoor Kitchen"):
	# 				frappe.throw((f'Property of type <b>Flat</b> should not have amenity {amenity.amenity}'))
#hello
	def after_insert(self):
		frappe.msgprint((f'Document {self.name} inserted successfullye'))