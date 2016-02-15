class TasksController < ApplicationController

	def new

		@task = Task.new

    if current_user.teams != []

      team = current_user.teams[0]
      
      @users = team.users.where(:access => 3).where(:active => true)

    else

      @users = User.where(:active => true)
      
    end  

	end

  def update_users

    # updates users based on team selected
    team = Team.find(params[:team_id])
    # map to email and id for use in our options_for_select
    @users = team.users.where(:access => 3).where(:active => true).map{|a| [a.email, a.id]}.insert(0, "")

  end

	def create

		@task = Task.new(task_params)

    if current_user.teams != []
      team = current_user.teams[0]
      @users = team.users.where(:access => 3).where(:active => true)
    else
      @users = User.where(:active => true)
    end

		if @task.save	
			redirect_to tasks_path, :notice => "New Task Assigned!"
		else
			render "new"
		end

	end

	def edit

    	@task = Task.find(params[:id])

      if current_user.teams != []

        team = current_user.teams[0]
        
        @users = team.users.where(:access => 3).where(:active => true)

      else

        @users = User.where(:active => true)

      end  

	end

	def update

  	@task = Task.find(params[:id])
 
  	if @task.update(task_params)
    		redirect_to tasks_path, :notice => "Task Updated!"
  	else
    		render "edit"
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

  def destroy

    @task = Task.find(params[:id])
    @task.destroy

    redirect_to tasks_path, :notice => "Task deleted!"

  end


	private
  	
    ## Strong Parameters 
  	def task_params

    	params.require(:task).permit(:id, :title, :body, :user_id, :manager_id)
      
  	end
end
