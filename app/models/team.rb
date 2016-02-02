class Team < ActiveRecord::Base
	has_many :memberships, :foreign_key => :team_id, :primary_key => :id, :dependent => :destroy
  	has_many :users, :through => :memberships
end
