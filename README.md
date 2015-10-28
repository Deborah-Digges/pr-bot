# pr-bot
A Pull Request Hook that comments on pull requests from users who are contributing to the repository for the first time

## Instructions to set up pr-bot

1. Fill in your credentials in `app.properties`
2. Create a [heroku account](https://www.heroku.com/)
3. Create a heroku app: `heroku create`
4. Deploy the code: `git push heroku master`
5. Ensure that atleast one instance of the app is running: `heroku ps:scale web=1`
6. List your app with: `heroku apps`
7. The service is now running at `<heroku-app-name>.heroku.com`
8. Go to the settings page of the repository of interest.
9. Navigate to `WebHooks and Services`
10. Click on `Add WebHook`
11. For `Payload URL` enter `<heroku-app-name>.heroku.com/v1/PREvent`
12. Choose `Let me select Individual Events` and choose the `Pull Request Event`
13. Add Webhook
14. Get Someone to Open a PR on your repository :-)

## To self-host using Docker

1. Install [Docker](http://docs.docker.com/installation/) and [Compose](https://docs.docker.com/compose/install/). OSX users can skip above two and install [Docker Toolbox](https://www.docker.com/docker-toolbox)
2. Move to this directory, and run `docker-compose up web`. It will install all the requirements on the first run
3. Follow steps 8 through 14 in the previous list. In the `Payload URL` section of the `Add webhook` page of your Github repo settings, add `<your-public-ip:5000|Public-URL>/v1/PREvent`
4. For development purposes, you can use [Ngrok](https://ngrok.io) to set up a temporary local tunnel and make your local server accessible via a public URL.

## To Deploy on Google App Engine

1. Install [Google App Engine SDK for Python](https://cloud.google.com/appengine/downloads?hl=en_US).
2. Go to [Google Cloud Console](https://console.developers.google.com) and Create a project. [Here](https://cloud.google.com/appengine/docs) is a quickstart. 
3. Copy the application id of the created project and paste it in `application` parameter of `app.yaml` file. 
4. Follow steps 8 through 14 in the [instruction](#instructions-to-set-up-pr-bot) list. In the `Payload URL` section of the `Add webhook` page of your Github repo settings, add `<your-application-id>.appspot.com/v1/PREvent`
5. Open the folder in Google App Engine Launcher as an existing project by Going to File -> Add Existing Application and deploy. 
6. Alternatively, deploy through command line by running `appcfg.py -A <YOUR_APPLICATION_ID> update path-to-root-appengine-dir/`.

## Configuration

1. Customize the  `message` in `app.properties`
2. Customize `new-users` in `app.properties`. When set to true, a comment is only made on a PR made by a new contributor.

## Try It Out!
Submit a PR to this repository

###### Made with :heart: - [@Deborah-Digges](http://github.com/Deborah-Digges)
