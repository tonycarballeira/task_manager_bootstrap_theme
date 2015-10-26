# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20151022221145) do

  create_table "sys_ost_object_status", primary_key: "ost_id", force: :cascade do |t|
    t.string "ost_name", limit: 50
  end

  create_table "sys_rln_sya_sym", primary_key: "rln_id", force: :cascade do |t|
    t.integer "rln_sya_id",              limit: 4
    t.integer "rln_sym_id",              limit: 4
    t.integer "rln_sym_action_add",      limit: 4
    t.integer "rln_sym_action_advanced", limit: 4
    t.integer "rln_sym_action_archive",  limit: 4
    t.integer "rln_sym_action_delete",   limit: 4
    t.integer "rln_sym_action_download", limit: 4
    t.integer "rln_sym_action_edit",     limit: 4
    t.integer "rln_sym_action_run",      limit: 4
    t.integer "rln_sym_action_test",     limit: 4
    t.integer "rln_sym_action_view",     limit: 4
  end

  create_table "sys_sla_log_action", primary_key: "sla_id", force: :cascade do |t|
    t.string   "sla_name",         limit: 255
    t.integer  "sla_sya_id",       limit: 4
    t.integer  "sla_sym_id",       limit: 4
    t.integer  "sla_ste_id",       limit: 4
    t.string   "sla_action",       limit: 50
    t.string   "sla_object",       limit: 255
    t.string   "sla_object_table", limit: 255
    t.integer  "sla_object_id",    limit: 4
    t.string   "sla_object_ref",   limit: 255
    t.string   "sla_ip",           limit: 50
    t.datetime "sla_datestamp"
    t.integer  "sla_ost_id",       limit: 4
  end

  create_table "sys_sle_log_error", primary_key: "sle_id", force: :cascade do |t|
    t.string   "sle_name",          limit: 255
    t.integer  "sle_sya_id",        limit: 4
    t.integer  "sle_sym_id",        limit: 4
    t.integer  "sle_ste_id",        limit: 4
    t.string   "sle_error_id",      limit: 50
    t.string   "sle_error_type",    limit: 100
    t.ntext    "sle_error_message", limit: 2147483647
    t.ntext    "sle_error_detail",  limit: 2147483647
    t.ntext    "sle_error_query",   limit: 2147483647
    t.string   "sle_url",           limit: 255
    t.string   "sle_ip",            limit: 50
    t.datetime "sle_datestamp"
    t.integer  "sle_ost_id",        limit: 4
  end

  create_table "sys_sls_log_security", primary_key: "sls_id", force: :cascade do |t|
    t.string   "sls_name",      limit: 255
    t.integer  "sls_sya_id",    limit: 4
    t.integer  "sls_sym_id",    limit: 4
    t.integer  "sls_ste_id",    limit: 4
    t.string   "sls_event",     limit: 100
    t.string   "sls_url",       limit: 255
    t.ntext    "sls_client",    limit: 2147483647
    t.string   "sls_ip",        limit: 50
    t.datetime "sls_datestamp"
    t.integer  "sls_ost_id",    limit: 4
  end

  create_table "sys_sqc_query_control", primary_key: "sqc_id", force: :cascade do |t|
    t.integer "sqc_sya_id",    limit: 4
    t.string  "sqc_name",      limit: 100
    t.integer "sqc_column",    limit: 4
    t.string  "sqc_direction", limit: 50
    t.integer "sqc_count",     limit: 4
  end

  create_table "sys_ste_site", primary_key: "ste_id", force: :cascade do |t|
    t.string  "ste_name",     limit: 255
    t.string  "ste_value",    limit: 255
    t.integer "ste_priority", limit: 4
    t.integer "ste_ost_id",   limit: 4
  end

  create_table "sys_stx_text_label", primary_key: "stx_id", force: :cascade do |t|
    t.string  "stx_name",   limit: 100
    t.string  "stx_value",  limit: 255
    t.integer "stx_ost_id", limit: 4
  end

  create_table "sys_sya_account", primary_key: "sya_id", force: :cascade do |t|
    t.string  "sya_name",     limit: 100
    t.string  "sya_email",    limit: 100
    t.string  "sya_password", limit: 50
    t.integer "sya_system",   limit: 4
    t.integer "sya_ste_id",   limit: 4
    t.integer "sya_ost_id",   limit: 4
  end

  create_table "sys_sym_module", primary_key: "sym_id", force: :cascade do |t|
    t.string   "sym_name",            limit: 50
    t.string   "sym_icon",            limit: 100
    t.string   "sym_folder",          limit: 100
    t.string   "sym_object",          limit: 100
    t.integer  "sym_sym_id",          limit: 4
    t.string   "sym_url",             limit: 255
    t.integer  "sym_priority",        limit: 4
    t.integer  "sym_action_add",      limit: 4
    t.integer  "sym_action_advanced", limit: 4
    t.integer  "sym_action_archive",  limit: 4
    t.integer  "sym_action_delete",   limit: 4
    t.integer  "sym_action_download", limit: 4
    t.integer  "sym_action_edit",     limit: 4
    t.integer  "sym_action_run",      limit: 4
    t.integer  "sym_action_test",     limit: 4
    t.integer  "sym_action_view",     limit: 4
    t.datetime "sym_beta_date"
    t.integer  "sym_ost_id",          limit: 4
  end

  create_table "sys_syw_whitelist", primary_key: "syw_id", force: :cascade do |t|
    t.string  "syw_name",   limit: 255
    t.string  "syw_value",  limit: 50
    t.integer "syw_ste_id", limit: 4
    t.integer "syw_ost_id", limit: 4
  end

  create_table "tst_dmo_demo", primary_key: "dmo_id", force: :cascade do |t|
    t.string   "dmo_name",      limit: 50
    t.ntext    "dmo_value",     limit: 2147483647
    t.money    "dmo_price",                        precision: 19, scale: 4
    t.datetime "dmo_datestamp"
    t.integer  "dmo_ost_id",    limit: 4
  end

  create_table "tst_exp_example", primary_key: "exp_id", force: :cascade do |t|
    t.string   "exp_name",      limit: 50
    t.ntext    "exp_value",     limit: 2147483647
    t.money    "exp_price",                        precision: 19, scale: 4
    t.integer  "exp_priority",  limit: 4
    t.string   "exp_ip",        limit: 50
    t.datetime "exp_datestamp"
    t.integer  "exp_ost_id",    limit: 4
  end

end