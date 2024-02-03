from myvidu.settings import env
import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Load env variables
SERVER_PORT = env("SERVER_PORT")
OPENVIDU_URL = env("OPENVIDU_URL")
OPENVIDU_SECRET = env("OPENVIDU_SECRET")

print(SERVER_PORT, OPENVIDU_URL, OPENVIDU_SECRET)


@api_view(["POST"])
def initialize_session(request):
    """
    # response.json()
    {
      "id": "ses_NtBoDI92QI",
      "object": "session",
      "sessionId": "ses_NtBoDI92QI",
      "createdAt": 1706452568389,
      "recording": false,
      "broadcasting": false,
      "mediaMode": "ROUTED",
      "recordingMode": "MANUAL",
      "defaultRecordingProperties": {
          "name": "",
          "hasAudio": true,
          "hasVideo": true,
          "outputMode": "COMPOSED",
          "recordingLayout": "BEST_FIT",
          "resolution": "1280x720",
          "frameRate": 25,
          "shmSize": 536870912
      },
      "customSessionId": "",
      "forcedVideoCodec": "MEDIA_SERVER_PREFERRED",
      "allowTranscoding": false,
      "connections": {
          "numberOfElements": 0,
          "content": []
        }
      }
    """
    try:
        body = request.data
        response = requests.post(
            url=(OPENVIDU_URL + "openvidu/api/sessions"),
            verify=False,
            auth=("OPENVIDUAPP", OPENVIDU_SECRET),
            headers={'Content-type': 'application/json'},
            json=body
        )

        response.raise_for_status()
        return Response(data=response.json()["sessionId"])
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 409:
            return Response(request.data["customSessionId"])
        else:
            return err


@api_view(["POST"])
def create_connection(request, sessionId):
    """
    {
      "id": "con_UmQtnpXY8w",
      "object": "connection",
      "status": "pending",
      "connectionId": "con_UmQtnpXY8w",
      "sessionId": "ses_RWpATKDT4j",
      "createdAt": 1706530424973,
      "type": "WEBRTC",
      "record": true,
      "role": "PUBLISHER",
      "kurentoOptions": null,
      "customIceServers": [],
      "rtspUri": null,
      "adaptativeBitrate": null,
      "onlyPlayWithSubscribers": null,
      "networkCache": null,
      "serverData": "",
      "token": "ws://localhost:4443?sessionId=ses_RWpATKDT4j&token=tok_MAi7GxucmWFxrX2J",
      "activeAt": null,
      "location": null,
      "ip": null,
      "platform": null,
      "clientData": null,
      "publishers": null,
      "subscribers": null
    }
    """
    body = request.data
    response = requests.post(
        url=(OPENVIDU_URL + "openvidu/api/sessions/" + sessionId + "/connection"),
        verify=False,
        auth=("OPENVIDUAPP", OPENVIDU_SECRET),
        headers={'Content-type': 'application/json'},
        json=body
    )
    return Response(data=response.json()["token"])
