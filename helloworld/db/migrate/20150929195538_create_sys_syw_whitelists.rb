class CreateSysSywWhitelists < ActiveRecord::Migration
  def up
    unless table_exists?('sys_syw_whitelist')
      execute "CREATE TABLE [dbo].[sys_syw_whitelist](

				[syw_id] [int] IDENTITY(1,1) NOT NULL,
				[syw_name] [nvarchar](255) NULL,
				[syw_value] [nvarchar](50) NULL,
				[syw_ste_id] [int] NULL,
				[syw_ost_id] [int] NULL,
			 CONSTRAINT [PK_sys_syw_whitelist] PRIMARY KEY CLUSTERED 
			(
				[syw_id] ASC
			)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
			) ON [PRIMARY]"
    end
    
  end

  def down
  	remove_table 'sys_syw_whitelist'
  end
end
