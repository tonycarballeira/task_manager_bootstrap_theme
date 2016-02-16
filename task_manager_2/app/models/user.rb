class User < ActiveRecord::Base

  has_many :memberships, :foreign_key => :user_id, :primary_key => :id, :dependent => :destroy
  has_many :teams, :through => :memberships
  has_many :tasks, :dependent => :destroy
  has_many :updates, :dependent => :destroy

  accepts_nested_attributes_for :memberships

	attr_accessor :password

	before_save :encrypt_password

  validates_presence_of :email
  validates_presence_of :first_name
  validates_presence_of :last_name
  validates_uniqueness_of :email
	validates_confirmation_of :password
	validates_presence_of :password, :on => :create
	

	def self.authenticate(email, password)

    	user = find_by_email(email)

    	if user && user.password_hash == BCrypt::Engine.hash_secret(password, user.password_salt)
      		user
    	else
      		nil
    	end
      
	end

	def encrypt_password

    	if password.present?
      		self.password_salt = BCrypt::Engine.generate_salt
      		self.password_hash = BCrypt::Engine.hash_secret(password, password_salt)
    	end

  end

  def suspend
    
  end

end
