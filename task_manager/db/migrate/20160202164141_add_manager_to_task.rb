class AddManagerToTask < ActiveRecord::Migration
  def change
  	add_column :tasks, :manager_id, :integer
  end
end
