class PagesController < ApplicationController

  def home

  	if current_user && current_user.access == 1

      @tasks = Task.all
      @users = User.all

    elsif current_user && current_user.access == 2

      # USERS

      @users = []

      User.all.each do |acc|
        if (acc.teams != []) && (acc.teams[0].id == current_user.teams[0].id) && (acc.access == 3)
          @users << acc
        end
      end

      puts @users

      # ACCOUNTS

      @tasks = []

      Task.all.each do |x|
        manager = User.where(:id => x.manager_id)[0]

        if (manager.teams != []) && (manager.teams[0].id == current_user.teams[0].id)
          @tasks << x
        end
      end

    else

      if current_user

        @tasks = Task.where(:user_id => current_user.id)

      end
      
    end
  	
  end

  def index
    @tasks = Task.where(:user_id => current_user.id)
  end

end
