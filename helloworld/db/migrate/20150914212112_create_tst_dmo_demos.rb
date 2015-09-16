class CreateTstDmoDemos < ActiveRecord::Migration
  def up
    unless table_exists?('tst_dmo_demo')
      execute "CREATE TABLE [dbo].[tst_dmo_demo](

				[dmo_id] [int] IDENTITY(1,1) NOT NULL,

				[dmo_name] [nvarchar](50) NULL,

				[dmo_value] [ntext] NULL,

				[dmo_price] [money] NULL,

				[dmo_datestamp] [datetime] NULL,

				[dmo_ost_id] [int] NULL,

			   CONSTRAINT [PK_tst_dmo_demo] PRIMARY KEY CLUSTERED

			   (

				   [dmo_id] ASC

			   )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

			   ) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]"
    end
    
  end

  def down
  	reomve_table 'tst_dmo_demo'
  end
end
