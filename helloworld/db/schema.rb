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

ActiveRecord::Schema.define(version: 20150914212112) do

  create_table "contact_forms", force: :cascade do |t|
    t.string   "full_name",  limit: 4000
    t.string   "email",      limit: 4000
    t.string   "order_num",  limit: 4000
    t.text     "comments",   limit: 2147483647
    t.datetime "created_at",                    null: false
    t.datetime "updated_at",                    null: false
    t.integer  "subject_id", limit: 4
  end

  add_index "contact_forms", ["subject_id"], name: "index_contact_forms_on_subject_id"

  create_table "subjects", force: :cascade do |t|
    t.string   "name",       limit: 4000
    t.string   "value",      limit: 4000
    t.integer  "ost_id",     limit: 4
    t.integer  "priority",   limit: 4
    t.datetime "created_at",              null: false
    t.datetime "updated_at",              null: false
  end

  create_table "subscriptions", force: :cascade do |t|
    t.string   "email",      limit: 4000
    t.string   "name",       limit: 4000
    t.string   "list",       limit: 4000
    t.datetime "created_at",              null: false
    t.datetime "updated_at",              null: false
    t.integer  "ost_id",     limit: 4
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

  add_foreign_key "contact_forms", "subjects"
end
