class AddStatusToSubscription < ActiveRecord::Migration
  def change
  	add_column :subscriptions, :ost_id, :integer
  end
end
