class CreateSysSteSites < ActiveRecord::Migration
  def up
    unless table_exists?('sys_ste_site')
      execute "CREATE TABLE [dbo].[sys_ste_site](

				[ste_id] [int] IDENTITY(1,1) NOT NULL,
				[ste_name] [nvarchar](255) NULL,
				[ste_value] [nvarchar](255) NULL,
				[ste_priority] [int] NULL,
				[ste_ost_id] [int] NULL,
			 CONSTRAINT [PK_sys_ste_site] PRIMARY KEY CLUSTERED 
			(
				[ste_id] ASC
			)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
			) ON [PRIMARY]"
    end
    
  end

  def down
  	remove_table 'sys_ste_site'
  end
end
