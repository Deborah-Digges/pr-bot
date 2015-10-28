from contributors import getContributorList
from logging.handlers import RotatingFileHandler

from Config import Config
from Constants import *
from flask import Flask
from flask import request
import json
import logging
import os
import requests
import sys



app = Flask(__name__)

config = Config('app.properties')
username = config.getProperty('DEFAULT', 'username')
password = config.getProperty('DEFAULT', 'password')
message = config.getProperty('comments', 'message')
newUsersOnly = config.getBoolean('DEFAULT', 'new-users')
postPREndPoint = config.getProperty('DEFAULT', 'end-point')

@app.route(postPREndPoint, methods=["POST"])
def postPRCommentToNewContributor():

    pullRequestEvent = json.loads(request.data)

    # Only comment on PRs that have just been opened
    if(pullRequestEvent[ACTION] == OPENED):
        pullRequest = pullRequestEvent[PULL_REQUEST]

        githubLoginName = pullRequest[USER][LOGIN]
        githubUserId = pullRequest[USER][ID]
        ownerLoginName = pullRequest[BASE][REPO][OWNER][LOGIN]
        repoName = pullRequest[BASE][REPO][NAME]

        url = pullRequest[LINKS][COMMENTS][HREF]
        comment = message.format(githubLoginName)
        data = BODY_FORMAT.format(comment)

        # Only comment on PRs by new contributors
        contributor_list = getContributorList(ownerLoginName, repoName)

        try:
            # If the flag has been set to only send the message to new users
            if newUsersOnly:
                # Then check if the user is a past contributor
                if githubUserId not in contributor_list:
                    response = requests.post(url, auth=(username, password), data=data)
                    app.logger.info(COMMENT_MADE_MESSAGE.format(
                        githubLoginName, githubUserId, url, contributor_list))
                else:
                    app.logger.info(COMMENT_NOT_MADE_MESSAGE.format(
                        githubLoginName, githubUserId, url, contributor_list))

            else:
                response = requests.post(url, auth=(username, password), data=data)
                app.logger.info(COMMENT_MADE_MESSAGE.format(
                    githubLoginName, githubUserId, url, contributor_list))

        except requests.exceptions.RequestException as e:
            app.logger.warning(COMMENT_NOT_MADE_MESSAGE.format(
                githubLoginName, githubUserId, url, contributor_list))

    return DONE


if __name__ == MAIN:
    # Add a stream handler as well as a file handler
    fileHandler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    app.logger.addHandler(fileHandler) 
    streamHandler = logging.StreamHandler()
    app.logger.addHandler(streamHandler)
    app.logger.setLevel(logging.INFO)
    port = int(os.environ.get(PORT, 5000))
    app.run(host='0.0.0.0', port=port)
