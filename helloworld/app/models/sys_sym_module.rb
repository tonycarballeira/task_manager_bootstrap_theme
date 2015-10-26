class SysSymModule < ActiveRecord::Base
	self.table_name = "sys_sym_module"
	has_many :sys_rln_sya_syms, :foreign_key => :rln_sym_id, :primary_key => :sym_id
	has_many :sys_sya_accounts, :through => :sys_rln_sya_syms

	def to_param
		"module#{id}"
	end

end