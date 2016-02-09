class UpdatesController < ApplicationController

	def new

		@update = Update.new
		@task_id = params[:task_id]
		@@task = Task.where(:id => @task_id)[0]
		
	end

	def create

		@update = Update.new(update_params)

		if @update.save			
			redirect_to task_path(@@task), :notice => "Update created!"		
		else
			render "new"
		end

	end

	private
  	
	  	## Strong Parameters 
		def update_params

	  		params.require(:update).permit(:id, :title, :body, :user_id, :task_id)

		end

end
