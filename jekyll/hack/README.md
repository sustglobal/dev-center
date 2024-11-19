# Running Locally With Docker
Check out this workflow if installing Jekyll locally causes issues.

## Test

Make sure your current working directly is the `hack` folder!

Run `docker compose up`
Navigate to [http://localhost:4000/](http://localhost:4000/)

Changes you make in the _docs folder will be automatically rebuilt, just make sure to refresh the browser to see the latest changes!

## Ready for PR

When you're ready for a PR:

Change your terminal to the root folder of the dev-center project `cd ../..`
Run `docker run -p 4000:4000 -v $(pwd):/app hack-app "/bin/bash" "-xec" "cd jekyll && bundle install && bundle exec jekyll build"`

**IMPORTANT**
When commiting, make sure the .nojekyll file isn't deleted. A git commit -am _will_ delete this file!
