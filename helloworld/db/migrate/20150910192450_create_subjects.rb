class CreateSubjects < ActiveRecord::Migration
  def change
    create_table :subjects do |t|
      t.string :name
      t.string :value
      t.integer :ost_id
      t.integer :priority

      t.timestamps null: false
    end
  end
end
