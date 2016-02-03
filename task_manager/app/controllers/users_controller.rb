class UsersController < ApplicationController

	def new
		@user = User.new

		if current_user.access == 1
			@user.memberships.build
		end
	end

	def create

		@user = User.new(user_params)

		if @user.save
			if current_user.access < 3
				redirect_to users_path, :notice => "New Account Created!"
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
      		redirect_to users_path, :notice => "Account Updated!"
    	else
      		render 'edit'
    	end
  	end


	def destroy
  		@user = User.find(params[:id])
  		@user.destroy
 
  		redirect_to users_path, :notice => "Account deleted!"
	end

	def index
		unless current_user && current_user.access < 3
  			redirect_to root_url, :notice => "You are not a Manager!"
  		end
  		
  		@accounts = User.all
	end

	def activate
		@user = User.find(params[:format])

		@user.update_attributes(:active => true)

		redirect_to users_path, :notice => "Account Activated!"
	end

	def suspend
		@user = User.find(params[:format])

		@user.update_attributes(:active => false)

		redirect_to users_path, :notice => "Account Suspended!"
	end

	private
  	
  	## Strong Parameters 
	def user_params
    	params.require(:user).permit(:email, :password, :password_confirmation, :manager, :access, memberships_attributes: [:id, :team_id, :user_id])
  	end

end
