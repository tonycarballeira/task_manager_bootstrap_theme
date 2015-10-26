class CreateSysSlaLogActions < ActiveRecord::Migration
  def up
    unless table_exists?('sys_sla_log_action')
      execute "CREATE TABLE [dbo].[sys_sla_log_action](

				[sla_id] [int] IDENTITY(1,1) NOT NULL,
				[sla_name] [nvarchar](255) NULL,
				[sla_sya_id] [int] NULL,
				[sla_sym_id] [int] NULL,
				[sla_ste_id] [int] NULL,
				[sla_action] [nvarchar](50) NULL,
				[sla_object] [nvarchar](255) NULL,
				[sla_object_table] [nvarchar](255) NULL,
				[sla_object_id] [int] NULL,
				[sla_object_ref] [nvarchar](255) NULL,
				[sla_ip] [nvarchar](50) NULL,
				[sla_datestamp] [datetime] NULL,
				[sla_ost_id] [int] NULL,
			 CONSTRAINT [PK_sys_sla_log_action] PRIMARY KEY CLUSTERED 
			(
				[sla_id] ASC
			)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
			) ON [PRIMARY]"
    end
    
  end

  def down
  	remove_table 'sys_sla_log_action'
  end
end
