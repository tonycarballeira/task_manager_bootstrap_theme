class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  protect_from_forgery with: :null_session
  def mod_user
  	@header = 'application/header/'
  	@body = 'application/body/'
  	@footer = 'application/footer/'

  	@app = {

  		modules: {
  			header: 'application/header/',
  			body: 'application/body/',
  			footer: 'application/footer/'
  		},

  	}

    sql = "SELECT * FROM contact_forms"
    
    @sql = Rails.cache.fetch("your_cache_key", :expires_in => 5.minutes) do
      ActiveRecord::Base.connection.exec_query(sql)
  end

  if params['done'] && params['done'] == 'true'
      redirect_to done_path 
    end 


  end
end
