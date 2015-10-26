class CreateSysSyaAccounts < ActiveRecord::Migration
  def up
    unless table_exists?('sys_sya_account')
      execute "CREATE TABLE [dbo].[sys_sya_account](

				[sya_id] [int] IDENTITY(1,1) NOT NULL,
				[sya_name] [nvarchar](100) NULL,
				[sya_email] [nvarchar](100) NULL,
				[sya_password] [nvarchar](50) NULL,
				[sya_system] [int] NULL,
				[sya_ste_id] [int] NULL,
				[sya_ost_id] [int] NULL,
			 CONSTRAINT [PK_sys_sya_account] PRIMARY KEY CLUSTERED 
			(
				[sya_id] ASC
			)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
			) ON [PRIMARY]"
    end
    
  end

  def down
  	remove_table 'sys_sya_account'
  end
end