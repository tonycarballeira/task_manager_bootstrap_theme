class CreateSysSqcQueryControls < ActiveRecord::Migration
  def up
    unless table_exists?('sys_sqc_query_control')
      execute "CREATE TABLE [dbo].[sys_sqc_query_control](

				[sqc_id] [int] IDENTITY(1,1) NOT NULL,
				[sqc_sya_id] [int] NULL,
				[sqc_name] [nvarchar](100) NULL,
				[sqc_column] [int] NULL,
				[sqc_direction] [nvarchar](50) NULL,
				[sqc_count] [int] NULL,
			 CONSTRAINT [PK_sys_sqc_query_control] PRIMARY KEY CLUSTERED 
			(
				[sqc_id] ASC
			)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
			) ON [PRIMARY]"
    end
    
  end

  def down
  	remove_table 'sys_sqc_query_control'
  end
end
