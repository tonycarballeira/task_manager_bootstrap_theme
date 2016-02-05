class TasksController < ApplicationController

	def new
		@task = Task.new
    @team_id = params[:team_id]

    if @team_id
      @users = Team.find(@team_id).users
    else
      @users = User.where(:access => 3)
    end
	end

  def update_users
    # updates users based on team selected
    team = Team.find(params[:team_id])
    # map to email and id for use in our options_for_select
    @users = team.users.map{|a| [a.email, a.id]}.insert(0, "")
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

    if current_user.access == 1

      @tasks = Task.all

    elsif current_user.access == 2

      @tasks = []

      Task.all.each do |x|
        manager = User.where(:id => x.manager_id)[0]

        if (manager.teams != []) && (manager.teams[0].id == current_user.teams[0].id)
          @tasks << x
        end
      end

    else

      @tasks = Task.where(:user_id => current_user.id)
      
    end

  end

  def show
    @task = Task.find(params[:id])

    @updates = Update.where(:task_id => @task.id)
  end


	private
  	
  	## Strong Parameters 
	def task_params
  	params.require(:task).permit(:id, :title, :body, :user_id, :manager_id)
	end
end
