json.array!(@subscriptions) do |subscription|
  json.extract! subscription, :id, :email, :name, :list
  json.url subscription_url(subscription, format: :json)
end
