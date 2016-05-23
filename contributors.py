"""
    Gets the list of people who have contributed to the project
"""

from Config import Config
import requests


def _getContributorList(response):
    contributors = []
    next_url = response.links.get('next', None)
    contributors.extend([contributor['id'] for contributor in response.json()])

    while next_url and next_url['url']:
        response = requests.get(next_url['url'], auth=())
        next_url = response.links.get('next', None)
        contributors.extend([contributor['id'] for contributor in response.json()])
    return contributors


def getContributorList(ownerLoginName, repoName):
    """
        Given a Github username and the repository repoName
        Returns a list of contributor ids
    """
    try:
        config = Config('app.properties')
        url = config.getProperty('contributors', 'url').format(ownerLoginName, repoName)
        username = config.getProperty('DEFAULT', 'username')
        password = config.getProperty('DEFAULT', 'password')
        response = requests.get(url, auth=(username, password))
        return _getContributorList(response)
    except requests.exceptions.RequestException:
        return []