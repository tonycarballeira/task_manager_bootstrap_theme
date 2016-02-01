class UsersController < ApplicationController

	def new
		@user = User.new
	end

	def create

		@user = User.new(user_params)

		if @user.save
			if current_user.manager
				redirect_to accounts_path, :notice => "New Account Created!"
			else
				redirect_to root_url, :notice => "Signed up!"
			end
		else
			render "new"
		end
	end

	private
  	
  	## Strong Parameters 
	def user_params
    	params.require(:user).permit(:email, :password, :password_confirmation, :manager)
  	end

end
