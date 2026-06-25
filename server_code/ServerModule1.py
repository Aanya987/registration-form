import anvil.server
from anvil.tables import app_tables

@anvil.server.callable
def submit_registration(name, mailid, branch, response):
  # Save data to Data Table
  app_tables.srm_responses.add_row(
    name=name,
    mailid=mailid,
    branch=branch,
    response=response
  )

  # Call email function from ServerModule2
  anvil.server.call('send_registration_email', name, mailid, branch, response)

  return "Your response has been recorded successfully!"