class SysRlnSyaSym < ActiveRecord::Base
	self.table_name = "sys_rln_sya_sym"
	belongs_to :sys_sym_module, :foreign_key => :rln_sym_id, :primary_key => :sym_id
	belongs_to :sys_sya_account, :foreign_key => :rln_sya_id, :primary_key => :sya_id
end