class CreateSysSymModules < ActiveRecord::Migration
  def up
    unless table_exists?('sys_sym_module')
      execute "CREATE TABLE [dbo].[sys_sym_module](

				[sym_id] [int] IDENTITY(1,1) NOT NULL,
				[sym_name] [nvarchar](50) NULL,
				[sym_icon] [nvarchar](100) NULL,
				[sym_folder] [nvarchar](100) NULL,
				[sym_object] [nvarchar](100) NULL,
				[sym_sym_id] [int] NULL,
				[sym_url] [nvarchar](255) NULL,
				[sym_priority] [int] NULL,
				[sym_action_add] [int] NULL,
				[sym_action_advanced] [int] NULL,
				[sym_action_archive] [int] NULL,
				[sym_action_delete] [int] NULL,
				[sym_action_download] [int] NULL,
				[sym_action_edit] [int] NULL,
				[sym_action_run] [int] NULL,
				[sym_action_test] [int] NULL,
				[sym_action_view] [int] NULL,
				[sym_beta_date] [datetime] NULL,
				[sym_ost_id] [int] NULL,
			 CONSTRAINT [PK_sys_sym_module] PRIMARY KEY CLUSTERED 
			(
				[sym_id] ASC
			)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
			) ON [PRIMARY]"
    end
    
  end

  def down
  	remove_table 'sys_sym_module'
  end
end