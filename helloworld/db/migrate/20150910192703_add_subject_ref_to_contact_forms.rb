class AddSubjectRefToContactForms < ActiveRecord::Migration
  def change
    add_reference :contact_forms, :subject, index: true, foreign_key: true
  end
end
