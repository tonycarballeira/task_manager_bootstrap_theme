class Task < ActiveRecord::Base

	belongs_to :user

	validates :title, presence: true
	validates :body, presence: true
	validates :user_id, presence: true
	validates :manager_id, presence: true
	
end
