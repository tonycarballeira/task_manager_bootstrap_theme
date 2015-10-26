class CreateSysRlnSyaSyms < ActiveRecord::Migration
  def up
    unless table_exists?('sys_rln_sya_sym')
      execute "CREATE TABLE [dbo].[sys_rln_sya_sym](

				[rln_sya_id] [int] NULL,
				[rln_sym_id] [int] NULL,
				[rln_sym_action_add] [int] NULL,
				[rln_sym_action_advanced] [int] NULL,
				[rln_sym_action_archive] [int] NULL,
				[rln_sym_action_delete] [int] NULL,
				[rln_sym_action_download] [int] NULL,
				[rln_sym_action_edit] [int] NULL,
				[rln_sym_action_run] [int] NULL,
				[rln_sym_action_test] [int] NULL,
				[rln_sym_action_view] [int] NULL
			) ON [PRIMARY]"
    end
    
  end

  def down
  	remove_table 'sys_rln_sya_sym'
  end
end