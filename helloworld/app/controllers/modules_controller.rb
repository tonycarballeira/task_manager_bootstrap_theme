class ModulesController < ApplicationController

	around_filter :record_not_found

	def index
		cookies[:user_id] = 7 
		@user = SysSyaAccount.find(cookies[:user_id]) 
	end

	def show
		# @module = SysSymModule.find(params["id"].slice(6, 6))

		@module = SysSymModule.find(params["id"])
		
		# TODO: logging occurs here

		# if module is not associated with current user redirect to index page

		unless SysSyaAccount.find(cookies[:user_id]).sys_sym_modules.include?(@module)
			redirect_to modules_path
		end
	end

	private

	def record_not_found
		yield
		
		rescue ActiveRecord::RecordNotFound
	  		redirect_to modules_url
	end
	
end