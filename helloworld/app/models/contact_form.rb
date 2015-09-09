class ContactForm < ActiveRecord::Base
	attr_accessor :sub

	before_create :sub_assign

	def sub_assign
		if sub == "customer"
			self.subject = 1
		else
			self.subject = 2
		end
	end


end
