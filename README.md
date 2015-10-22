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

## Configuration

1. Customize the  `message` in `app.properties`
2. Customize `new-users` in `app.properties`. When set to true, a comment is only made on a PR made by a new contributor.

## Try It Out!
Submit a PR to this repository

###### Made with :heart: - [@Deborah-Digges](http://github.com/Deborah-Digges)
