class RemoveSubjectFromContactForm < ActiveRecord::Migration
  def change
  	remove_column :contact_forms, :subject
  end
end
