class PagesController < ApplicationController

  def home
  	@user_tasks = Task.where(:user_id => current_user.id)
  end

end
