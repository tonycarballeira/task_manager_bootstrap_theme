class ContactMailer < ApplicationMailer

  # Subject can be set in your I18n file at config/locales/en.yml
  # with the following lookup:
  #
  #   en.contact_mailer.contact_email.subject
  #
  def contact_email(contact_form)
    @contact_form = contact_form

    mail to: contact_form.subject.value, subject: "Contact"
  end

end
