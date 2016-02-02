class TeamsController < ApplicationController
	def new
		@team = Team.new
	end

	def create

		@team = Team.new(team_params)

		if @team.save			
			redirect_to accounts_path, :notice => "New Team Created!"
		else
			render "new"
		end
	end

	private
  	
  	## Strong Parameters 
	def team_params
    	params.require(:team).permit(:name)
  	end
end
