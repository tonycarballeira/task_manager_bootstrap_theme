module SqlModules
	module Resolve
		module SqlQueryHelper
			def form_query
				sql = "
				  SELECT * 
				  FROM contact_forms
				"
		        @forms = ActiveRecord::Base.connection.exec_query(sql)
			end
		end
	end
end