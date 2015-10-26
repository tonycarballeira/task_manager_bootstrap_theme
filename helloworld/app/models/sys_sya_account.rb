class SysSyaAccount < ActiveRecord::Base
	self.table_name = "sys_sya_account"
	has_many :sys_rln_sya_syms, :foreign_key => :rln_sya_id, :primary_key => :sya_id
	has_many :sys_sym_modules, :through => :sys_rln_sya_syms
end