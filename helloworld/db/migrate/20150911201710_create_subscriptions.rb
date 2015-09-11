class CreateSubscriptions < ActiveRecord::Migration
  def change
    create_table :subscriptions do |t|
      t.string :email
      t.string :name
      t.string :list

      t.timestamps null: false
    end
  end
end
