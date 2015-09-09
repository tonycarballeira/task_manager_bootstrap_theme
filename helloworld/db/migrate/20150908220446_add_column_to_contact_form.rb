class AddColumnToContactForm < ActiveRecord::Migration
  def change
  	add_column :contact_forms, :subject, :integer
  end
end
