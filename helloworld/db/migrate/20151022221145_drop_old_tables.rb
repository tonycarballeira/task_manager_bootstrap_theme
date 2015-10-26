class DropOldTables < ActiveRecord::Migration
  def change
  	drop_table :contact_forms
  	drop_table :controls
  	drop_table :products
  	drop_table :subjects
  	drop_table :subscriptions
  end
end