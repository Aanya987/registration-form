import anvil.server
import anvil.email

@anvil.server.callable
def send_registration_email(name, mailid, branch, response):
  subject = "New SRM Registration Form Submission"

  body = f"""
A new registration form has been submitted.

Name: {name}
Email ID: {mailid}
Branch: {branch}
Confirmation Checkbox: {response}
"""

  # Change this email to the one where YOU want to receive responses
  anvil.email.send(
    to="aanyaaa.021@gmail.com",
    subject=subject,
    text=body
  )

  return "Email sent successfully"