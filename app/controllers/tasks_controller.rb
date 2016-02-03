class TasksController < ApplicationController

	def new
		@task = Task.new
	end

	def create

		@task = Task.new(task_params)

		if @task.save	
			redirect_to tasks_path, :notice => "New Task Assigned!"
		else
			render "new"
		end
	end

	def edit
    	@task = Task.find(params[:id])
  	end

  	def update
    	@task = Task.find(params[:id])
 
    	if @task.update(task_params)
      		redirect_to tasks_path, :notice => "Task Updated!"
    	else
      		render 'edit'
    	end
  	end

  	def index
  		unless current_user && current_user.access < 3
  			redirect_to root_url, :notice => "You are not a Manager!"
  		end

    	@tasks = Task.all
  	end


	private
  	
  	## Strong Parameters 
	def task_params
    	params.require(:task).permit(:title, :body, :user_id, :manager_id)
  	end
end
