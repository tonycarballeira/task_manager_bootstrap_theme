class PagesController < ApplicationController

  def home
  	
  end

  def accounts
  	unless current_user && current_user.manager
  		redirect_to root_url, :notice => "You are not a Manager!"
  	end
  	@accounts = User.all
  end

  def manager_tasks
  	unless current_user && current_user.manager
  		redirect_to root_url, :notice => "You are not a Manager!"
  	end
  end

end
