class PagesController < ApplicationController

  def home

  	if current_user.access == 1

      @tasks = Task.all
      @users = User.all

    elsif current_user.access == 2

      @users = User.where(:access => 3)
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

  def test
  end

end
