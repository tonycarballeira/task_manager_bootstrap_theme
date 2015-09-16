module SqlModules::Resolve::ContactForms
	def form_query
		sql = "
		  SELECT * 
		  FROM contact_forms
		"
        @forms = ActiveRecord::Base.connection.exec_query(sql)
	end

	def self.included(base)
    	base.send :helper_method, :form_query if base.respond_to? :helper_method
	end
end
	