from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

  def outlined_button_1_click(self, **event_args):
    """This method is called when the Submit button is clicked"""

    name = self.text_box_1.text.strip() if self.text_box_1.text else ""
    mailid = self.text_box_2.text.strip() if self.text_box_2.text else ""
    branch = self.text_box_3.text.strip() if self.text_box_3.text else ""
    response = self.check_box_1.checked

    # Validation
    if not name or not mailid or not branch:
      Notification("Please fill all the fields.", style="danger").show()
      return

    if "@" not in mailid or "." not in mailid:
      Notification("Please enter a valid email address.", style="danger").show()
      return

    if not response:
      Notification("Please tick the checkbox before submitting.", style="warning").show()
      return

    try:
      result = anvil.server.call(
        'submit_registration',
        name=name,
        mailid=mailid,
        branch=branch,
        response=response
      )

      Notification(result, style="success").show()

      # Clear form after successful submit
      self.text_box_1.text = ""
      self.text_box_2.text = ""
      self.text_box_3.text = ""
      self.check_box_1.checked = False

    except Exception as e:
      Notification(f"Submission failed: {str(e)}", style="danger").show()