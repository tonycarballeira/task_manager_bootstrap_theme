class TasksController < ApplicationController

	def new
		@task = Task.new
	end

	def create

		@task = Task.new(user_params)

		if @task.save	
			redirect_to manager_tasks_path, :notice => "New Task Assigned!"
		else
			render "new"
		end
	end


	private
  	
  	## Strong Parameters 
	def task_params
    	params.require(:user).permit(:title, :body)
  	end
end
