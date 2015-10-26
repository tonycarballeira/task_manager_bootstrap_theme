class CreateSysSleLogErrors < ActiveRecord::Migration
  def up
    unless table_exists?('sys_sle_log_error')
      execute "CREATE TABLE [dbo].[sys_sle_log_error](

				[sle_id] [int] IDENTITY(1,1) NOT NULL,
				[sle_name] [nvarchar](255) NULL,
				[sle_sya_id] [int] NULL,
				[sle_sym_id] [int] NULL,
				[sle_ste_id] [int] NULL,
				[sle_error_id] [nvarchar](50) NULL,
				[sle_error_type] [nvarchar](100) NULL,
				[sle_error_message] [ntext] NULL,
				[sle_error_detail] [ntext] NULL,
				[sle_error_query] [ntext] NULL,
				[sle_url] [nvarchar](255) NULL,
				[sle_ip] [nvarchar](50) NULL,
				[sle_datestamp] [datetime] NULL,
				[sle_ost_id] [int] NULL,
			 CONSTRAINT [PK_sys_sle_log_error] PRIMARY KEY CLUSTERED 
			(
				[sle_id] ASC
			)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
			) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]"
    end
    
  end

  def down
  	remove_table 'sys_sle_log_error'
  end
end
