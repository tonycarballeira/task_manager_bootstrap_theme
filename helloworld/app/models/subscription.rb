class Subscription < ActiveRecord::Base
	before_create :status_assign

	def status_assign
		self.ost_id = 2
	end
end
