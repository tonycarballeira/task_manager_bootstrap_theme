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

	def edit
    	@user = User.find(params[:id])
  	end

  	def update
    	@user = User.find(params[:id])
 
    	if @user.update(user_params)
      		redirect_to accounts_path, :notice => "Account Updated!"
    	else
      		render 'edit'
    	end
  	end


	def destroy
  		@user = User.find(params[:id])
  		@user.destroy
 
  		redirect_to accounts_path, :notice => "Account deleted!"
	end

	def activate
		@user = User.find(params[:format])

		@user.update_attributes(:active => true)

		redirect_to accounts_path, :notice => "Account Activated!"
	end

	def suspend
		@user = User.find(params[:format])

		@user.update_attributes(:active => false)

		redirect_to accounts_path, :notice => "Account Suspended!"
	end

	private
  	
  	## Strong Parameters 
	def user_params
    	params.require(:user).permit(:email, :password, :password_confirmation, :manager)
  	end

end
