class UpdatesController < ApplicationController

	def new
		@update = Update.new
	end

	def create

		@update = Update.new(update_params)

		if @update.save			
			redirect_to root_url, :notice => "Signed up!"		
		else
			render "new"
		end
	end

	private
  	
  	## Strong Parameters 
	def task_params
  		params.require(:update).permit(:id, :title, :body, :user_id)
	end

end
