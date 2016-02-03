class PagesController < ApplicationController

  def home
  	if current_user && current_user.access == 3
  		@user_tasks = Task.where(:user_id => current_user.id)
  	end
  end

end
