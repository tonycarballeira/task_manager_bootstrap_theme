class ContactForm < ActiveRecord::Base
	validates :full_name, presence: true
	validates :order_num, presence: true, length: { minimum: 2 }
	validates :comments, presence: true
	validates :email, format: { with: /\A[^@\s]+@([^@\s]+\.)+[^@\s]+\z/, message: "invalid format"}, presence: true
	
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
