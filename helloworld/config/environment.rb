# Load the Rails application.
require File.expand_path('../application', __FILE__)

# Initialize the Rails application.
Rails.application.initialize!
Dir.glob("#{RAILS_ROOT}/app/helpers/*[^(.rb|.ignore)]").each{|dir| config.load_paths << dir }

ActionMailer::Base.smtp_settings = {
    :address => "smtp.gmail.com",
    :port => "587",
    :domain => "gmail.com",
    :user_name => "tonycarballeira@gmail.com",
    :password => "",
    :authentication => "plain",
    :enable_starttls_auto => true
}