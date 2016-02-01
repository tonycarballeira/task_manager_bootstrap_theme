class PagesController < ApplicationController

  def home
  	@accounts = User.all
  end

  def accounts
  	unless current_user && current_user.manager
  		redirect_to root_url, :notice => "You are not a Manager!"
  	end
  end

  def manager_tasks
  	unless current_user && current_user.manager
  		redirect_to root_url, :notice => "You are not a Manager!"
  	end
  end

end
