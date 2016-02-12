class AddUserAndTaskToUpdates < ActiveRecord::Migration
  def change
  	add_reference :updates, :user, index: true
  	add_reference :updates, :task, index: true
  end
end
