class CreateContactForms < ActiveRecord::Migration
  def change
    create_table :contact_forms do |t|
      t.string :full_name
      t.string :email
      t.string :order_num
      t.text :comments

      t.timestamps null: false
    end
  end
end
