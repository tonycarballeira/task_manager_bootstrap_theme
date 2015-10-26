class CreateSysOstObjectStatuses < ActiveRecord::Migration
  def up
    unless table_exists?('sys_ost_object_status')
      execute "CREATE TABLE [dbo].[sys_ost_object_status](

        				[ost_id] [int] IDENTITY(1,1) NOT NULL,
        				[ost_name] [nvarchar](50) NULL,
        			CONSTRAINT [PK_sys_ost_object_status] PRIMARY KEY CLUSTERED 
        			(
        				[ost_id] ASC
        			)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
        			) ON [PRIMARY]"
    end
    
  end

  def down
  	remove_table 'sys_ost_object_status'
  end
end
