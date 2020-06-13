A dockerized micro service for a saas app.
Our API allows subscriptions to a saas app, it also includes documentation of all allowed operations and you can test it straight from our server. No need for external testers like postman. We use our integrated curl setup to test our endpoints.
We store user details, their plans, current subscriptions and all transactions. How To:

1. All GET requests are to get information(retrieve what has been previously stored).
   2 all POST are to add information(create new users, transactions etc.)
2. All upt requests are to update stored data
3. Patch is to overwrite.
4. Delete deletes all stored data.
   E.g subscription.microapi.dev/api/plan/11/delete will delete a plan with the id 11.
   {ID} parameters relate to the id of a particular object. Every list, user, transaction and subscriptions are given ids. Use this to access them. Please note that two models can have the same id, since they exist as separate entities.
   To return data as json, please add /v1.json to the url. It also supports yaml, which can be gotten by appending /v1.json
   Also, a much more sophisticated doc is available by appending /redoc/.

This is Team Gold's backend Task
