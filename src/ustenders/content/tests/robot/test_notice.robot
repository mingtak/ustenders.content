# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s ustenders.content -t test_notice.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src ustenders.content.testing.USTENDERS_CONTENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_notice.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Notice
  Given a logged-in site administrator
    and an add notice form
   When I type 'My Notice' into the title field
    and I submit the form
   Then a notice with the title 'My Notice' has been created

Scenario: As a site administrator I can view a Notice
  Given a logged-in site administrator
    and a notice 'My Notice'
   When I go to the notice view
   Then I can see the notice title 'My Notice'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add notice form
  Go To  ${PLONE_URL}/++add++Notice

a notice 'My Notice'
  Create content  type=Notice  id=my-notice  title=My Notice


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the notice view
  Go To  ${PLONE_URL}/my-notice
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a notice with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the notice title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
