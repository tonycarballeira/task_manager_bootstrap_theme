class AddIdToRlnJoin < ActiveRecord::Migration
  def change
  	add_column :sys_rln_sya_sym, :rln_id, :primary_key
  end
end
