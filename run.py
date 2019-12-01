import requests
requests.packages.urllib3.disable_warnings()      # Disable warnings. Living on the wild side..

def getRoomList():
    url = WEBEX_TEAMS_URL + 'rooms'
    headers = {'Content-Type': "application/json", 'Authorization': WEBEX_TEAMS_TOKEN}
    res = requests.get(url=url, headers=headers)
    return res.json()['items']

def getRoomMembers(roomId):
    url = WEBEX_TEAMS_URL + 'memberships?roomId=' + roomId
    headers = {'Content-Type': "application/json", 'Authorization': WEBEX_TEAMS_TOKEN}
    res = requests.get(url=url, headers=headers)
    return res.json()['items']

def main():
    print('\nGetting list of rooms...')
    rooms = getRoomList()
    print('\nRoom list:')
    for room in rooms:
        print(room['title'] + '\t' + room['id'])
#
    print('\n\n\nWhich roomId would you like to query?\n')
    roomId = input()
    members = getRoomMembers(roomId)
#
    print('\nThe room members are:\n')
    emails = []
    for member in members:
        print(member['personDisplayName'] + '\t' + member['personEmail'])
        emails.append(member['personEmail'])

    print('list of e-mails:')
    for email in emails:
        print(email)
    print('\n\n\nDone!')


##############################

WEBEX_TEAMS_TOKEN = 'Bearer ' + 'MDBmYjA4NDgtM2QwZi00Yjk5LTkxNzUtMTc3YTg4MDVjMzdjZjY0ZTY4NGEtZjYx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
WEBEX_TEAMS_URL = 'https://api.ciscospark.com/v1/'
main()
