class ContactForm < ActiveRecord::Base
	belongs_to :subject

	validates :full_name, presence: true
	validates :order_num, presence: true, length: { minimum: 2 }
	validates :comments, presence: true
	validates :email, format: { with: /\A[^@\s]+@([^@\s]+\.)+[^@\s]+\z/, message: "invalid format"}, presence: true
end
