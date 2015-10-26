class CreateSysStxTextLabels < ActiveRecord::Migration
  def up
    unless table_exists?('sys_stx_text_label')
      execute "CREATE TABLE [dbo].[sys_stx_text_label](

				[stx_id] [int] IDENTITY(1,1) NOT NULL,
				[stx_name] [nvarchar](100) NULL,
				[stx_value] [nvarchar](255) NULL,
				[stx_ost_id] [int] NULL,
			 CONSTRAINT [PK_sys_stx_text_label] PRIMARY KEY CLUSTERED 
			(
				[stx_id] ASC
			)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
			) ON [PRIMARY]"
    end
    
  end

  def down
  	remove_table 'sys_stx_text_label'
  end
end