# A step-by-step tutorial on how to create a Google API key and enable the YouTube Data API v3:

## Go to the Google Cloud Platform Console:
Navigate to the Google Cloud Platform Console at https://console.cloud.google.com/. Sign in with your Google account. If you don't have a Google account, you'll need to create one.

## Create a new project:
Click on the project dropdown in the top-left corner, then click the "New Project" button at the top-right corner of the modal. Fill in the project name, organization, and location if needed, then click "Create" to create the project.

## Enable the YouTube Data API v3:
After the project has been created, you'll be redirected to the project dashboard. Click on the hamburger menu (three horizontal lines) in the top-left corner, and then click on "APIs & Services" > "Library". In the search bar, type "YouTube Data API v3" and click on the first result. On the YouTube Data API v3 page, click "Enable" to enable the API for your project.

## Create an API key:
Once the API is enabled, you'll be redirected to the API overview page. Click on "Create credentials" at the top. In the "Create credentials" modal, select "API key" from the dropdown. Click "Create" to generate the API key.

## Restrict the API key (optional, but recommended):
After the API key has been created, click on the "Restrict key" button. You can restrict the key by selecting specific APIs, setting up application restrictions, and setting up API key restrictions (such as limiting the number of requests per day). Make sure to save your changes.

## Copy the API key:
Once you have created and restricted your API key, you will see it in the "Credentials" section. Click the "Copy" button next to the API key to copy it to your clipboard.

## Use the API key in your code:
Replace the api_key placeholder in your code with the copied API key:
