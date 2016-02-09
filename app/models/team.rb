class Team < ActiveRecord::Base

	has_many :memberships, :foreign_key => :team_id, :primary_key => :id, :dependent => :destroy
  	has_many :users, :through => :memberships

  	validates_presence_of :name
  	validates_uniqueness_of :name
  	
end
