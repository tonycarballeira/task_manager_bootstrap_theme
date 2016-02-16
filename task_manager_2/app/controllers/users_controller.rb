class UsersController < ApplicationController

	before_filter :user_restrict

	def new

		@user = User.new
		@user.memberships.build	

	end

	def create

		@user = User.new(user_params)

		if @user.save
			redirect_to users_path, :notice => "New Account Created!"
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
      		render "edit"
    	end

  	end


	def destroy

  		@user = User.find(params[:id])
  		@user.destroy
 
  		redirect_to users_path, :notice => "Account deleted!"

	end

	def index

		if current_user.access == 1	
  			@accounts = User.all
		else
  			@staffers = User.where(:access => 3)
  		end

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

	    	params.require(:user).permit(:email, :first_name, :last_name, :password, :password_confirmation, :manager, :access, memberships_attributes: [:id, :team_id, :user_id])

	  	end

	  	def user_restrict

	  		unless current_user && current_user.access < 3
	  			redirect_to root_path
	  		end

	  	end

end
