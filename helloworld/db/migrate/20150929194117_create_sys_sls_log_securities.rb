class CreateSysSlsLogSecurities < ActiveRecord::Migration
  def up
    unless table_exists?('sys_sls_log_security')
      execute "CREATE TABLE [dbo].[sys_sls_log_security](

				[sls_id] [int] IDENTITY(1,1) NOT NULL,
				[sls_name] [nvarchar](255) NULL,
				[sls_sya_id] [int] NULL,
				[sls_sym_id] [int] NULL,
				[sls_ste_id] [int] NULL,
				[sls_event] [nvarchar](100) NULL,
				[sls_url] [nvarchar](255) NULL,
				[sls_client] [ntext] NULL,
				[sls_ip] [nvarchar](50) NULL,
				[sls_datestamp] [datetime] NULL,
				[sls_ost_id] [int] NULL,
			 CONSTRAINT [PK_sys_sls_log_security] PRIMARY KEY CLUSTERED 
			(
				[sls_id] ASC
			)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
			) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]"
    end
    
  end

  def down
  	remove_table 'sys_sls_log_security'
  end
end
