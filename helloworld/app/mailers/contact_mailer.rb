class ContactMailer < ApplicationMailer

  # Subject can be set in your I18n file at config/locales/en.yml
  # with the following lookup:
  #
  #   en.contact_mailer.contact_email.subject
  #
  def contact_email(contact_form)
    @contact_form = contact_form
    to_email = ""
    
    if contact_form.subject == 1
    	to_email = "chinaski87@outlook.com"
    else
    	to_email = "tonycarballeira@gmail.com"
    end

    mail to: to_email, subject: "Contact"
  end

end
