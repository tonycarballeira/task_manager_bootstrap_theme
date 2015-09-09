json.array!(@contact_forms) do |contact_form|
  json.extract! contact_form, :id, :full_name, :email, :order_num, :comments
  json.url contact_form_url(contact_form, format: :json)
end
